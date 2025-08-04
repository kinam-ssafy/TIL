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

문자열은 문자들의 순서가 있는 **변경 불가능(불변성)**한 시퀀스 자료형

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

---

## tuple

튜플의 불변 특성 -> 내부 동작에 사용
다중 할당, 값 교환, 함수 다중 반환 등

ex)

x, y = 10, 20 라고 하면

실제 내부 동작
(x, y) = (10, 20)
튜플로 (10, 20)에 할당되어 저장

x, y = 1, 2

x, y = y, x
처럼 값 교환에도 사용

실제 내부 동작
temp = (y, x) 튜플 생성
x, y = temp 튜플 풀어냄

튜플은 데이터의 **안정성**과 **무결성** 보장

---

## range

연속된 정수 시퀀스 생성하는 변경 불가능한(immutable) 자료형

반복문과 함께 사용. 반복 실행 시 유용

모든 숫자를 메모리에 저장하는 대신 시작 값, 끝 값, 간격이라는 **규칙**만 기억하여 메모리를 효율적으로 사용

range()는 1 or 2 or 3개의 인자 가질 수 있음

range(start, stop, step)

range(stop)
- 매개변수 하나면 stop으로 인식
- start는 0, step은 1 기본값으로 자동 설정
- range(5) >> 0, 1, 2, 3, 4

my_range_1 = range(5)
print(my_range_1) # range(0, 5) 라고 나옴

내부 값 확인하려면 list로 형변환 해야함

print(list(my_range_1)) # [0, 1, 2, 3, 4]

range(start, stop)
- 매개변수 두 개면 start와 stop으로 인식
- step은 1이 기본값
- range(2, 5) >> 2, 3, 4

range(start, stop, step)
- 모든 매개변수 직접 지정
- range(2, 10, 2) >> 2, 4, 6, 8

### range의 규칙

값의 범위 규칙
- stop 값은 생성되는 시퀀스에 포함 x
- range(1, 5) >> 1, 2, 3, 4

증가/감소 값(step) 규칙
- step이 양수일 때(기본값: 1)
 - 시작 값이 끝 값보다 크면 할당 x 에러는 안남
- step이 음수일 때
 -start 값은 stop보다 반드시 커야 함


---
## dict 딕셔너리

key - value 쌍으로 이루어진 **순서**와 **중복**이 없는 **변경 불가능**한 자료형

비시퀀스 노중복 가변

순서가 없다? >> index가 없음

인덱스는 자료에 순서를 부여

### 딕셔너리 표현
- 중괄호 {} 안에 값들이 , 로 구분
- 값 1개는 키와 값이 쌍으로 이루어짐
- 각 값에는 순서 x


```python
my_dict1 = {}
my_dict2 = {'key' : 'value'}
my_dict3 = {'apple' : 12, 'list' : [1, 2, 3]}

print(my_dict1) # {}

print(my_dict1) # {'key' : 'value'}

print(my_dict1) # {'apple' : 12, 'list' : [1, 2, 3]}
```

- 순서 없는 자료형이지만 파이썬 3.7이상부터는 입력한 순서는 출력 시 그대로 유지
- 순서 없는 자료형, key를 통한 접근

### key의 규칙
- 고유해야함 >> key는 중복될 수 없음
- 변경 불가능한(immutable) 자료형만 사용 가능
  - 가능: str, int, float, tuple
  - 불가능: list, dict
  
### value의 규칙
- 어떤 자료형이든 자유롭게 사용 가능

key 접근 시 대괄호 []사용

```python
my_dict = {'name': '홍길동', 'age': 25}
print(my_dict['name'])  # '홍길동'
print(my_dict['test'])  # KeyError: 'test'
```

딕셔너리 값 추가 및 변경
```python

# 딕셔너리 값 추가 및 변경
my_dict = {'apple': 12, 'list': [1, 2, 3]}
# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['apple'] = 100
print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}
```

## set 세트
순서와 중복이 없는 변경 가능한 자료형

