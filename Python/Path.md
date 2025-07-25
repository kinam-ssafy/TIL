# Python 파일 내용 정리

## 📄 01\_basic.py

`pathlib` 모듈을 사용하여 현재 작업 디렉토리, 홈 디렉토리 등 기본 경로를 다루고, 파일의 이름과 확장자를 분리하는 방법을 보여줍니다.

```python
from pathlib import Path
from pprint import pprint as print


# 경로 다루기 

# 현재 작업 디렉토리
current_path = Path.cwd()
print(f'현재 작업 경로 : {current_path}')

# 홈 디렉토리
home_path = Path.home()
print(f'홈 디렉토리 : {home_path}')

# 특정 경로
specific_path = Path('home/user/documents/file.txt')
print(f'특정 경로 : {specific_path}')

# 경로 결합 하기
new_path = Path('documents') / 'subfolder' / 'file.txt'
print(f'경로 합치기 : {new_path}')


# 파일 다루기

# 파일명만 확인하기
file_name = specific_path.name
print(f'파일명 확인 : {file_name}')

# 파일 확장자를 제외한 이름
stem = specific_path.stem
print(f'파일명 확인 : {stem}')

# 파일 확장자
suffix = specific_path.suffix
print(f'파일 확장자 확인 : {suffix}')
```

## 📄 02\_create.py

`pathlib`를 이용해 새 폴더(`new_directory`)와 파일(`new_file.txt`, `new.md`)을 생성합니다. 특히, `write_text`로 파일에 내용을 쓰고, `open`과 'a' 모드를 사용하여 기존 파일에 여러 줄의 텍스트를 추가하는 방법을 다룹니다.

```python
from pathlib import Path


# 폴더 생성
# exist_ok : True (폴더가 존재할 경우 에러 발생하지 않음)
new_dir = Path('new_directory')
new_dir.mkdir(exist_ok=True)

# 파일 생성
Path('new_file.txt').write_text("Hello, World!")

# 새로만든 폴더 내부에 파일 생성
new_file = new_dir / 'new.md'
new_file.write_text('# 새로 만들기', encoding='utf-8')

# 작성된 파일에 이어서 여러 줄 쓰기
with new_file.open('a', encoding='utf-8') as file:
    file.write('\n')
    file.write('* First line\n')
    file.write('* Second line\n')
    file.write('* Third line\n')
```

## 📄 03\_file\_info.py

`pathlib`의 `iterdir()`를 사용하여 현재 디렉토리의 모든 파일과 폴더 목록을 가져옵니다. 반복문을 통해 각 항목이 파일인지 폴더인지 `is_file()`과 `is_dir()`로 확인하고 이름을 출력합니다.

```python
from pathlib import Path
# 현재 위치의 파일 목록 보기
current_path = Path.cwd()

print(current_path.iterdir()) # <generator object Path.iterdir at 0x000001F6010147B0>
# 반복문을 이용해 내용 확인하기
for item in current_path.iterdir():
    print(item)             # 파일/폴더
    print(item.name)        # 파일/폴더 이름만 출력
    print('-----')

# 파일/폴더 여부 확인
for item in current_path.iterdir():
    if item.is_file():
        print(f'파일 : {item.name}')
    elif item.is_dir():
        print(f'폴더 : {item.name}')
    else:
        print(item.name)
```

## 📄 04\_search.py

`pathlib`의 `glob`과 `rglob`를 사용하여 특정 패턴의 파일을 검색하는 방법을 보여줍니다. `glob('*.py')`으로 현재 디렉토리의 파이썬 파일을, `rglob('*_*')`으로 모든 하위 디렉토리에서 이름에 언더스코어(\_)가 포함된 파일을 찾습니다.

```python
from pathlib import Path

current_path = Path.cwd()

# 특정 패턴의 파일 찾기
for python_file in current_path.glob('*.py'):
    print(python_file.name)


# 재귀적으로 모든 하위 디렉토리 검색
for file in current_path.rglob('*.txt'):
    print(file.name)

# 응용하기
# 언더스코어가 1개를 가지는 파일 리스트 생성하기
result = []
for file in current_path.rglob('*_*'):  # 언더스코어를 가진 모든 파일, 폴더 검색
    if file.is_file() and file.name.count('_') == 1:   # 파일이면서 언더스코어가 1개라면
        result.append(file.name)     # 결과에 담기

print(result)
```

## 📄 05\_read\_file.py

`pathlib`를 사용하여 텍스트 파일을 읽는 다양한 방법을 소개합니다. `read_text()`로 파일 전체를 한 번에 읽거나, `open()`과 함께 `read()`, `readline()`, `readlines()`를 사용하여 내용을 읽어올 수 있습니다.

```python
from pathlib import Path


file_path = Path('new_directory/new.md')

# Text를 바로 가져오는 방법
print(file_path.read_text(encoding='utf-8'))

# open 메서드를 이용한 방법
with file_path.open('r', encoding='utf-8') as file:
    print(file)   # <_io.TextIOWrapper name='new_dir\\new.md' mode='r' encoding='utf-8'> 
    print(file.read())


# 한 줄씩 라인 별로 읽어 오기
with file_path.open('r', encoding='utf-8') as file:
    print(file.readline()) # # 새로 만들기
    print(file.readline()) # * First line


# 텍스트를 리스트로 가져오기
with file_path.open('r', encoding='utf-8') as file:
    print(file.readlines()) # ['# 새로 만들기\n', '* First line\n', '* Second line\n', '* Third line\n']
```

## 📄 06\_JSON\_read.py

JSON 파일을 읽고 파이썬 객체(딕셔너리)로 변환하는 방법을 설명합니다. `json.loads()`는 JSON 형식의 문자열을, `json.load()`는 파일 객체에서 직접 데이터를 읽어와 변환합니다.

```python
import json
from pathlib import Path
from pprint import pprint as print

# JSON 파일 읽어오기
json_file = Path('sample_data/books_20.json')

json_text = json_file.read_text(encoding='utf-8')  # JSON은 문자열
print(json_text)
print(type(json_text))  # <class 'str'>

# loads 사용 (JSON 문자열을 변환할 때 사용)
data = json.loads(json_text) #  변환
# print(data)
print(type(data))  # <class 'dict'>

# load 사용 (JSON 파일에서 바로 읽어와서 변환할 때 사용)
json_file = Path('sample_data/books_20.json')
with json_file.open(encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(type(data))   # <class 'dict'>
```

## 📄 07\_JSON\_write.py

파이썬 딕셔너리 객체를 JSON 파일로 저장하는 방법을 보여줍니다. `json.dumps()`는 딕셔너리를 JSON 형식의 문자열로 변환하며, `json.dump()`는 파일에 직접 씁니다. `ensure_ascii=False`는 한글이 깨지지 않게 하고, `indent=4`는 가독성을 높여줍니다.

```python
import json
from pathlib import Path


# JSON 파일로 저장하기
data = {
    'name': '파일 저장하기',
    'value': 20
}

# dumps 사용 (dictionary를 json 문자열로 변환)
json_string = json.dumps(data, ensure_ascii=False, indent=4)

# JSON 파일을 생성
new_json_1 = Path('sample_data/sample1.json')
new_json_1.write_text(json_string, encoding='utf-8')


# dump 사용 (직접 dictionary를 JSON 파일로 저장할 때 사용)
new_json_2 = Path('sample_data/sample2.json')
with new_json_2.open('w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
```