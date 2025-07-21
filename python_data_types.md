# 데이터 타입

파이썬 자바 C 다 다름

---
### Python 인터프리터 사용 방법

- 터미널을 켜고 python -i를 입력하면 인터프리터 환경 실행
- 안되면 설치 시 add to path 안한 것
- 삭제하고 다시 설치하거나 

C:\Users\사용자이름\AppData\Local\Programs\Python\Python311 과 같이 파이썬 설치경로 확인

**시스템 환경 변수 편집:**

- `Win + S` 키를 누르고 "시스템 환경 변수 편집"을 검색하여 실행
- `환경 변수...` 버튼을 클릭
- `사용자 변수` 또는 `시스템 변수` 목록에서 `Path`를 찾아 선택하고 `편집...`을 누름
- `새로 만들기`를 클릭하여 위에서 찾은 Python 폴더 경로 두 개를 각각 추가
- `확인`을 눌러 모든 창을 닫기
- **중요:** Git Bash와 열려 있는 모든 터미널을 닫고 새로 시작해야 변경 사항이 적용

---
## 문자열

문자열은 문자들의 순서가 있는 변경 **불가능(불변성)**한 시퀀스 자료형

가변성인지 불변성인지 확인

```python
my_str = 'Hello'
my_str[1] = 'a'
```

len() 함수로 문자열의 길이 확인 가능


True, False와 같은 단어들 변수로 지정 불가 (에러는 나지 않았지만 최근 버전부터는 에러도 남)


str[1:5:-1] 과 같이 불러오면 아무것도 안뜸

str[1:5] 는 -> 방향으로 불러오는데 ::-1 은 <- 방향으로 불러옴

str[1:5][::-1] 과 같은 방식으로 뒤집기

f string

f'{variable}'

f'{num * 3}' 과 같이 {} 내에서 연산 가능




Boolean : True False 값만 가짐


-2 ** 4

2의 4제곱이 우선 계산 후 - 부호 붙음

---
pi처럼 무한소수를 나타내는 수를 소수점 n번째까지 불러오고 싶을 때

round() 함수 사용

round(pi, 10) >> 소수점 10번째 자리까지 반올림


---

## 이스케이프 시퀀스

| 예약 문자 | 기능 |
| --- | --- |
| `\n` | 줄 바꿈 |
| `\t` | 탭 |
| `\\` | 백슬래시 |
| `\'` | 작은 따옴표 |
| `\"` | 큰 따옴표 |



# 실습

```python
# 정수 자료형
student_count = 30
temperature = -5
balance = 0

# 실수 자료형
pi = 3.14
weight = 65.5
tax_rate = 0.1

# 지수 표현
# 1,230,000,000 (1.23 * 10^9)
big_number = 1.23e9
# 0.00314 (3.14 * 10^-3)
small_number = 3.14e-3

# 문자열 표현
print('Hello, World!')  # Hello, World!
print(type('Hello, World!'))  # str

# 중첩 따옴표
print(
    '문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.'
)  # 문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.
print(
    "문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다."
)  # 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.

# Escape sequence
# 따옴표 앞에 \를 붙여 문자로 인식시킴
print('He\'s a boy.')
# \n 은 줄바꿈(엔터)을 의미함
print('첫째 줄\n둘째 줄')

# 여러 줄 문자열을 작성할 때는 """ 또는 '''를 사용
multi_line_str = """
이것은
여러 줄로 이루어진
문자열입니다.
"""
print(multi_line_str)


# String Interpolation "f-string"
name = '홍길동'
age = 25
greeting = f'안녕하세요, 제 이름은 {name}이고 나이는 {age}살입니다.'
# 안녕하세요, 제 이름은 홍길동이고 나이는 25살입니다.
print(greeting)


# 문자열의 시퀀스 특징
my_str = 'hello'
# 1. 인덱싱
print(my_str[1])  # e


# 2. 슬라이싱
print(my_str[2:4])  # ll
print(my_str[:3])  # hel
print(my_str[3:])  # lo
print(my_str[::2])  # hlo
print(my_str[::-1])  # olleh

# 3. 길이
print(len(my_str))  # 5

# 4. 문자열은 불변
# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'

# 이것은
age = 10

# 주석입니다.
# print(age)

# 여러 줄 주석을 작성하는 방법은 다음과 같습니다.
"""
여러 줄 주석은
이렇게 작성할 수 있습니다.
"""
---------------------------------------
# 부동소수점 에러
result = 0.1 + 0.2
print(result == 0.3)  # False
print(result)  # 0.30000000000000004


# 해결 전
a = 3.2 - 3.1
b = 1.2 - 1.1

print(a)  # 0.10000000000000009
print(b)  # 0.09999999999999987
print(a == b)  # False

# 해결 후
from decimal import Decimal

a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a)  # 0.1
print(b)  # 0.1
print(a == b)  # True

-----------------------------------
numeral_system
# 2진수 10은 10진수로 2입니다. (1 * 2^1 + 0 * 2^0)
print(0b10)

# 8진수 30은 10진수로 24입니다. (3 * 8^1 + 0 * 8^0)
print(0o30)

# 16진수 10은 10진수로 16입니다. (1 * 16^1 + 0 * 16^0)
print(0x10)



```

[파이썬 튜터](https://pythontutor.com/)

파이썬 코드가 한 줄씩 어떻게 실행되는지 눈으로 보여주는 시각화도구

코드 작성 후 render all objects on the heap 실행