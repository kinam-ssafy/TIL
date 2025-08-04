# 목차

---

## 모듈
- 모듈 활용
- 사용자 정의 모듈

---

## 파이썬 표준 라이브러리
- 패키지

---

## 제어문

---

## 조건문
- if statement

## 반복문
- for statement
- while statement
- 반복 제어
- 유용한 내장 함수 map & zip

---

## 참고
- 모듈 내부 살펴보기
- for-else
- enumerate

## 학습 목표

* ✓ 모듈의 개념을 이해하고, 모듈을 활용하여 코드를 효율적으로 구성할 수 있습니다.
* ✓ 사용자 정의 모듈을 생성하고 활용할 수 있습니다.
* ✓ 파이썬 표준 라이브러리의 개념과 패키지의 중요성을 이해합니다.
* ✓ 제어문의 필요성을 이해하고, 조건문(if)을 활용하여 코드의 실행 흐름을 제어할 수 있습니다.
* ✓ 반복문을 사용하여 특정 작업을 반복적으로 수행하도록 코드를 작성할 수 있습니다.
* ✓ 반복 제어문(break, continue)을 활용하여 반복문의 동작을 제어할 수 있습니다.
* ✓ map()과 zip() 내장 함수의 활용법을 이해하고 코드에 적용할 수 있습니다.

------------------------------------------------------------

## 모듈(Module)

> **한 파일로 묶인 변수와 함수의 모음**   
> 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

## 모듈 예시

  * `math` 내장 모듈
      * 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈

<!-- end list -->

```python
import math

print(math.pi) # 3.141592653589793
print(math.sqrt(4)) # 2.0
```
---

## 모듈 활용 

## Import 문 사용

  * 같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수 있음
  * ‘.’(dot) 연산자
      * “점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라” 라는 의미
    <!-- end list -->
    ```python
    import math

    print(math.pi)      # 모듈명.변수명
    print(math.sqrt(4)) # 모듈명.함수명
    ```

-----

  * **단점**
      * 자칫 코드가 길어질 수 있음

## from 절 사용

  * 코드가 짧고 간결해짐
    ```python
    from math import pi, sqrt

    print(pi)      # 변수명
    print(sqrt(4)) # 함수명
    ```

-----

  * **단점**
      * 정의된 모듈의 위치를 알기 어려워 명시적이지 않을 수 있음
      * 사용자가 선언한 변수 또는 함수와 겹치게 되어 모듈에서 정의한 값이나 동작이 이루어 지지 않을 수 있음
    <!-- end list -->
    ```python
    from math import sqrt
    math_result = sqrt(16) # 실수형 4.0

    def sqrt(x):           # 사용자가 정의한 sqrt 함수
        return str(x ** 0.5)
    my_result = sqrt(16)   # 문자열 4.0
    ```

-----

## from 절 사용시 주의사항

  * 서로 다른 모듈에서 `import`된 변수나 함수의 이름이 같은 경우 이름 충돌 발생
      * 마지막에 `import` 된 것이 이전 것을 덮어쓰기 때문에, 나중에 `import`된 것만 유효함
    <!-- end list -->
    ```python
    from math import sqrt      # math.sqrt가 먼저 import됨
    from my_math import sqrt   # my_math.sqrt가 math.sqrt를 덮어씀

    result = sqrt(9)           # math.sqrt가 아닌 my_math.sqrt가 사용됨
    ```

-----

  * 모든 요소를 한 번에 `import` 하는 `*` 표기는 권장하지 않음
    ```python
    from math import *
    from my_math import sqrt, tangent # 어느 함수가 math 모듈과 중복되는지 모름

    # 아래는 사용자가 임의로 정의한 변수들
    a = 100
    c = 200
    e = 300                       # math 모듈의 자연상수 e를 사용할 수 없게 됨
    ```
    -----

    ## 'as' 키워드

  * `'as'` 키워드를 사용하여 별칭(alias)을 부여
      * 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결
    <!-- end list -->
    ```python
    from math import sqrt
    from my_math import sqrt as my_sqrt

    sqrt(4)
    my_sqrt(4)
    ```

-----

  * `import` 되는 함수나 변수명이 너무 길거나 자주 사용해야 할 경우 ‘as’ 키워드로 별칭을 정의해 쉽게 사용
    ```python
    import pandas as pd
    import matplotlib.pyplot as plt

    # 별칭을 부여하지 않으면 길고 불편
    # df = pandas.DataFrame()
    # matplotlib.pyplot.plot(x, y)

    # 짧고 편리
    df = pd.DataFrame()
    plt.plot(x, y)
    ```

