# JavaScript DOM 조작과 Event 실습

## 📚 목차

1. [DOM 조작과 Event](#dom-조작과-event)
2. [Input Event](#input-event)
3. [입력 유효성 확인 실습](#입력-유효성-확인-실습)
4. [Drag Event](#drag-event)
5. [카드 순서 바꾸기 실습](#카드-순서-바꾸기-실습)
6. [Scroll Event](#scroll-event)
7. [스크롤 시 나타나는 요소 실습](#스크롤-시-나타나는-요소-실습)
8. [스크롤 진행률 표시 실습](#스크롤-진행률-표시-실습)
9. [Parallax Scroll 실습](#parallax-scroll-실습)
10. [참고: 고급 실습](#참고-고급-실습)

---

## DOM 조작과 Event

### DOM이란?

**DOM (Document Object Model)**
- 웹 페이지의 모든 내용을 JavaScript가 이해하고 조작할 수 있도록 만든 구조화된 모델

### DOM 조작이란?

**DOM 조작**
- JS가 웹페이지의 뼈대(HTML)와 디자인(CSS)을 실시간으로 통제하는 핵심 기술

### Event란?

**Event**
- 웹 페이지 내에서 발생하는 모든 사건을 말함
- JavaScript가 이를 감지하여 우리가 원하는 특정 동작을 실행하도록 만드는 방아쇠 역할

### DOM 조작과 Event 처리의 의미

DOM 조작과 Event 처리는 웹페이지를 단순한 정적인 문서가 아니라, 사용자와 끊임없이 대화하고 반응하는 **살아있는 인터페이스**로 만들어줍니다.

### DOM 조작과 Event 처리 활용

**1. 즉각적인 피드백**
- 사용자와 상호 작용
- 실시간 유효성 확인

**2. 효율적인 정보 관리**
- 평소에는 숨겨 두었다가 필요할 때 보여줌

**3. 시각적 매력과 몰입감**
- 사용자 서비스 이용 경험 개선

---

## Input Event

### Input Event란?

**Input Event**
- 데이터를 입력할 때마다 발생하는 이벤트

### 유사한 입력 이벤트 비교

| 이벤트 | 발생 시점 | 활용 |
|--------|----------|------|
| **Input Event** | 요소의 value(값)이 변경될 때 | 붙여넣기에도 반응하는 유효성 검사 가능 |
| **Keyup Event** | 키보드 키가 눌렸다가 떼어질 때 | 특정 키(예: Enter 키)를 눌렀을 때만 동작 수행 |

---

## 입력 유효성 확인 실습

### 실습 목표

최대 글자 개수를 넘어서면 사용자에게 알려주기

### HTML 구조

```html
<h1>텍스트 입력 제한 (20자)</h1>
<input type="text" 
       class="text-input" 
       id="textInput" 
       placeholder="최대 20자">
<div class="counter" id="counter">0 / 20</div>
```

### CSS 스타일

```css
body {
  margin: 20px;
  background: white;
}

.text-input {
  width: 300px;
  padding: 10px;
  border: 2px solid black;
}

/* 20자를 넘어갔을 때의 스타일 */
.text-input.error {
  background-color: #ffcccc;
  animation: shake 0.5s;
}

/* 움직임을 정의, 이름은 shake */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}

.counter {
  margin-top: 10px;
}
```

### CSS Animation

**CSS animation**
- JS를 사용하지 않고도 복잡한 움직임을 구현할 수 있게 해주는 CSS의 기능
- 시작부터 끝까지 애니메이션의 전반적인 규칙을 정의

**주요 animation 속성들**
- `animation-name`: 어떤 동작을 할지 (Keyframes 이름 지정)
- `animation-duration`: 몇 초동안 진행할지
- `animation-timing-function`: 속도 변화 (느리게, 빠르게 등)

### CSS keyframes

**@keyframes**
- CSS 애니메이션의 개별 동작 단계와 변화 지점을 정의하는 규칙
- `@keyframes`라는 특별한 문법으로 정의

```css
/* 애니메이션의 이름은 'pulse'입니다. */
@keyframes pulse {
  0% { 
    /* 0%: 시작 지점 (초기 상태) */
    transform: scale(1);  /* 원래 크기 */
    opacity: 1;           /* 불투명도 100% */
  }
  50% { 
    /* 50%: 중간 지점 */
    transform: scale(1.2);  /* 크기 1.2배 */
    opacity: 0.5;           /* 반투명 */
  }
  100% { 
    /* 100%: 종료 지점 */
    transform: scale(1);  /* 다시 원래 크기로 돌아옵니다. */
    opacity: 1;
  }
}
```

### CSS transforms

**transform**
- 요소를 이동, 회전, 크기 조절, 기울이기 등을 할 수 있게 해주는 CSS 속성
- `transform: [함수]([값]);` 형태로 사용

**transform에서 사용하는 주요 함수들**
- `translate(x, y)`: x축과 y축으로 이동
- `rotate(각도)`: 회전
- `scale(x, y)`: x축과 y축 배율 조절
- `skew(x각도, y각도)`: x축과 y축 기준으로 기울이기

### JavaScript 코드

```javascript
const textInput = document.querySelector('#textInput')
const counter = document.querySelector('#counter')
const maxLength = 20

textInput.addEventListener('input', function (e) {
  const currentLength = e.target.value.length
  
  if (currentLength > maxLength) {
    // 입력 제한
    e.target.value = e.target.value.substring(0, maxLength)
    
    // 에러 효과 추가
    e.target.classList.add('error')
    
    // 에러 효과 500ms 이후 제거
    setTimeout(() => {
      e.target.classList.remove('error')
    }, 500)
    return
  }
  
  // 글자 수 표시
  counter.textContent = `${currentLength} / ${maxLength}`
})
```

### 실행 결과

20자를 넘어가면:
- 붉은 색으로 변함
- 입력창이 좌우로 흔들림
- 최대 글자 수에서 더 이상 입력되지 않음

---

## Drag Event

### Drag Event란?

**Drag Event**
- 웹 페이지의 요소를 끌어서 이동시키는 과정에서 발생하는 이벤트
- 단순한 하나의 이벤트가 아닌, 끌기 시작부터 끌기 종료까지 모든 단계에서 순서대로 발생하는 여러 개의 이벤트 그룹

### Drag Event 중요한 조건

```html
<div draggable="true">드래그 가능한 요소</div>
```

- `draggable="true"`: 드래그 하려는 HTML 요소에서 이 속성을 추가해야 요소가 드래그될 수 있음
- 기본 값은 `false`로 요소가 드래그 되지 않음

### Drag Event 종류

#### 요소에서 발생하는 Event (마우스로 드래그 중인 요소에서 발생)

**1. dragstart 이벤트**
- 사용자가 요소를 끌기 시작하는 순간 끌리는 요소에서 발생

**2. drag 이벤트**
- 사용자가 요소를 끌고 다니는 과정 동안 끌리는 요소에서 계속 발생

**3. dragend 이벤트**
- 사용자가 마우스 버튼을 놓거나 드래그가 끝나는 순간 끌리는 요소에서 발생

#### 드래그 영역에서 발생하는 Event (드래그 되는 요소 아래 위치한 영역에서 발생)

**1. dragenter 이벤트**
- 끌고 있는 요소가 대상 영역 위로 들어올 때 해당 영역에서 발생

**2. dragover 이벤트**
- 끌고 있는 요소가 대상 영역 위에 머물고 있는 동안 해당 영역에서 발생
- 이 때, 기본 동작을 취소해야 drop이 가능 (마우스 포인터 모양이 다름)

**3. dragleave 이벤트**
- 끌고 있는 요소가 대상 영역 밖으로 벗어날 때 해당 영역에서 발생

**4. drop 이벤트**
- 끌고 있던 요소를 대상 영역 위에 놓는 순간 해당 영역에서 발생

---

## 카드 순서 바꾸기 실습

### 실습 목표

드래그 앤 드롭으로 카드의 순서를 바꾸는 실습

### HTML 구조

```html
<div class="container">
  <div class="card" draggable="true">
    <div class="card-number">1</div>
    <h3>카드 1</h3>
  </div>
  <div class="card" draggable="true">
    <div class="card-number">2</div>
    <h3>카드 2</h3>
  </div>
  <div class="card" draggable="true">
    <div class="card-number">3</div>
    <h3>카드 3</h3>
  </div>
  <div class="card" draggable="true">
    <div class="card-number">4</div>
    <h3>카드 4</h3>
  </div>
</div>
```

### CSS 스타일

```css
.container {
  display: flex;
  gap: 20px;
  padding: 20px;
}

.card {
  width: 200px;
  height: 250px;
  background: white;
  border: 2px solid #333;
  border-radius: 10px;
  padding: 20px;
  cursor: move;
  transition: all 0.3s;
}

.card.dragging {
  opacity: 0.5;
  transform: scale(1.05);
}

.card.drag-over {
  border-color: #4CAF50;
  border-style: dashed;
}
```

### JavaScript 코드

```javascript
const cards = document.querySelectorAll('.card')
let draggedElement = null

cards.forEach(card => {
  // 드래그 시작
  card.addEventListener('dragstart', function (e) {
    draggedElement = this
    this.classList.add('dragging')
  })
  
  // 드래그 종료
  card.addEventListener('dragend', function (e) {
    this.classList.remove('dragging')
    cards.forEach(c => c.classList.remove('drag-over'))
  })
  
  // 드래그 중인 요소가 다른 카드 위로 올 때
  card.addEventListener('dragover', function (e) {
    e.preventDefault()  // 기본 동작 취소 (drop 가능하게)
    this.classList.add('drag-over')
  })
  
  // 드래그 중인 요소가 카드를 벗어날 때
  card.addEventListener('dragleave', function (e) {
    this.classList.remove('drag-over')
  })
  
  // 드롭했을 때
  card.addEventListener('drop', function (e) {
    e.preventDefault()
    
    if (draggedElement !== this) {
      // 두 카드의 위치 교환
      const container = this.parentNode
      const allCards = [...container.children]
      const draggedIndex = allCards.indexOf(draggedElement)
      const targetIndex = allCards.indexOf(this)
      
      if (draggedIndex < targetIndex) {
        container.insertBefore(draggedElement, this.nextSibling)
      } else {
        container.insertBefore(draggedElement, this)
      }
    }
    
    this.classList.remove('drag-over')
  })
})
```

### 동작 원리

1. **dragstart**: 카드를 끌기 시작할 때 `dragging` 클래스 추가
2. **dragover**: 다른 카드 위로 드래그할 때 `drag-over` 클래스 추가
3. **drop**: 카드를 놓을 때 두 카드의 위치를 교환
4. **dragend**: 드래그 종료 시 모든 스타일 클래스 제거

---

## Scroll Event

### Scroll Event란?

**Scroll Event**
- 사용자가 페이지를 스크롤할 때 발생하는 이벤트
- 스크롤 위치를 감지하여 다양한 동적 효과를 구현할 수 있음

### Scroll Event 활용 예시

1. 스크롤 시 요소가 나타나는 효과
2. 스크롤 진행률 표시
3. Parallax(시차) 스크롤 효과
4. 무한 스크롤
5. 스크롤에 따른 애니메이션

---

## 스크롤 시 나타나는 요소 실습

### 실습 목표

스크롤하여 요소가 화면에 들어오면 애니메이션과 함께 나타나게 하기

### HTML 구조

```html
<section class="content">
  <div class="box">Box 1</div>
</section>
<section class="content">
  <div class="box">Box 2</div>
</section>
<section class="content">
  <div class="box">Box 3</div>
</section>
```

### CSS 스타일

```css
.content {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.box {
  width: 300px;
  height: 300px;
  background: #4CAF50;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
  color: white;
  opacity: 0;
  transform: translateY(50px);
  transition: all 0.6s ease;
}

.box.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### JavaScript 코드

```javascript
const boxes = document.querySelectorAll('.box')

function checkBoxes() {
  const triggerBottom = window.innerHeight * 0.8
  
  boxes.forEach(box => {
    const boxTop = box.getBoundingClientRect().top
    
    if (boxTop < triggerBottom) {
      box.classList.add('visible')
    } else {
      box.classList.remove('visible')
    }
  })
}

window.addEventListener('scroll', checkBoxes)
checkBoxes()  // 페이지 로드 시 한 번 실행
```

### 동작 원리

1. `getBoundingClientRect()`: 요소의 화면상 위치 정보를 가져옴
2. `triggerBottom`: 화면 높이의 80% 지점을 기준점으로 설정
3. 요소의 상단이 기준점보다 위에 있으면 `visible` 클래스 추가
4. CSS transition으로 부드러운 애니메이션 구현

---

## 스크롤 진행률 표시 실습

### 실습 목표

페이지 상단에 스크롤 진행률을 표시하는 바 만들기

### HTML 구조

```html
<div class="progress-bar" id="progressBar"></div>
<div class="content">
  <!-- 긴 콘텐츠 -->
</div>
```

### CSS 스타일

```css
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 0;
  height: 5px;
  background: linear-gradient(to right, #4CAF50, #8BC34A);
  z-index: 9999;
  transition: width 0.1s;
}

.content {
  height: 300vh;  /* 스크롤을 위한 긴 높이 */
  padding: 20px;
}
```

### JavaScript 코드

```javascript
const progressBar = document.querySelector('#progressBar')

window.addEventListener('scroll', function () {
  // 현재 스크롤 위치
  const scrollY = window.scrollY
  
  // 전체 스크롤 가능한 높이
  const scrollHeight = document.documentElement.scrollHeight - window.innerHeight
  
  // 스크롤 진행률 계산 (0~100)
  const scrollPercent = (scrollY / scrollHeight) * 100
  
  // 진행률 바의 너비 설정
  progressBar.style.width = `${scrollPercent}%`
})
```

### 주요 개념

- `window.scrollY`: 현재 스크롤 위치
- `document.documentElement.scrollHeight`: 문서 전체 높이
- `window.innerHeight`: 브라우저 창 높이
- 진행률 = 현재 위치 / 스크롤 가능한 전체 높이

---

## Parallax Scroll 실습

### Parallax Scroll이란?

**Parallax Scroll (시차 스크롤)**
- 스크롤할 때 배경과 전경이 서로 다른 속도로 움직여 깊이감을 주는 효과

### 실습 목표

여러 레이어가 다른 속도로 움직이는 시차 효과 구현

### HTML 구조

```html
<div class="parallax-container">
  <div class="layer" data-speed="0.5">
    <img src="mountain-far.png" alt="먼 산">
  </div>
  <div class="layer" data-speed="0.3">
    <img src="mountain-mid.png" alt="중간 산">
  </div>
  <div class="layer" data-speed="0.1">
    <img src="mountain-near.png" alt="가까운 산">
  </div>
</div>
```

### CSS 스타일

```css
.parallax-container {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.layer {
  position: absolute;
  width: 100%;
  height: 100%;
}

.layer img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

### JavaScript 코드 - 기본 버전

```javascript
const layers = document.querySelectorAll('.layer')

window.addEventListener('scroll', function () {
  const scrollY = window.scrollY
  
  layers.forEach(layer => {
    const speed = layer.dataset.speed
    const yPos = -(scrollY * speed)
    layer.style.transform = `translateY(${yPos}px)`
  })
})
```

### JavaScript 코드 - 심화 버전

```javascript
const parallaxContainer = document.querySelector('.parallax-container')
const layers = {
  sky: document.querySelector('.sky'),
  mountains: document.querySelector('.mountains'),
  trees: document.querySelector('.trees'),
  ground: document.querySelector('.ground')
}

// 각 레이어의 이동 속도
const speeds = {
  sky: 0.05,
  mountains: 0.15,
  trees: 0.25,
  ground: 0.35
}

window.addEventListener('scroll', function () {
  const scrollY = window.scrollY
  
  // 각 레이어를 다른 속도로 이동
  layers.sky.style.transform = `translateY(${scrollY * speeds.sky}px)`
  layers.mountains.style.transform = `translateY(${scrollY * speeds.mountains}px)`
  layers.trees.style.transform = `translateY(${scrollY * speeds.trees}px)`
  layers.ground.style.transform = `translateY(${scrollY * speeds.ground}px)`
})
```

### 동작 원리

1. 각 레이어에 `data-speed` 속성으로 이동 속도 설정
2. 스크롤 위치 × 속도 = 레이어 이동 거리
3. 속도가 작을수록 천천히 움직여 멀리 있는 것처럼 보임
4. 속도가 클수록 빠르게 움직여 가까이 있는 것처럼 보임

---

## 참고: 고급 실습

### 스크롤을 활용한 배경색 변경 실습

#### 동작 원리

스크롤 진행률은 0~1의 범위를 가지고 있음

```
스크롤 진행률 = 현재 스크롤 위치 / 스크롤 가능한 높이
```

이를 인덱스의 개수만큼 곱하고 내림 계산을 하면 구간 별로 Index를 다르게 가져갈 수 있음

**예시:**
- 배열의 길이가 5라면 진행도에 배열의 길이만큼 곱하고 내림을 하면 구간 별로 index가 계산됨
- 스크롤 진행률이 0.3 부근인 경우: 5를 곱하면 1.5가 되고 내림 계산을 하면 1이 됨 → index는 1로 설정
- 스크롤 진행률이 0.5 부근인 경우: 5를 곱하면 2.5가 되고 내림 계산을 하면 2가 됨 → index는 2로 설정
- 스크롤 진행률이 0.8 부근인 경우: 5를 곱하면 4.0이 되고 내림 계산을 하면 4가 됨 → index는 4로 설정

#### 실습 내용

스크롤에 따라 새벽, 아침, 낮, 저녁, 밤 총 5구간을 설정하여 배경색을 달리하고, 스크롤 진행도에 따라 해와 달의 움직임을 표현하는 실습

#### 주요 코드 (배경 인덱스)

```javascript
// 현재 스크롤 위치와 진행률 계산
const scrollY = window.scrollY
const scrollHeight = document.documentElement.scrollHeight - window.innerHeight
const progress = Math.min(scrollY / scrollHeight, 1)  // 0~1 사이 값

// 진행률을 색상 인덱스로 변환
const colorIndex = Math.floor(progress * colors.length)
const currentColorIndex = Math.min(colorIndex, colors.length - 1)

// 정해진 색상 적용
const currentColor = colors[currentColorIndex]
```

**진행률 계산에서 min을 사용한 이유:**
- 모바일이나 특정 브라우저에서 높이보다 스크롤 위치가 넘어가는 경우가 발생하여 진행률이 1 이상이 될 수 있음
- 0~1 사이의 값이 아닌 1 이상의 값이 나오는 경우가 발생하면 최대 Index를 넘어버리게 되어 min을 통해 제한

#### 해의 이동 코드

```javascript
// 해와 달의 위치 계산
function calculateCelestialPosition(progress, isNightTime = false) {
  const screenWidth = window.innerWidth
  
  if (!isNightTime) {
    // 해의 경로 (새벽 -> 낮만 떠 있도록): 0% 시 60% 진행률
    const normalizedProgress = Math.min(progress / 0.6, 1)
    const halfSunSize = sunSize / 2
    const x = -halfSunSize + normalizedProgress * (screenWidth - halfSunSize)
    
    // 저녁 (60%) 이후에는 해를 숨김
    sun.style.opacity = progress >= 0.6 ? 0 : 1
    return { x }
  }
}
```

#### 달의 이동 코드

```javascript
// 해의 경로 코드 이어서...

// 달의 경로 (저녁 -> 밤): 60% 시 100% 진행률
if (progress < 0.6) {
  moon.style.opacity = 0
  return null
}

// 남은 달의 이동 구간은 해의 이동구간 0.6을 뺀 0.4임
const normalizedProgress = (progress - 0.6) / 0.4  // 0~1 사이 값으로 정규화
const x = normalizedProgress * (screenWidth - moonSize)
moon.style.opacity = 1  // 달 표시
return { x }
```

#### 심화 기능

**1. 배경색을 부드럽게 변경하기 위한 선형 보간 계산 추가**

선형 보간: 두 값 사이를 부드럽게 이어주는 계산 방법
- 예: 빨강(255, 0, 0)과 파랑(0, 0, 255) 사이의 중간 색상 구하기
- 공식: `시작값 + (끝값 - 시작값) * 진행률`

**2. 해와 달을 곡선 형태로 표기하기 위한 포물선 곡선 계산 공식 추가**

기본 포물선 공식: `ax² + bx + c`

수학적 원리:
- `2 * normalizedX * (1 - normalizedX)` 포물선 공식
- normalizedX는 0~1 사이의 값 (진행률)

#### 실제 응용 서비스

연속된 이미지를 불러와서 스크롤 진행도에 따라 index를 변경하면 자연스럽게 동영상이 재생되는 효과를 낼 수 있음

---

### 가로 세로 스크롤 혼합 실습

#### 동작 원리

붉은 색 점선이 사용자에게 보여지는 화면일 때, 스크롤을 내려감과 함께 가로 배치된 요소가 이동하면서 보여짐

```
┌────────────────────────┐
│  sticky               │
│                        │
│  ┌──────────────┐     │
│  │ 가로 이동    │     │
│  └──────────────┘     │
│                        │
│  sticky               │
└────────────────────────┘
     ↓ 스크롤 방향
```

#### 실습을 위해 필요한 CSS 속성

1. 가로 스크롤하는 영역(`horizontal-track`)의 너비(`width`)와 실제 스크롤(`horizontal-container`) 되는 높이(`height`)가 같아야 함
2. `horizontal-track`의 너비는 개별 page의 개수로 동일하게 맞춤
3. 가로 정렬을 위해 Flex 설정이 필요함
4. 가로 정렬된 요소를 숨기기 위해 `overflow: hidden` 설정이 필요함
   - hidden을 하는 이유: 가로 스크롤바를 없애기 위함
5. 가로 스크롤 하는 동안 viewport에 고정하기 위해 `sticky` 설정이 필요함
   - 하지 않으면 스크롤과 함께 올라가버림
   - `fixed`인 경우 가로 이동 후에도 고정되어 있게 됨

#### 동작 원리 상세

스크롤을 하다가 `horizontal-container` 영역에서 가로 스크롤이 동작할 영역

스크롤을 하게 되면 `horizontal-container`의 top의 위치가 이동함

`horizontal-container`의 top의 위치가 스크롤되어 이동하는 거리 만큼 `horizontal-track`의 위치도 이동하여 화면에 출력하는 원리

#### 주요 코드

```javascript
function updateHorizontalPosition() {
  // getBoundingClientRect: 요소의 화면상 위치 정보
  const containerRect = horizontalContainer.getBoundingClientRect()
  const containerHeight = horizontalContainer.offsetHeight  // 컨테이너 전체 높이 (500vh)
  const windowHeight = window.innerHeight  // 브라우저 창 높이
  
  // 가로 스크롤 영역 (horizontal-container)이 화면에 보이는 동안만 실행
  if (containerRect.top <= 0 && containerRect.bottom >= windowHeight) {
    // 스크롤 진행률 계산 (0에서 1 사이 값)
    const scrollProgress = Math.abs(containerRect.top) / (containerHeight - windowHeight)
    
    // 가로 이동 거리 계산
    const maxMove = 400  // 4페이지 이동 (페이지1은 고정, 2~5페이지 이동 = 400vw)
    const moveDistance = scrollProgress * maxMove
    
    // translateX로 가로 이동 적용 (음수는 왼쪽으로 이동)
    horizontalTrack.style.transform = `translateX(-${moveDistance}vw)`
  }
}

window.addEventListener('scroll', updateHorizontalPosition)
```

---

## 핵심 정리

### 핵심 키워드

| 개념 | 설명 | 활용 |
|------|------|------|
| **Input Event** | 입력 값이 변경될 때 발생 | 실시간 유효성 검사 |
| **Drag Event** | 요소를 끌고 놓을 때 발생 | 순서 변경, 파일 업로드 |
| **Scroll Event** | 페이지를 스크롤할 때 발생 | 무한 스크롤, 애니메이션 |
| **CSS Animation** | JS 없이 움직임 구현 | 부드러운 전환 효과 |
| **Transform** | 요소의 변형 (이동, 회전, 크기) | 시각적 효과 |
| **Parallax** | 시차 스크롤 효과 | 깊이감 표현 |

### 주요 메서드 정리

```javascript
// 요소의 화면상 위치 정보
element.getBoundingClientRect()

// 현재 스크롤 위치
window.scrollY

// 문서 전체 높이
document.documentElement.scrollHeight

// 브라우저 창 높이
window.innerHeight

// CSS 애니메이션 제어
element.classList.add('animation-class')
element.classList.remove('animation-class')

// Transform 적용
element.style.transform = 'translateX(100px)'
```

---

## 마무리

이제 여러분은:
- Input Event로 실시간 유효성을 검사하고
- Drag Event로 요소의 순서를 변경하며
- Scroll Event로 동적인 애니메이션을 구현하고
- CSS Animation과 Transform으로 시각적 효과를 만들 수 있습니다

이러한 기술들을 조합하여 사용자 경험이 뛰어난 인터랙티브한 웹 페이지를 만들어보세요!

---

**작성일**: 2024  
**과정**: SSAFY JavaScript 관통 프로젝트 08
