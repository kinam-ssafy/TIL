import sys
import os
from pathlib import Path
from datetime import datetime
import easyocr
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLabel, QTextEdit, 
                              QProgressBar, QFileDialog, QListWidget, QCheckBox,
                              QGroupBox, QGridLayout, QLineEdit, QScrollArea,
                              QSplitter, QMessageBox, QSpinBox, QDoubleSpinBox,
                              QComboBox)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QMimeData, QSize
from PyQt6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QIcon

import platform
import subprocess
import cv2
import numpy as np


def preprocess_image(image, apply_preprocessing=True):
    """OCR을 위한 이미지 전처리
    
    Args:
        image: OpenCV 이미지 (BGR)
        apply_preprocessing: 전처리 적용 여부
        
    Returns:
        전처리된 이미지 또는 원본 이미지
    """
    if not apply_preprocessing:
        return image
    
    # 그레이스케일 변환
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
    
    # 노이즈 제거 (Non-local Means Denoising)
    denoised = cv2.fastNlMeansDenoising(gray, h=10)
    
    # 대비 향상 (CLAHE - Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(denoised)
    
    # 적응형 이진화 (Adaptive Thresholding)
    # Otsu's method와 함께 사용
    _, binary = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 약간의 모폴로지 연산으로 텍스트 정리 (선택적)
    kernel = np.ones((2, 2), np.uint8)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    return binary


def sort_text_by_position(results, direction='vertical'):
    """텍스트를 위치 기반으로 정렬
    
    Args:
        results: OCR 결과 리스트 [(bbox, text, confidence), ...]
        direction: 'vertical' (위→아래, 좌→우) 또는 'horizontal' (좌→우, 위→아래)
        
    Returns:
        정렬된 텍스트 리스트와 신뢰도
    """
    if not results:
        return []
    
    # bbox의 좌상단 좌표를 기준으로 정렬
    if direction == 'vertical':
        # 세로 방향 읽기: Y좌표 우선, 같은 줄이면 X좌표
        # 줄 높이를 고려하여 같은 줄로 간주할 범위 설정
        sorted_results = sorted(results, key=lambda x: (
            round(x[0][0][1] / 30),  # Y 좌표를 30픽셀 단위로 그룹화 (같은 줄)
            x[0][0][0]  # 같은 줄 내에서는 X 좌표로 정렬
        ))
    else:
        # 가로 방향 읽기: X좌표 우선, 같은 열이면 Y좌표
        sorted_results = sorted(results, key=lambda x: (
            round(x[0][0][0] / 30),  # X 좌표를 30픽셀 단위로 그룹화 (같은 열)
            x[0][0][1]  # 같은 열 내에서는 Y 좌표로 정렬
        ))
    
    return sorted_results