---------------------------------
# 사용자 정의 모듈  
----------------------------------
## 직접 정의한 모듈 사용하기

  * `my_math.py` 생성하여 두 수의 합을 구하는 `add` 함수를 작성

    ```python
    # my_math.py
    def add(x, y):
        return x + y
    ```

-----

  * 같은 위치에 `sample.py` 파일을 생성하고 `my_math` 모듈의 `add` 함수 `import` 후 `add` 함수 호출

    ```python
    # sample.py
    import my_math

    print(my_math.add(10, 20)) # 30
    ```
-----------------------------------
## 파이썬 표준 라이브러리  
-----------------------------------
Python Standard Library  
파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

[PSL](https://docs.python.org/ko/3/library/index.html)

------------------------------------
## 패키지 (Package)

> 연관된 **모듈**들을 하나의 디렉토리에 **모아 놓은 것**

## 직접 패키지 만들어 보기

  * 다음과 같은 구조로 폴더와 파일을 생성
  * `sample.py` 파일을 생성
  * `my_package` 폴더를 생성
      * `my_package` 폴더 내부에 `math` 폴더와 `statistics` 폴더 생성
      * `my_package/math` 폴더 내부에 `my_math.py` 파일 생성 후 다음 코드 작성
        ```python
        # my_package/math/my_math.py
        def add(x, y):
            return x + y
        ```
      * `my_package / statistics` 폴더 내부에 `tools.py` 파일 생성 후 다음 코드 작성
        ```python
        # my_package/statistics/tools.py
        def mod(x, y):
            return x % y
        ```
## 직접 만든 패키지 사용하기

  * `sample.py` 에 다음 코드를 작성해서 실행 결과 확인

-----

```python
# sample.py

from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1, 2))  # 출력: 3
print(tools.mod(1, 2))    # 출력: 1
```

## 패키지의 종류

  * **PSL (Python Standard Library) 내부 패키지**

      * 파이썬을 설치하면 자동으로 사용할 수 있는 기본 패키지
      * 다양한 기능이 들어 있어 복잡한 작업도 쉽게 처리할 수 있음
      * `'math'`, `'os'`, `'sys'`, `'random'` 등 다양한 패키지가 존재
      * 설치 없이 바로 `import` 해서 사용 가능

  * **파이썬 외부 패키지**

      * 필요한 기능을 사용하기 위해 직접 설치해서 쓰는 패키지
      * 다양한 패키지들이 존재
          * 예시) 엑셀 파일 불러오고 조작 / 데이터를 분석하고 시각화 / 웹 데이터를 가져오기 등
      * 사용할 패키지를 설치할 때는 `'pip'`를 사용

-----

> **💡 라이브러리 (Library)**
>
> 다양한 패키지들을 포함하는
> 상위 개념
> **라이브러리 \> 패키지 \> 모듈**

## pip

---

외부 패키지들을 설치하도록 도와주는  
파이썬의 패키지 관리 시스템

## 패키지 설치

  * 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음


```shell
$pip install SomePackage
$pip install SomePackage==1.0.5
$pip install SomePackage>=1.0.4
```
## requests 외부 패키지 설치 및 사용 예시

  * **requests 패키지**
      * 파이썬에서 웹에 요청을 보내고 응답을 받는 걸 아주 쉽게 만들어주는 외부 패키지 >> 백엔드, API 다루면 필수
  * **`pip`를 통해 `requests` 패키지를 설치**
    ```shell
    $ pip install requests
    ```
  * **`requests`를 import 하여 웹에 데이터 요청**
    ```python
    import requests

    # 공휴일 정보 API
    url = "https://date.nager.at/api/v3/publicholidays/2025/KR"
    response = requests.get(url).json()
    print(response)
    ```

-----

> **💡 .get(url)**
>
> 주어진 url로 요청하는 `requests` 패키지 메서드


-----

> **💡 .json()**
>
> 문자열로 이루어진 json 자료형을 dict 자료형으로 변환시키는 `requests` 패키지 메서드


-----

> ✳️ **메서드는 OOP에서 진행**

# 패키지 사용 목적

---

모듈들의 이름공간을 구분하여 충돌을 방지  
모듈들을 효율적으로 관리하고 할 수 있도록 돕는 역할


# 제어문 (Control Statement)

---

코드의 실행 흐름을 제어하는 데 사용되는 구문  
**조건**에 따라 코드 블록을 실행하거나 **반복적**으로 코드를 실행

# 조건문 (Conditional Statement)

---

주어진 조건식을 평가하여 해당 조건이 참(`True`)인 경우에만  
코드 블록을 실행하거나 건너뜀

### `if` / `elif` / `else`

---

파이썬 조건문에 사용되는 키워드