중복이 없어 수학에서의 집합 연산을 수행 가능

```python
# 세트 표현
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1} 중복 허용 x
```
비어있는 딕셔너리와의 혼동을 피하기위해 빈 세트는 반드시 set()로 만들 것

순서가 없음
- 인덱싱(set[0])이나 슬라이싱(set[0:2]) 사용 불가

#### 세트의 집합 연산

```python
# 세트의 집합 연산
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```

---

## None
파이썬에서 '값이 없음'을 표현하는 특별한 데이터 타입

- 내용물 없는 빈 상자 같은 존재지만 비어있는 것은 아님
- 숫자 0이나 빈 문자열('')과는 다름
- **값이 존재하지 않음** 또는 **아직 정해지지 않음** 이라는 상태를 나타내기 위해 사용

```python
# None
my_variable = None
print(my_variable)  # None
```

---

## Boolean
'참(True)'과 '거짓(False)' 단 두 가지 값만 가지는 데이터 타입

```python
# Boolean
is_active = True
is_logged_in = False

print(is_active)  # True
print(is_logged_in)  # False
print(10 > 5)  # True
print(10 == 5)  # False
```

---
## Collection
여러 개의 값을 하나로 묶어 관리하는 자료형들을 통칭하는 말

- str, list, tuple, range, set, dict 데이터 타입이 모두 collection에 분류됨

## 컬렉션 정리

| 컬렉션명 | 변경 가능 여부 | 순서 존재 여부 |
|---|:---:|:---:|
| str | X | O |
| list | O | O |
| tuple | X | O |
| dict | O | X |
| set | O | X |

---



## 불변 vs 가변

* 컬렉션 타입은 생성 후 내용을 변경할 수 있는지 없는지에 따라 '불변'과 '가변' 두 그룹으로 나뉨

| 구분 | 불변 (Immutable) | 가변 (Mutable) |
|---|---|---|
| 특징 | 변경 불가, 안전성, 예측 가능 | 변경 가능, 유연성, 효율성 |
| 종류 | str, tuple, range | list, dict, set |
---

불변 : 값 자체가 메모리에 들어가있음

가변 : 메모리 주소를 저장해둠

---

## 형변환 Type Conversion
한 데이터 타입을 다른 데이터 타입으로 변환하는 과정

- 예를 들어 문자열 "100"을 숫자 100으로 바꾸거나 3.14 를 정수 3으로 바꾸는 등의 데이터 형태를 바꾸는 것
- 형변환은 2가지 있음
    - 암시적 형변환: 파이썬이 자동으로 처리
    - 개발자가 직접 지시


### 암시적 형변환 Implicit Conversion
- 파이썬이 데이터 손실 막기위해 더 정밀한 타입으로 자동 변환해주는 규칙

예시
- 정수와 실수의 연산에서 정수가 실수로 변환됨
- Boolean과 Numeric Type에서만 가능

```python
# 암시적 형변환
# 정수(int)와 실수(float)의 덧셈
print(3 + 5.0)  # 8.0
# 불리언(bool)과 정수(int)의 덧셈
print(True + 3)  # 4
# 불리언간의 덧셈
print(True + False)  # 1
```

### 명시적 형변환 Explicit Conversion
개발자가 변환하고 싶은 타입을 직접 함수로 지정하여 변환하는 것

- 서로 다른 타입의 데이터를 '호환'되도록 맞추는 과정

#### 명시적 형변환 예시

| 함수 | 설명 | 예시 | 결과 |
|---|---|---|---|
| `int()` | 정수로 변환 | `int("123")` | `123` |
| `float()` | 실수로 변환 | `float("3.14")` | `3.14` |
| `str()` | 문자열로 변환 | `str(100)` | `"100"` |
| `list()` | 리스트로 변환 | `list("abc")` | `['a', 'b', 'c']` |
| `tuple()` | 튜플로 변환 | `tuple([1,2])` | `(1, 2)` |
| `set()` | 세트로 변환 | `set([1,2,2])` | `{1, 2}` |
---