class OCRWorker(QThread):
    """OCR 작업을 별도 스레드에서 처리"""
    progress = pyqtSignal(int, int, str)  # current, total, filename
    result_ready = pyqtSignal(str, str)  # filename, text
    finished = pyqtSignal(str)  # output_path
    error = pyqtSignal(str, str)  # filename, error_message
    
    def __init__(self, image_files, output_path, use_gpu=False, 
                 apply_preprocessing=True, min_confidence=0.3, 
                 sort_direction='vertical'):
        super().__init__()
        self.image_files = image_files
        self.output_path = output_path
        self.use_gpu = use_gpu
        self.apply_preprocessing = apply_preprocessing
        self.min_confidence = min_confidence
        self.sort_direction = sort_direction
        self.reader = None
        
    def run(self):
        try:
            # EasyOCR reader 초기화
            self.progress.emit(0, len(self.image_files), "EasyOCR 모델 로딩 중...")
            self.reader = easyocr.Reader(['ko', 'en'], gpu=self.use_gpu)
            
            all_results = []
            all_results.append("=" * 80)
            all_results.append("OCR 추출 결과")
            all_results.append(f"전처리: {'적용' if self.apply_preprocessing else '미적용'}, "
                             f"최소 신뢰도: {self.min_confidence:.1%}, "
                             f"정렬: {self.sort_direction}")
            all_results.append("=" * 80)
            all_results.append("")
            
            for idx, image_path in enumerate(self.image_files, 1):
                filename = Path(image_path).name
                self.progress.emit(idx, len(self.image_files), filename)
                
                try:
                    # 이미지 읽기 (한글 경로 지원)
                    img_array = np.fromfile(image_path, np.uint8)
                    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    
                    if image is None:
                        raise Exception("이미지를 읽을 수 없습니다")
                    
                    # 📌 개선 1: 이미지 전처리
                    processed_image = preprocess_image(image, self.apply_preprocessing)
                    
                    # OCR 수행 (전처리된 이미지 사용)
                    result = self.reader.readtext(processed_image)
                    
                    # 📌 개선 2: 신뢰도 기반 필터링
                    filtered_result = [
                        (bbox, text, conf) 
                        for bbox, text, conf in result 
                        if conf >= self.min_confidence
                    ]
                    
                    # 📌 개선 4: 레이아웃 기반 정렬
                    sorted_result = sort_text_by_position(filtered_result, self.sort_direction)
                    
                    # 텍스트 추출 (신뢰도 정보 포함)
                    text_lines = []
                    for bbox, text, confidence in sorted_result:
                        text_lines.append(f"{text} (신뢰도: {confidence:.1%})")
                    
                    text = '\n'.join(text_lines)
                    
                    # 통계 정보
                    total_detected = len(result)
                    filtered_count = len(filtered_result)
                    avg_confidence = sum(conf for _, _, conf in filtered_result) / len(filtered_result) if filtered_result else 0
                    
                    # 결과 저장
                    file_result = f"\n## 📄 {filename}\n"
                    file_result += "-" * 80 + "\n"
                    file_result += f"감지된 텍스트: {total_detected}개 | 필터링 후: {filtered_count}개 | 평균 신뢰도: {avg_confidence:.1%}\n"
                    file_result += "-" * 80 + "\n"
                    file_result += (text.strip() if text.strip() else "(신뢰도 기준을 만족하는 텍스트가 없습니다)") + "\n"
                    
                    all_results.append(file_result)
                    
                    # 실시간으로 각 파일 결과 전송
                    self.result_ready.emit(filename, file_result)
                    
                except Exception as e:
                    error_msg = f"오류 발생: {str(e)}"
                    file_result = f"\n## ❌ {filename}\n"
                    file_result += "-" * 80 + "\n"
                    file_result += error_msg + "\n"
                    
                    all_results.append(file_result)
                    self.error.emit(filename, error_msg)
                    self.result_ready.emit(filename, file_result)
            
            # 최종 결과 파일 저장
            final_text = "\n".join(all_results)
            with open(self.output_path, 'w', encoding='utf-8') as f:
                f.write(final_text)
            
            self.finished.emit(str(self.output_path))
            
        except Exception as e:
            self.error.emit("전체 프로세스", str(e))