## `for` 반복문

-----

반복 가능한(iterable) 객체의 요소들을 반복하는데 사용  
반복 가능한 객체의 요소 개수 만큼 반복이 수행됨

```python
for 변수 in 반복 가능한 객체:
    코드 블록
```


# 반복 가능한 객체 (iterable)

-----

요소를 하나씩 반환할 수 있는 모든 객체  
(반복문에서 순회할 수 있는 객체)

-----

✳️ 시퀀스 자료형 (`list`, `tuple`, `str`) 뿐만 아니라 비 시퀀스 자료형 (`dict`, `set`) 등도 반복 가능한 객체  


## for문 작동 원리

  * 리스트 내 첫 항목이 반복 변수(`item`)에 할당되고 코드블록이 실행
  * 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행
  * ... 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행
  * 더 이상 반복 변수에 할당할 값이 없으면 반복 종료

-----

```python
item_list = ['apple', 'banana', 'coconut']

for item in item_list: # item: 반복 변수 for 단수형 in 복수형 권장
    print(item)

# 출력
"""
apple
banana
coconut
"""
```

## 문자열 순회

  * 문자열은 문자로 구성된 시퀀스 자료형
  * 문자열 반복시 문자가 반복 변수에 할당되어 반복 수행

-----

```python
country = 'Korea'

for char in country:
    print(char)

# 출력
"""
K
o
r
e
a
"""
```

## `range` 순회

  * 특정 숫자 범위만큼 반복을 하고 싶을 때 `range` 함수를 사용

-----

```python
for i in range(5):
    print(i)

# 출력
"""
0
1
2
3
4
"""
```

## 딕셔너리 순회

  * `dict` 자료형은 비시퀀스 자료형으로 반복 순서가 보장되지 않음을 유의

-----

```python
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])
```

-----

```
# 출력
"""
x
10
y
20
z
30
"""
```
## 인덱스로 리스트 순회

  * 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
  * 인덱스를 사용하면 리스트의 원하는 위치에 있는 값을 읽거나 변경할 수 있음

-----

```python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers) # [8, 12, 20, -16, 10]
```

-----

## 중첩 리스트 순회

  * 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회

-----

### 1\. 바깥 리스트 순회

```python
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)

# 출력
"""
['A', 'B']
['c', 'd']
"""
```

### 2\. 안쪽 리스트까지 순회 (중첩 반복)

```python
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    for item in elem:
        print(item)

# 출력
"""
A
B
c
d
"""
```

## 반복 제어

---

`for`문과 `while`은 매 반복마다 본문 내 모든 코드를 실행하지만  
때때로 일부만 실행하는 것이 필요할 때가 있음

## 반복 제어 키워드

### `break` 키워드

  * 해당 키워드를 만나게 되면 남은 코드를 무시하고 반복 즉시 종료
  * 반복을 끝내야 할 명확한 조건이 있을 때 사용

<!-- end list -->

```python
for i in range(10):
    if i == 5:
        break
    print(i, end=' ') # 0 1 2 3 4
```

-----

### `continue` 키워드

  * 해당 키워드를 만나게 되면 다음 코드는 무시하고 다음 반복을 수행

<!-- end list -->

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=' ') # 1 3 5 7 9
```

## `continue` 예시

  * 리스트에서 홀수만 출력하기

-----

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# 출력
"""
1
3
5
7
9
"""
```

## 빈 코드 블록 키워드

  * **`pass` 키워드**
      * '아무 동작도 하지 않음'을 명시적으로 나타내는 키워드
      * 반복 제어가 아닌 코드의 틀을 유지하거나 나중에 내용을 채우기 위한 용도로 사용
      * 코드를 비워두면 오류가 발생하기 때문에 `pass` 키워드를 사용함
      * 반복문 뿐만 아니라 함수, 조건문에서도 사용 가능

-----

### `pass` 사용 예시

```python
# while문 예시
while True:
    if condition1:
        break
    elif condition2:
        pass # 빈 코드를 의미
    else:
        print('출력')
```

```python
# if문 예시
if condition:
    pass # 아무런 동작도 수행하지 않음
else:
    pass # 구조를 잡을 뿐
```

```python
# 함수 정의 예시
def my_function():
    pass # 없으면 오류 발생
```

-----

## map 함수

### map(function, iterable)