str -> int
- 형식에 맞는 숫자만 가능

int -> str
- 모두 가능

```python
# str -> int
print(int('1'))  # 1
# ValueError: invalid literal for int() with base 10: '3.5'
# print(int('3.5'))
print(int(3.5))  # 3
print(float('3.5'))  # 3.5

# int -> str
print(str(1) + '등')  # 1등
```

---

## 컬렉션 간 형변환 정리

| | str | list | tuple | range | set | dict |
|---|---|:---:|:---:|:---:|:---:|:---:|
| str | | O | O | X | O | X |
| list | O | | O | X | O | X |
| tuple | O | O | | X | O | X |
| range | O | O | O | | O | X |
| set | O | O | O | X | | X |
| dict | O | O(key만) | O(key만) | X | O(key만) | |

---


## 산술 연산자

* 수학적 계산을 위해 사용되는 연산자

| 기호 | 연산자 |
|---|---|
| `-` | 음수 부호 |
| `+` | 덧셈 |
| `-` | 뺄셈 |
| `*` | 곱셈 |
| `/` | 나눗셈 |
| `//` | 정수 나눗셈 (몫) |
| `%` | 나머지 |
| `**` | 지수 (거듭제곱) |

----


## 복합 연산자

* 연산과 할당이 함께 이뤄짐

| 기호 | 예시 | 의미 |
|---|---|---|
| `+=` | `a += b` | `a = a + b` |
| `-=` | `a -= b` | `a = a - b` |
| `*=` | `a *= b` | `a = a * b` |
| `/=` | `a /= b` | `a = a / b` |
| `//=` | `a //= b` | `a = a // b` |
| `%=` | `a %= b` | `a = a % b` |
| `**=` | `a **= b` | `a = a ** b` |

```python
# 복합 연산자 예시
y = 10
y -= 4
# y = y - 4
print(y)  # 6

z = 7
z *= 2
print(z)  # 14

w = 15
w /= 4
print(w)  # 3.75

q = 20
q //= 3
print(q)  # 6
```

---

## 비교 연산자

* 두 값을 비교하여 그 관계가 맞는지 틀리는지를 True 또는 False로 반환

| 기호 | 내용 |
|---|---|
| `<` | 미만 |
| `<=` | 이하 |
| `>` | 초과 |
| `>=` | 이상 |
| `==` | 같음 |
| `!=` | 같지 않음 |
| `is` | 같음 |
| `is not` | 같지 않음 |

```python
# 비교 연산자 예시 
print(3 > 6)  # False
print(3 < 6)  # True
print(3 >= 3)  # True
print(3 <= 6)  # True
```

---

## `==` 연산자

  * **값(데이터)이 같은지**를 비교
  * **동등성(equality)**
  * 예를 들어, `1 == True`의 경우 파이썬이 내부적으로 `True`를 `1`로 간주할 수 있으므로 `True` 결과가 나옴

<!-- end list -->

```python
print(2 == 2.0) # True
print(2 != 2) # False
print('HI' == 'hi') # False
print(1 == True) # True
```

-----

## `is` 연산자

  * **객체 자체**가 같은지를 비교
  * **식별성(identity)**
  * 두 변수가 완전히 동일한 객체를 가리키는지, 즉 **메모리 주소가 같은지** 확인할 때 사용

<!-- end list -->

```python
# SyntaxWarning: "is" with a literal.
# Did you mean "=="?

print(1 is True) # False
print(2 is 2.0) # False
```

`is`는 메모리 주소를 비교하는데, 값 자체를 비교하는 `==`를 써야 할 곳에 실수로 사용한 것 같다고 파이썬이 알려주는 경고

## `is` 대신 `==`를 사용해야 하는 이유

* **결론**: `is`는 **'정체성'**을, `==`는 **'가치'**를 비교하기 때문
* 두 연산자는 "같다"를 확인하는 목적이 근본적으로 다름