class ImagePreviewWidget(QWidget):
    """드롭 가능한 이미지 미리보기 위젯"""
    files_dropped = pyqtSignal(list)
    
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.has_images = False
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 드롭 안내 레이블
        self.drop_label = QLabel("📦 이미지를 드래그하거나 클릭하여 선택하세요")
        self.drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drop_label.setStyleSheet("""
            QLabel {
                border: 3px dashed #aaa;
                border-radius: 10px;
                background-color: #f5f5f5;
                padding: 60px 20px;
                font-size: 14px;
                color: #666;
                min-height: 150px;
            }
        """)
        layout.addWidget(self.drop_label)
        
        # 이미지 미리보기 영역 (처음엔 숨김)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: 3px dashed #aaa;
                border-radius: 10px;
                background-color: #f5f5f5;
                min-height: 150px;
            }
        """)
        self.scroll_area.hide()
        
        self.image_container = QWidget()
        self.image_layout = QHBoxLayout()
        self.image_container.setLayout(self.image_layout)
        
        self.scroll_area.setWidget(self.image_container)
        layout.addWidget(self.scroll_area)
        
        self.setLayout(layout)
        
    def mousePressEvent(self, event):
        """클릭 시 파일 선택 대화상자 열기"""
        folder = QFileDialog.getExistingDirectory(self, "이미지 폴더 선택")
        if folder:
            self.files_dropped.emit([folder])
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            if self.has_images:
                self.scroll_area.setStyleSheet("""
                    QScrollArea {
                        border: 3px dashed #4a90e2;
                        border-radius: 10px;
                        background-color: #e8f4f8;
                        min-height: 150px;
                    }
                """)
            else:
                self.drop_label.setStyleSheet("""
                    QLabel {
                        border: 3px dashed #4a90e2;
                        border-radius: 10px;
                        background-color: #e8f4f8;
                        padding: 60px 20px;
                        font-size: 14px;
                        color: #4a90e2;
                        min-height: 150px;
                    }
                """)
            
    def dragLeaveEvent(self, event):
        if self.has_images:
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 3px dashed #aaa;
                    border-radius: 10px;
                    background-color: #f5f5f5;
                    min-height: 150px;
                }
            """)
        else:
            self.drop_label.setStyleSheet("""
                QLabel {
                    border: 3px dashed #aaa;
                    border-radius: 10px;
                    background-color: #f5f5f5;
                    padding: 60px 20px;
                    font-size: 14px;
                    color: #666;
                    min-height: 150px;
                }
            """)
        
    def dropEvent(self, event: QDropEvent):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        self.files_dropped.emit(files)
        
        # 스타일 복원
        if self.has_images:
            self.scroll_area.setStyleSheet("""
                QScrollArea {
                    border: 3px dashed #aaa;
                    border-radius: 10px;
                    background-color: #f5f5f5;
                    min-height: 150px;
                }
            """)
        else:
            self.drop_label.setStyleSheet("""
                QLabel {
                    border: 3px dashed #aaa;
                    border-radius: 10px;
                    background-color: #f5f5f5;
                    padding: 60px 20px;
                    font-size: 14px;
                    color: #666;
                    min-height: 150px;
                }
            """)
    
    def add_image(self, image_path):
        """이미지 썸네일 추가"""
        self.has_images = True
        self.drop_label.hide()
        self.scroll_area.show()
        
        # 썸네일 컨테이너
        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.setSpacing(5)
        
        # 이미지 레이블
        pixmap = QPixmap(str(image_path))
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, 
                                         Qt.TransformationMode.SmoothTransformation)
            img_label = QLabel()
            img_label.setPixmap(scaled_pixmap)
            img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            img_label.setStyleSheet("border: 1px solid #ddd; padding: 5px; background: white;")
            container_layout.addWidget(img_label)
        
        # 파일명 레이블
        name_label = QLabel(Path(image_path).name)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setWordWrap(True)
        name_label.setMaximumWidth(120)
        name_label.setStyleSheet("font-size: 10px; color: #666;")
        container_layout.addWidget(name_label)
        
        container.setLayout(container_layout)
        self.image_layout.addWidget(container)
        
    def clear_images(self):
        """모든 이미지 제거"""
        while self.image_layout.count():
            item = self.image_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        self.has_images = False
        self.scroll_area.hide()
        self.drop_label.show()
        
    def update_drop_text(self, count):
        """드롭 영역 텍스트 업데이트"""
        if count > 0:
            self.has_images = True
        else:
            self.has_images = False
            self.drop_label.show()
            self.scroll_area.hide()


class OCRApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_files = []
        self.output_path = None
        self.ocr_worker = None
        
        self.setWindowTitle("🔍 OCR 추출기 (개선 버전)")
        self.setMinimumSize(900, 700)
        
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        
        # 제목
        title = QLabel("🔍 이미지 OCR 텍스트 추출기 (개선 버전)")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)
        
        # 이미지 미리보기 영역
        self.image_preview = ImagePreviewWidget()
        self.image_preview.files_dropped.connect(self.on_files_dropped)
        main_layout.addWidget(self.image_preview)
        
        # 파일 목록 및 설정
        content_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # 왼쪽: 파일 목록
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        file_group = QGroupBox("📁 선택된 파일")
        file_layout = QVBoxLayout()
        
        self.file_list = QListWidget()
        self.file_list.setMaximumHeight(150)
        file_layout.addWidget(self.file_list)
        
        file_buttons = QHBoxLayout()
        clear_btn = QPushButton("🗑️ 목록 지우기")
        clear_btn.clicked.connect(self.clear_files)
        file_buttons.addWidget(clear_btn)
        file_layout.addLayout(file_buttons)
        
        file_group.setLayout(file_layout)
        left_layout.addWidget(file_group)
        
        # 📌 오른쪽: OCR 설정 (개선된 부분)
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        settings_group = QGroupBox("⚙️ OCR 설정")
        settings_layout = QGridLayout()
        
        # GPU 사용
        self.gpu_checkbox = QCheckBox("GPU 가속 사용")
        settings_layout.addWidget(self.gpu_checkbox, 0, 0, 1, 2)
        
        # 전처리 옵션 (새로 추가)
        self.preprocessing_checkbox = QCheckBox("이미지 전처리 적용")
        self.preprocessing_checkbox.setChecked(True)
        self.preprocessing_checkbox.setToolTip("노이즈 제거, 대비 향상, 이진화를 통해 OCR 정확도 향상")
        settings_layout.addWidget(self.preprocessing_checkbox, 1, 0, 1, 2)
        
        # 신뢰도 임계값 (새로 추가)
        confidence_label = QLabel("최소 신뢰도:")
        settings_layout.addWidget(confidence_label, 2, 0)
        
        self.confidence_spinbox = QDoubleSpinBox()
        self.confidence_spinbox.setRange(0.0, 1.0)
        self.confidence_spinbox.setSingleStep(0.05)
        self.confidence_spinbox.setValue(0.3)
        self.confidence_spinbox.setDecimals(2)
        self.confidence_spinbox.setSuffix(" (30%)")
        self.confidence_spinbox.setToolTip("이 값보다 낮은 신뢰도의 텍스트는 제외됩니다")
        self.confidence_spinbox.valueChanged.connect(
            lambda v: self.confidence_spinbox.setSuffix(f" ({int(v*100)}%)")
        )
        settings_layout.addWidget(self.confidence_spinbox, 2, 1)
        
        # 정렬 방향 (새로 추가)
        sort_label = QLabel("텍스트 정렬:")
        settings_layout.addWidget(sort_label, 3, 0)
        
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["세로 방향 (위→아래)", "가로 방향 (좌→우)"])
        self.sort_combo.setToolTip("OCR 결과를 정렬하는 방향")
        settings_layout.addWidget(self.sort_combo, 3, 1)
        
        settings_group.setLayout(settings_layout)
        right_layout.addWidget(settings_group)
        
        content_splitter.addWidget(left_panel)
        content_splitter.addWidget(right_panel)
        content_splitter.setStretchFactor(0, 1)
        content_splitter.setStretchFactor(1, 1)
        
        main_layout.addWidget(content_splitter)
        
        # 출력 경로 설정
        output_group = QGroupBox("💾 결과 파일 저장 위치")
        output_layout = QHBoxLayout()
        
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText("파일을 추가하면 자동으로 설정됩니다")
        self.path_edit.setReadOnly(True)
        output_layout.addWidget(self.path_edit, 4)
        
        path_btn = QPushButton("📂 경로 선택")
        path_btn.clicked.connect(self.select_output_path)
        output_layout.addWidget(path_btn, 1)
        
        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)
        
        # OCR 실행 버튼
        self.start_btn = QPushButton("▶️ OCR 시작")
        self.start_btn.clicked.connect(self.start_ocr)
        self.start_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 12px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """)
        main_layout.addWidget(self.start_btn)
        
        # 진행 상황
        progress_group = QGroupBox("📊 진행 상황")
        progress_layout = QVBoxLayout()
        
        self.progress_label = QLabel("대기 중...")
        progress_layout.addWidget(self.progress_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        progress_layout.addWidget(self.progress_bar)
        
        progress_group.setLayout(progress_layout)
        main_layout.addWidget(progress_group)
        
        # 결과 표시
        result_group = QGroupBox("📝 OCR 결과")
        result_layout = QVBoxLayout()
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("OCR 결과가 여기에 표시됩니다...")
        result_layout.addWidget(self.result_text)
        
        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)
        
        # 결과 파일 열기 버튼
        result_button_layout = QHBoxLayout()
        
        self.open_file_btn = QPushButton("📄 결과 파일 열기")
        self.open_file_btn.clicked.connect(self.open_result_file)
        self.open_file_btn.setEnabled(False)
        result_button_layout.addWidget(self.open_file_btn)
        
        self.open_folder_btn = QPushButton("📁 결과 폴더 열기")
        self.open_folder_btn.clicked.connect(self.open_result_folder)
        self.open_folder_btn.setEnabled(False)
        result_button_layout.addWidget(self.open_folder_btn)
        
        main_layout.addLayout(result_button_layout)
        
        # 스타일 적용
        self.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #ddd;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QPushButton {
                padding: 6px 12px;
                border-radius: 4px;
                border: 1px solid #ccc;
            }
            QPushButton:hover {
                background-color: #e8e8e8;
            }
        """)
        
    def on_files_dropped(self, files):
        """파일 드롭 이벤트 처리"""
        self.add_files(files)
        
    def add_files(self, files):
        """파일 목록에 이미지 추가"""
        valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif'}
        
        for file in files:
            path = Path(file)
            
            if path.is_file() and path.suffix.lower() in valid_extensions:
                if str(path) not in self.image_files:
                    self.image_files.append(str(path))
                    self.file_list.addItem(path.name)
                    self.image_preview.add_image(path)
            elif path.is_dir():
                for img_file in path.glob('*'):
                    if img_file.suffix.lower() in valid_extensions:
                        if str(img_file) not in self.image_files:
                            self.image_files.append(str(img_file))
                            self.file_list.addItem(img_file.name)
                            self.image_preview.add_image(img_file)
        
        self.update_drop_area()
        self.update_default_output_path()
        
    def clear_files(self):
        """파일 목록 초기화"""
        self.image_files.clear()
        self.file_list.clear()
        self.image_preview.clear_images()
        self.result_text.clear()
        self.update_drop_area()
        self.path_edit.clear()
        self.output_path = None
        
    def update_drop_area(self):
        """드롭 영역 텍스트 업데이트"""
        count = len(self.image_files)
        self.image_preview.update_drop_text(count)
            
    def update_default_output_path(self):
        """기본 출력 경로 설정"""
        if self.image_files and not self.output_path:
            first_image_path = Path(self.image_files[0])
            
            # 타임스탬프 생성 (YYMMDD_HHMMSS)
            timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
            filename = f"ocr_result_{timestamp}.txt"
            
            # 한글 경로 문제 방지: 홈 디렉토리나 현재 작업 디렉토리 사용
            try:
                # 원본 이미지 경로에 저장 시도
                default_output = first_image_path.parent / filename
                # 경로에 한글이 있는지 테스트 (파일 생성 테스트)
                test_file = default_output.parent / ".test_write"
                test_file.write_text("test", encoding='utf-8')
                test_file.unlink()
                self.output_path = str(default_output)
            except (OSError, UnicodeEncodeError):
                # 한글 경로 문제 시 홈 디렉토리 사용
                home_dir = Path.home() / "Documents"
                if not home_dir.exists():
                    home_dir = Path.home()
                default_output = home_dir / filename
                self.output_path = str(default_output)
                
            self.path_edit.setText(str(self.output_path))
            
    def select_output_path(self):
        """출력 파일 경로 선택"""
        if self.output_path:
            default_path = self.output_path
        else:
            timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
            default_path = str(Path.home() / f"ocr_result_{timestamp}.txt")
            
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "결과 파일 저장 위치", 
            default_path,
            "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            self.output_path = file_path
            self.path_edit.setText(file_path)
            
    def start_ocr(self):
        """OCR 프로세스 시작"""
        if not self.image_files:
            QMessageBox.warning(self, "경고", "이미지 파일을 먼저 추가해주세요!")
            return
        
        if not self.output_path:
            self.update_default_output_path()
        
        # UI 초기화
        self.result_text.clear()
        self.open_file_btn.setEnabled(False)
        self.open_folder_btn.setEnabled(False)
        self.start_btn.setEnabled(False)
        
        # 설정 값 가져오기
        use_gpu = self.gpu_checkbox.isChecked()
        apply_preprocessing = self.preprocessing_checkbox.isChecked()
        min_confidence = self.confidence_spinbox.value()
        sort_direction = 'vertical' if self.sort_combo.currentIndex() == 0 else 'horizontal'
        
        # OCR 작업 시작
        self.ocr_worker = OCRWorker(
            self.image_files, 
            self.output_path, 
            use_gpu,
            apply_preprocessing,
            min_confidence,
            sort_direction
        )
        self.ocr_worker.progress.connect(self.update_progress)
        self.ocr_worker.result_ready.connect(self.append_result)
        self.ocr_worker.finished.connect(self.finish_ocr)
        self.ocr_worker.error.connect(self.show_error)
        self.ocr_worker.start()
        
    def update_progress(self, current, total, filename):
        """진행률 업데이트"""
        if current == 0:
            self.progress_label.setText(filename)
        else:
            percentage = int((current / total) * 100)
            self.progress_bar.setValue(percentage)
            self.progress_label.setText(f"처리 중... ({current}/{total}) - {filename}")
            
    def append_result(self, filename, text):
        """결과를 실시간으로 추가"""
        self.result_text.append(text)
        # 자동 스크롤
        cursor = self.result_text.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.result_text.setTextCursor(cursor)
        
    def show_error(self, filename, error_msg):
        """에러 표시"""
        print(f"Error processing {filename}: {error_msg}")
        
    def finish_ocr(self, output_path):
        """OCR 완료 처리"""
        self.progress_label.setText(f"✅ 완료! ({len(self.image_files)}개 파일 처리)")
        self.progress_bar.setValue(100)
        self.open_file_btn.setEnabled(True)
        self.open_folder_btn.setEnabled(True)
        self.start_btn.setEnabled(True)
        
        QMessageBox.information(self, "완료", f"OCR이 완료되었습니다!\n결과 파일: {output_path}")
        
    def open_result_file(self):
        """결과 파일 열기"""
        if self.output_path and Path(self.output_path).exists():
            if platform.system() == 'Windows':
                os.startfile(self.output_path)
            elif platform.system() == 'Darwin':
                subprocess.call(['open', self.output_path])
            else:
                subprocess.call(['xdg-open', self.output_path])
        else:
            QMessageBox.warning(self, "오류", "결과 파일을 찾을 수 없습니다.")
            
    def open_result_folder(self):
        """결과 폴더 열기"""
        if self.output_path:
            folder = str(Path(self.output_path).parent)
        else:
            folder = str(Path.cwd())
            
        if platform.system() == 'Windows':
            os.startfile(folder)
        elif platform.system() == 'Darwin':
            subprocess.call(['open', folder])
        else:
            subprocess.call(['xdg-open', folder])


def main():
    app = QApplication(sys.argv)
    
    # 앱 스타일 설정
    app.setStyle('Fusion')
    
    window = OCRApp()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