반복 가능한 데이터구조(iterable)의 모든 요소에 function을 적용하고, 그 결과 값들을 map object로 묶어서 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)       # <map object at 0x00000239C915D760>
print(list(result)) # ['1', '2', '3']
```

-----

> **💡 map object**
>
> 결과를 하나씩 꺼내 쓸 수 있는  
> 반복 가능한 객체 자료형.  
> 전체 값을 확인하려면 `list`나  
> `tuple`로 형변환을 해줘야 함

## `map` 함수 활용

  * SWEA 문제의 `input` 처럼 문자열 ‘1 2 3’이 입력 되었을 때 활용 예시

<!-- end list -->

```python
# '1 2 3'을 입력했을 경우

numbers1 = input().split()
print(numbers1) # ['1', '2', '3']

numbers2 = list(map(int, input().split()))
print(numbers2) # [1, 2, 3]
```

-----

> **💡 split 메서드**
>
> 문자열을 지정한 기준  
> 문자(기본은 공백)를 기준으로  
> 잘라서, 잘린 문자들을 리스트로  
> 반환해주는 문자열 메서드
>


-----

> **TIP**
>
>   * 입력이 ‘1 2 3’과 같이 공백으로 구분되어 있는지, ‘123’처럼 연속된 문자형태인지 확인
>   * 만약 문자열이 공백으로 구분된다면 문자열의 `split()` 메서드를 통해 분리해서 `map` 함수에 넣어야 함
>   * 만약 ‘123’과 같이 연속된 문자 형태이면 `split()` 하지 않고 문자열 그대로 `map` 함수에 넣어야 함  

## `zip(*iterables)`

-----

`zip` 함수는 여러 개의 반복 가능한 데이터 구조를 묶어서,  
같은 위치에 있는 값들을 하나의 `tuple`로 만든 뒤  
그것들을 모아 `zip object`로 반환하는 함수

-----

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)      # <zip object at 0x000001C76DE58700>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]
```

> **`zip object`**
>
> 짝지어진 결과(`tuple`)를 하나씩  
> 꺼내 쓸 수 있는 반복 가능한 객체  
> 자료형  
> 전체 값을 확인하려면 `list`나  
> `tuple`로 형변환을 해줘야 함

## `zip` 함수 활용

  * 여러 개의 리스트를 동시에 조회할 때

<!-- end list -->

```python
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

# 출력
"""
(10, 20, 40) # 0번 인덱스 값
(20, 40, 20) # 1번 인덱스 값
(30, 50, 30) # 2번 인덱스 값
(50, 70, 50) # 3번 인덱스 값
"""
```

-----

> **TIP**
>
>   * 반복 가능한 자료형의 길이가 다른 경우 가장 짧은 길이를 기준으로 묶어서 반환해요.
>   * 반드시 반복 가능한 자료형만 인자로 넣을 수 있어요.
>   * `zip object`는 언패킹을 활용하여 변수에 바로 `tuple` 요소를 할당할 수 있어요.

## `zip` 함수 활용

  * 2차원 리스트의 같은 컬럼(열) 요소를 동시에 조회할 때
  * 실행 결과가 전치 행렬과 동일함

<!-- end list -->

```python
scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]

for score in zip(*scores):
    print(score)

# 출력
"""
(10, 40, 20)
(20, 50, 40)
(30, 39, 50)
"""
```

-----

> **💡 전치 행렬 (Transpose Matrix)**
>
> (i, j)의 값을 (j, i) 위치로 옮긴  
> 행렬  
> 즉, 행을 열로, 열을 행으로  
> 뒤집은 행렬

## 모듈 내부 살펴보기

  * 내장 함수 `help`를 사용해 모듈에 무엇이 들어있는지 확인 가능

-----

```python
help(math)
```

-----

## enumerate 함수

### `enumerate(iterable, start=0)`

iterable 객체의 각 요소에 대해 **인덱스와 값을 함께** 반환하는 내장함수

-----

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# 출력
"""
0 apple
1 banana
2 cherry
"""
```

## `enumerate` 함수 활용

  * `enumerate`의 `index` 정보를 이용해 넘버링으로 사용

      * `start` 에 시작 값을 설정할 수 있음

    <!-- end list -->

    ```python
    movies = ['인터스텔라', '기생충', '인사이드 아웃', '라라랜드']

    for idx, title in enumerate(movies, start=1):
        print(f"{idx}위: {title}")

    # 출력
    """
    1위: 인터스텔라
    2위: 기생충
    3위: 인사이드 아웃
    4위: 라라랜드
    """
    ```

-----

  * 인덱스 정보를 이용해 요소의 위치를 확인할 수 있음

    ```python
    respondents = ['은지', '정우', '소민', '태호']
    answers = ['', '좋아요', '', '괜찮아요']

    for i, response in enumerate(answers):
        if response == '':
            print(f"{respondents[i]} 미제출")

    # 출력
    """
    은지 미제출
    소민 미제출
    """
    ```
    