---

* **`is` (Identity Operator):**
    * 두 변수가 **완전히 동일한 메모리 주소의 객체를 가리키는지**, 즉 **'정체성(identity)'**이 같은지를 확인
---

* **`==` (Equality Operator):**
    * 두 변수가 가리키는 객체의 **내용**, 즉 **'값(value)'**이 같은지를 확인


----

## `is`를 값 비교에 사용하면 안 되는 이유 - "의도와 다른 결과를 낳습니다."

  * 아래 코드에서 `is`는 "두 객체가 메모리상에서 같은 존재인가?"를 묻기 때문에 `False`가 출력됩니다.
  * 하지만 우리가 정말 궁금한 것은 "**두 객체의 값이 논리적으로 같은가?**"이므로 `==`를 사용해야 의도에 맞는 `True`를 얻을 수 있습니다.

<!-- end list -->

```python
# 1(정수)과 True(불리언)는 다른 객체이다.
print(1 is True)  # False

# 1과 True의 '값'은 논리적으로 같다.
print(1 == True)  # True
```

```python
# 2(정수)와 2.0(실수)는 다른 객체이다.
print(2 is 2.0)  # False

# 2와 2.0의 '값'은 논리적으로 같다.
print(2 == 2.0) # True
```

## `is` 연산자는 언제 사용하는가?

* 주로 **싱글턴(Singleton) 객체**를 비교할 때 사용합니다.

---

## 싱글턴(Singleton) 객체란?

* 특정 값에 대해 파이썬 전체에서 **단 하나의 객체만 생성되어 재사용되는 특별한 객체**입니다.
* 여러 변수가 이 값을 가지더라도, 모두 **미리 만들어진 하나의 객체**를 함께 가리키게 되므로 항상 같은 메모리 주소를 가집니다.
* 파이썬의 대표적인 싱글턴 객체: `None`, `True`, `False`
----


## 싱글턴 객체를 비교할 때

  * **`is` 연산자**는 두 변수가 완전히 **동일한 객체를 가리키는지**, 즉 **메모리 주소가 같은지**를 확인할 때 사용합니다.
  * 파이썬 전체에서 **단 하나의 객체만 생성되어 재사용되는 싱글턴 객체** 비교에 적합합니다.

-----

### 싱글턴(Singleton) 객체

프로그램 전체에서 오직 1개만 존재하도록 만들어진 특별한 객체 (`None`, `True`, `False`)

-----

```python
x = None

# 권장
if x is None:
    print('x는 None입니다.')

# 비권장
if x == None:
    print('x는 None입니다.')
```

```python
x = True
y = True

print(x is y) # True
print(True is True) # True
print(False is False) # True
print(None is None) # True
```
---

## 추가 예시: 리스트나 객체 비교 시 주의사항

  * 리스트 또는 다른 \*\*가변 객체(mutable)\*\*를 비교할 때, **값 자체**가 같은지 확인하려면 `==`를 사용합니다.
  * 두 변수가 **완전히 동일한 객체를 가리키는지**를 확인해야 한다면 `is`를 사용합니다.

<!-- end list -->

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True (두 리스트의 값은 동일)
print(a is b) # False (서로 다른 리스트 객체)

# b가 a를 그대로 참조하도록 할 경우
b = a
print(a is b) # True (같은 객체를 가리키므로 True)
```
---

## `==`와 `is` 정리

* **값 비교에는 `==`를 사용**하고, **객체(레퍼런스) 비교에는 `is`를 사용하는 것이 원칙**입니다.
* 숫자나 문자열, 불리언 값 등 **동등성(값)을 판단해야 할 때 `is`를 쓰면 의도치 않은 결과(False)가 나올 수 있습니다.** 이는 파이썬 내부적인 최적화나 타입 차이로 인해 일관성이 깨질 수 있기 때문입니다.
* `is`는 주로 **싱글턴 객체**에 대한 비교 시 사용합니다.

---


## 논리 연산자

* 여러 개의 조건을 조합하거나, `True`/`False` 값을 반대로 뒤집을 때 사용합니다 (`and`, `or`, `not`이 대표적).

| 기호 | 연산자 | 내용 |
|---|---|---|
| `and` | 논리곱 | 두 피연산자 모두 `True`인 경우에만 전체 표현식을 `True`로 평가 |
| `or` | 논리합 | 두 피연산자 중 하나라도 `True`인 경우 전체 표현식을 `True`로 평가 |
| `not` | 논리부정 | 단일 피연산자를 부정 |

---

## 논리 연산자 활용

```python
print(True and False) # False
print(True or False)  # True
print(not True)       # False
print(not 0)          # True
```

-----

## 비교 연산자와 함께 사용 가능

```python
num = 15
result = (num > 10) and (num % 2 == 0)
print(result) # False

name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result) # True
```

## 단축 평가

논리 연산에서 **두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작**

컴퓨터는 생각보다 '게으른' 구석이 있습니다. 똑똑한 게으름이죠!

꼭 필요한 계산만 하고, 결과가 이미 정해졌다면 굳이 뒤에 있는 코드까지 확인하지 않습니다. 이렇게 결과가 확정되는 순간 평가를 '단축'하고 넘어간다고 해서 '**단축 평가**'라고 부릅니다.

---

## 파이썬의 '참(True)'과 '거짓(False)'에 대한 새로운 시각

* 단축 평가를 이해하려면, 파이썬이 어떤 값을 '참'으로 보고 어떤 값을 '거짓'으로 보는지 알아야 합니다.

---

### 거짓으로 취급되는 값들

* `False`, 숫자 `0`, 빈 문자열 `""`, 빈 리스트 `[]`, `None` 등 **'비어있거나 없다'는 느낌의 값들**

---

### 참으로 취급되는 값들

* `True` 그리고 **'거짓'이 아닌 모든 값**
* `1`, `-10`, `"hello"`, `[1, 2]` 등 **내용이 있는 값**

---

## 단축 평가 동작 정리

### `and` 연산자

* 하나라도 '거짓'이면 바로 '거짓'
* `and`는 연산을 왼쪽에서 오른쪽으로 진행하다가, **처음 만나는 '거짓' 값을 바로 반환**
* 만약 끝까지 갔는데 모든 값이 '참'이면, **맨 마지막 '참' 값을 반환**

### `or` 연산자

* 하나라도 '참'이면 바로 '참'
* `or`는 연산을 왼쪽에서 오른쪽으로 진행하다가, **처음 만나는 '참' 값을 바로 반환**
* 만약 끝까지 갔는데 모든 값이 '거짓'이면, **맨 마지막 '거짓' 값을 반환**

---
## 단축 평가 `and` 연산자 예시 문제

```python
item1 = '지도'
item2 = '나침반'

# and는 item1('지도')를 보고 통과
# -> item2('나침반')를 보고 통과
# -> 맨 마지막 값인 '나침반'을 최종 결과로 선택
result = item1 and item2

print(f'최종적으로 챙긴 물건: {result}')
# >> 최종적으로 챙긴 물건: 나침반
```

-----

```python
item1 = '지도'
item2 = ''

# and는 item1('지도')를 보고 통과
# -> item2('')를 봄
# -> item2가 '내용 없는 값'이므로, 여기서 멈추고 ''를 최종 결과로 선택!
result = item1 and item2

print(f'최종적으로 챙긴 물건: {result}')
# >> 최종적으로 챙긴 물건:
```

-----

```python
item1 = ''
item2 = '나침반'

# and는 item1('')을 보자마자 '탈락!'을 외치며 평가를 멈춤
# -> 그 자리에서 바로 ''를 최종 결과로 선택!
# (item2는 쳐다보지도 않음)
result = item1 and item2

print(f'최종적으로 챙긴 물건: {result}')
# >> 최종적으로 챙긴 물건:
```
---
## 멤버십 연산자

* 특정 값이 시퀀스나 다른 컬렉션 안에 포함되어 있는지 확인하는 연산자입니다.

| 기호 | 내용 |
|---|---|
| **`in`** | 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인 |
| **`not in`** | 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인 |

---

## 멤버십 연산자 예시

  * 특정 값이 시퀀스나 다른 컬렉션 안에 포함되어 있는지 확인하는 연산자입니다.

<!-- end list -->

```python
word = 'hello'
numbers = [1, 2, 3, 4, 5]

print('h' in word)        # True
print('z' in word)        # False
print(4 not in numbers)   # False
print(6 not in numbers)   # True
```

---

## 시퀀스형 연산자

* **시퀀스 자료형(문자열, 리스트, 튜플)에 특별한 의미로 사용되는 연산자**입니다.
* `+`는 시퀀스를 연결하는 기능을, `*`는 시퀀스를 반복하는 기능을 합니다.

| 연산자 | 내용 |
|---|---|
| `+` | 결합 연산자 |
| `*` | 반복 연산자 |

---

## 시퀀스형 연산자 예시

  * 특정 값이 시퀀스나 다른 컬렉션 안에 포함되어 있는지 확인하는 연산자

<!-- end list -->

```python
# Gildong Hong
print('Gildong' + ' Hong')
# hihihihihi
print('hi' * 5)

# [1, 2, 'a', 'b']
print([1, 2] + ['a', 'b'])
# [1, 2, 1, 2]
print([1, 2] * 2)
```

---

## 연산자 우선순위 정리

| 우선순위 | 연산자 | 내용 |
|---|---|---|
| 높음 | `()` | 소괄호 grouping |
| | `[]` | 인덱싱, 슬라이싱 |
| | `**` | 거듭제곱 |
| | `+, -` | 단항 연산자 양수/음수 |
| | `*, /, //, %` | 산술 연산자 |
| | `+, -` | 산술 연산자 |
| | `<`, `<=`, `>`, `>=`, `==`, `!=` | 비교 연산자 |
| | `is`, `is not` | 객체 비교 |
| | `in`, `not in` | 멤버십 연산자 |
| | `not` | 논리 부정 |
| | `and` | 논리 AND |
| 낮음 | `or` | 논리 OR |

---

## Trailing Comma (후행 쉼표)

Trailing Comma는 **컬렉션의 마지막 요소 뒤에 붙는 쉼표**를 의미합니다.

-----

  * 일반적으로 Trailing Comma 작성은 '선택사항'입니다.
  * 단, **하나의 요소로 구성된 튜플을 만들 때는 필수**입니다.

<!-- end list -->

```python
x = 1 # 정수
x = (1) # 정수

x = 1,  # 튜플
x = (1,) # 튜플
```

---

## Trailing Comma 기본 규칙

  * 각 요소를 별도의 줄에 작성
  * 마지막 요소 뒤에 trailing comma 추가
  * 닫는 괄호는 새로운 줄에 배치

<!-- end list -->

```python
items = [
    'item1',
    'item2',
    'item3',
]

config = {
    'host': 'localhost',
    'port': 8080,
    'debug': True,
}
```
---

Here's the extracted text from the image, organized for Notion:

## Trailing Comma 좋은 예시

```python
# Good
items = [
    'item1',
    'item2',
]
my_func(
    'value1',
    'value2',
)
```

-----

## Trailing Comma 나쁜 예시

```python
# Bad
items = ['item1', 'item2',]
my_func('value1', 'value2',)
```

```python
# 한 줄 작성 시에는 불필요
items = ['item1', 'item2']
my_func('value1', 'value2')
```
---
## Trailing Comma 장점

1.  **가독성 향상**
    * 각 줄이 동일한 패턴을 가짐
    * 코드 리뷰가 용이함
2.  **유지보수 용이성**
    * 항목 추가/제거가 간단함
    * 실수로 인한 구문 오류 방지

----



