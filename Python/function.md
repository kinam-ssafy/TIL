# 함수 Funtion

# 목차

## 함수
- 함수 구조
- 함수와 반환 값

## 매개변수와 인자
- 다양한 인자 종류

## 재귀 함수

## 내장 함수

## 함수와 Scope
- global 키워드

## 함수 스타일 가이드
- 함수 이름 작성 규칙
- 단일 책임 원칙

## Packing & UnPacking
- Packing
- Unpacking

## 참고
- 함수와 반환
- 람다 표현식

# 학습 목표

- ✓ 함수의 기본 구조를 이해하고, 직접 함수를 정의할 수 있다.
- ✓ 다양한 인자 전달 방식을 목적에 맞게 활용할 수 있다.
- ✓ 재귀 함수의 개념과 동작 원리를 이해하고, 간단한 문제를 재귀적으로 해결할 수 있다.
- ✓ 다양한 내장 함수(len, max, sun)을 활용할 수 있다.
- ✓ 지역/전역 변수의 개념과 변수의 유효 범위(Scope)를 설명할 수 있다.
- ✓ 함수 이름 규칙과 단일 책임 원칙을 준수하여 가독성 좋은 함수를 작성할 수 있다.
- ✓ 패킹/언패킹을 통해 가변 인자를 다룰 수 있다.

----

# 함수 (Function)

> 특정 작업을 수행하기 위한 **재사용 가능한 코드 묶음**

## 함수를 사용하는 이유

  - 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
  - **재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상

-----

### **코드 비교**


**\# 두 수의 합을 구하는 코드**

```python
# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3
sum_result = num1 + num2

print(sum_result)
```

**\# 두 수의 합을 구하는 함수**

```python
# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2

# 함수를 호출하여 결과 출력
num1 = 5
num2 = 3
sum_result = get_sum(num1, num2)
print(sum_result)
```

### 함수 호출 (function call)

함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것

## `print()` 함수는 반환 값이 없음

* `print()` 함수는 화면에 값을 출력하기만 할 뿐, 반환(return)값이 없음
* 파이썬에서 반환 값이 없는 함수는 기본적으로 `None`을 반환한다고 간주되기 때문

## 매개변수 (parameter)

* 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

---

## 인자 (argument)

* 함수를 호출할 때, 실제로 전달되는 값

## 다양한 인자 종류

1.  위치 인자
2.  기본 인자 값
3.  키워드 인자
4.  임의의 인자 목록
5.  임의의 키워드 인자 목록

## 1\. Positional Arguments (위치 인자)

  * 함수 호출 시 인자의 위치에 따라 전달되는 인자
  * 위치 인자는 함수 호출 시 반드시 값을 전달해야 함

-----

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

# 올바른 위치로 인자 전달
greet('Alice', 25)
# 출력: 안녕하세요, Alice님! 25살이시군요.

# 잘못된 위치로 인자 전달
greet(25, 'Alice')
# 출력: 안녕하세요, 25님! Alice살이시군요.

# 필수 인자를 누락하여 에러 발생
greet('Alice')
# TypeError: greet() missing 1 required positional argument: 'age'
```

## 2\. Default Argument Values (기본 인자 값)

  * 함수 정의에서 매개변수에 **기본 값을 할당**하는 것
  * 함수 호출 시 인자를 전달하지 않으면, **기본값이 매개변수에 할당됨**

-----

```python
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

# age 인자를 전달하지 않으면 기본값 30이 사용됨
greet('Bob') 
# 출력: 안녕하세요, Bob님! 30살이시군요.

# age 인자를 전달하면 기본값을 덮어씀
greet('Charlie', 40) 
# 출력: 안녕하세요, Charlie님! 40살이시군요.
```

## 3\. Keyword Arguments(키워드 인자)

  * 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
  * 매개변수와 인자의 순서를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
  * 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
  * **단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**

-----

```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

# 키워드를 사용하면 순서와 관계없이 인자를 전달할 수 있습니다.
greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.

# 키워드 인자(age=35) 뒤에 위치 인자('Dave')를 사용하면 문법 오류가 발생합니다.
greet(age=35, 'Dave')      
# SyntaxError: positional argument follows keyword argument
```

## 4\. Arbitrary Argument Lists (임의의 인자 목록)

  * 정해지지 않은 개수의 인자를 처리하는 인자
  * 함수 정의 시 매개변수 앞에 `*`를 붙여 사용
  * 여러 개의 인자를 `tuple`로 처리
  * tuple >> 시퀀스, 변경불가 특성으로 내부동작에 사용
    
-----

```python
def calculate_sum(*args):
    print(args)      # (1, 100, 5000, 30)
    print(type(args))  # <class 'tuple'>

calculate_sum(1, 100, 5000, 30)
```

## 5\. Arbitrary Keyword Argument Lists(임의의 키워드 인자 목록)

  * 정해지지 않은 개수의 키워드 인자를 처리하는 인자
  * 함수 정의 시 매개변수 앞에 `**`를 붙여 사용
  * 여러 개의 인자를 `dictionary`로 묶어 처리

-----

```python
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30}
```

## 함수 인자 권장 작성 순서

  * 위치 → 기본 → 가변 → 가변 키워드
  * 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
  * **단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조절될 수 있음**

-----

```python
# 위치, 기본, 가변, 가변 키워드 순서로 정의된 함수
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    ...
```
## 인자의 모든 종류를 적용한 예시

### 함수 정의 및 호출

```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)

# 함수 호출
func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
```

### 실행 결과

```text
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
```
4 5 6은 tuple로 묶임

kwargs는 dict로 묶임

default_arg = 'default' >> 'default'라고 꼭 문자열을 넣으라는 법은 없음


# 재귀 함수

---

> 함수 내부에서 자기 자신을 호출하는 함수

## 재귀 함수 예시 - 팩토리얼 (2/4)

  * factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
  * 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
  * 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출

-----

종료 조건 명확히 해야함!

```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)

# 팩토리얼 계산 예시
print(factorial(5)) # 120
```

## 재귀 함수 특징

  * 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들어, 코드의 가독성이 높아짐
  * 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

## 재귀 함수 활용 시 기억해야 할 것

  * 종료 조건을 명확히 할 것
  * 반복되는 호출이 종료 조건을 향하도록 할 것

> **스택 오버플로우**
> 
> 작업 공간에 일이 너무 많이 쌓여 프로그램이 멈추는 오류
## TIP

  * 재귀 함수는 메모리 사용량 많고 느릴 수 있음
  * 종료 조건 잘못되면 스택 오버플로우 에러 발생 가능
  * 복잡한 재귀 함수는 오히려 코드 가독성 저하 가능

## 재귀 함수를 사용하는 이유

* **문제의 자연스러운 표현**
    * 복잡한 문제를 간결하고 직관적으로 표현 가능

* **코드 간결성**
    * 상황에 따라 반복문보다 알고리즘 코드가 더 간결하고 명확해질 수 있음

* **수학적 문제 해결**
    * 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현 가능

# 내장 함수 (Bulit-in function)

> 파이썬이 기본적으로 제공하는 함수  
> (별도의 import 없이 바로 사용 가능)  

파이썬 공식 문서에서 자습서, 레퍼런스정도만 봐도 좋음  

## 자주 사용되는 내장 함수 예시

```python
numbers = [1, 2, 3, 4, 5]

print(numbers)              # [1, 2, 3, 4, 5]
print(len(numbers))         # 5
print(max(numbers))         # 5
print(min(numbers))         # 1
print(sum(numbers))         # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
```

# 함수와 Scope

## Python의 범위(Scope)

* 함수는 코드 내부에 `local scope`를 생성하며, 그 외의 공간인 `global scope`로 구분

---
## 범위와 변수 관계

* **scope**
    * `global scope` : 코드 어디에서든 참조할 수 있는 공간
    * `local scope` : 함수가 만든 scope (함수 내부에서만 참조 가능)
* **variable**
    * `global variable` : `global scope`에 정의된 변수
    * `local variable` : `local scope`에 정의된 변수

## Scope 예시

  * `num`은 `local scope`에 존재하기 때문에 `global scope`에서 사용할 수 없음
  * > 이는 변수의 **수명주기**와 연관이 있음

-----

```python
def func():
    num = 20
    print('local', num) # local 20

func()

print('global', num) # NameError: name 'num' is not defined
```

## 변수 수명주기(lifecycle)

***

* 변수의 수명주기는 변수가 선언되는 위치와 `scope`에 따라 결정됨

1.  **`built-in scope`**
    * 파이썬이 실행된 이후부터 영원히 유지
2.  **`global scope`**
    * 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3.  **`local scope`**
    * 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

## 이름 검색 규칙(Name Resolution)

* 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)
* 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
    1.  Local scope : 지역 범위(현재 작업 중인 범위)
    2.  Enclosed scope : 지역 범위 한 단계 위 범위
    3.  Global scope : 최상단에 위치한 범위
    4.  Built-in scope : 모든 것을 담고 있는 범위  
        (정의하지 않고 사용할 수 있는 모든 것)

---
함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음  

## LEGB Rule 예시

  * `sum`이라는 이름을 `global scope`에서 사용함으로써, 기존 `built-in scope`에 있던 내장함수 `sum`을 사용하지 못하게 됨
  * > `sum`을 참조 시 `LEGB Rule`에 따라 `global`에서 먼저 찾기 때문

-----

```python
print(sum) # <built-in function sum>
print(sum(range(3))) # 3

sum = 5

print(sum) # 5
print(sum(range(3))) # TypeError: 'int' object is not callable
```

-----

> **💡 코드 추가 설명** \> `sum` 변수 객체 삭제를 위해 `del sum`을 입력 후 진행

## LEGB Rule 퀴즈 (3/3)

```python
# ①
x = 'G'
y = 'G'

# ②
def outer_func():
    x = 'E'
    y = 'E'

    # ③
    def inner_func(y):
        z = 'L'
        # ④
        print(x, y, z)  # E P L
    
    # ⑤
    inner_func('P')
    # ⑥
    print(x, y) # E E

outer_func()
# ⑦
print(x, y) # G G
```

-----

## 추가 설명

  * **① G (global) 영역**
  * **② E (Enclosing) 영역**
  * **③ `inner_func(y)` 함수**
      * ‘y’는 파라미터로, Local 변수처럼 취급
      * 함수 안에는 ‘x’가 없지만, ‘z’는 있음
  * **④ `print(x, y, z)`  \# E P L**
      * `x`: L(없음) -\> E(찾음) -\> 'E'
      * `y`: L(파라미터 y 존재) -\> 전달받은 'P'
      * `z`: L(찾음) -\> 'L'
  * **⑤ `inner_func('P')`**
      * `inner_func`을 호출하면서 ‘P’라는 값을 인자로 전달
  * **⑥ `print(x, y)`  \# E E**
      * `x`: 이 함수의 Local 영역에서 'E'를 찾음
      * `y`: 이 함수의 Local 영역에서 'E'를 찾음
  * **⑦ `print(x, y)`  \# G G**
      * `x`: G(Global) 영역에서 'G'를 찾음
      * `y`: G(Global) 영역에서 'G'를 찾음


## 'global' 키워드

  * 변수의 스코프를 전역 범위로 지정하기 위해 사용
  * 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

-----

```python
num = 0 # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언 / num 수정 가능
    num += 1

print(num) # 0
increment()
print(num) # 1
```

## 'global' 키워드 주의사항 - 1

  * `global` 키워드 선언 전에 참조 불가

<!-- end list -->

```python
num = 0
def increment():
    # SyntaxError: name 'num' is used 
    # prior to global declaration
    print(num)
    global num
    num += 1
```

-----

## 'global' 키워드 주의사항 - 2

  * 매개변수에는 `global` 키워드 사용 불가

<!-- end list -->

```python
num = 0
def increment(num):
    # SyntaxError: "num" is assigned before global
    # declaration
    global num
    num += 1
```

## 함수 스타일 가이드
### 함수 이름 작성 규칙

## 기본 규칙

  * 소문자와 언더스코어(\_) 사용
  * 동사로 시작하여 함수의 동작 설명
  * 약어 사용 지양

-----

```python
# Good
def calculate_total_price(price, tax):
    return price + (price * tax)

# Bad
def calc_price(p, t):
    return p + (p * t)
```

## 함수 이름 구성 요소

* **동사 + 명사**
    * `save_user()`
* **동사 + 형용사 + 명사**
    * `calculate_total_price()`
* **get/set 접두사**
    * `get_username()`, `set_username()`

---

> **TIP**
>
> * 이름만으로 '무엇을 하는지' 명확하게 표현하세요.
> * `True`/`False`를 반환한다면 `is` 또는 `has` 로 시작하는 것을 추천합니다.
> * 프로젝트 전체에서 일관성을 지키는 것이 가독성에 도움을 줍니다.

## 단일 책임 원칙(Single Responsibility Principle)

* 모든 객체는 하나의 명확한 목적과 책임만을 가져야 함

---

## 함수 설계 원칙

1.  **명확한 목적**
    * 함수는 한 가지 작업만 수행
    * 함수 이름으로 목적을 명확히 표현
2.  **책임 분리**
    * 데이터 검증, 처리, 저장 등을 별도 함수로 분리
    * 각 함수는 독립적으로 동작 가능하도록 설계
3.  **유지보수성**
    * 작은 단위의 함수로 나누어 관리
    * 코드 수정 시 영향 범위를 최소화

## 잘못된 설계 예시

  * 여러 책임이 섞인 함수

-----

```python
def process_user_data(user_data):
    # 책임 1: 데이터 유효성 검사
    if len(user_data['password']) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다')

    # 책임 2: 비밀번호 암호화 및 저장
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)

    # 책임 3: 이메일 발송
    send_email(user_data['email'], '가입을 환영합니다!')
```

## 올바른 설계 예시

  * 책임을 분리한 함수들

-----

```python
def validate_password(password):
    """비밀번호 유효성 검사"""
    if len(password) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다')

def save_user(user_data):
    """비밀번호 암호화 및 저장"""
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)

def send_welcome_email(email):
    """환영 이메일 발송"""
    send_email(email, '가입을 환영합니다!')

# 메인 함수에서 순차적으로 실행
def process_user_data(user_data):
    validate_password(user_data['password'])
    save_user(user_data)
    send_welcome_email(user_data['email'])
```

# Packing & Unpacking

## 패킹 (Packing)

> 여러 개의 데이터를 하나의 컬렉션으로 모아 담는 과정

-----

> **기본 원리**
>
>   * 여러 개의 값을 하나의 튜플로 묶는 파이썬의 기본 동작
>   * 한 변수에 콤마(,)로 구분된 값을 넣으면 자동으로 튜플로 처리

-----

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values) # (1, 2, 3, 4, 5)
```

## '\*'을 활용한 패킹 (함수 매개변수 작성 시)

  * 남는 위치 인자들을 튜플로 묶기
  * `*`를 붙인 매개변수가 남는 위치 인자들을 모두 모아 하나의 튜플로 만듦

-----

```python
def my_func(*args):
    print(args) # (1, 2, 3, 4, 5)
    print(type(args)) # <class 'tuple'>

my_func(1, 2, 3, 4, 5)
```

## '\*\*'을 활용한 패킹 (함수 매개변수 작성 시)

  * 남는 키워드 인자들을 딕셔너리로 묶기
  * `**`를 붙인 매개변수가 남는 키워드 인자들을 모두 모아 하나의 딕셔너리로 만듦

-----

```python
def my_func2(**kwargs):
    print(kwargs) # {'a': 1, 'b': 2, 'c': 3}
    print(type(kwargs)) # <class 'dict'>

my_func2(a=1, b=2, c=3)
```

## print 함수의 패킹 예시

  * `print` 함수에서 임의의 가변 인자를 작성할 수 있었던 이유
  * > 인자 개수에 상관 없이 튜플 하나로 패킹 되어서 내부에서 처리

-----

```python
def my_func(*objects):
    print (objects) # (1, 2, 3, 4, 5)
    print(type(objects)) # <class 'tuple'>

my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>
```

-----

> ```python
> #공식 문서 발췌
> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
> ```
>
> `objects` 를 텍스트 스트림 `file` 로 인쇄하는데, `sep` 로 구분되고 `end` 를 뒤에 붙입니다. 있다면, `sep`, `end`, `file` 및 `flush` 는 반드시 키워드 인자로 제공해야 합니다.
>
> 모든 비 키워드 인자는 `str()` 이 하듯이 문자열로 변환된 후 스트림에 쓰이는데, `sep` 로 구분되고 `end` 를 뒤에 붙입니다.

end = '\n' 을 끄고 싶으면?  
print('hello', end=' ')  

# 언패킹 (Unpacking)

> 컬렉션에 담겨있는 데이터들을 개별 요소로 펼쳐 놓는 과정

-----

> **기본 원리**
>
>   * 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
>   * ‘시퀀스 언패킹(Sequence Unpacking)’ 또는 ‘다중 할당(Multiple Assignment)’이라고 부름

-----

```python
packed_values = 1, 2, 3, 4, 5
# (1, 2, 3, 4, 5) 튜플의 각 요소들이  
# a, b, c, d, e 변수에 순서대로 '언패킹' 되어 할당됨
a, b, c, d, e = packed_values
print(a, b, c, d, e) # 1 2 3 4 5
```

## '\*'을 활용한 패킹 (함수 인자 전달)

  * 리스트나 튜플 앞에 `*`를 붙여 각 요소를 함수의 개별 위치 인자로 전달

-----

```python
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names) # alice jane peter
```

## '\*\*'을 활용한 언패킹 (딕셔너리 -\> 함수 키워드 인자)

  * 딕셔너리 앞에 `**`를 붙여 `{키: 값}` 쌍을 `키=값` 형태의 키워드 인자로 전달

-----

```python
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict) # 1 2 3
```
x y z / 'z': 1 'x': 2 'y': 3 써도 될까?   

## Packing & Unpacking, `*` & `**` 정리

| 구분 | 상황 | * 연산자 | ** 연산자 |
| :--- | :--- | :--- | :--- |
| **패킹** | 함수 정의 시 | 여러 위치 인자를 하나의 튜플로 받음 | 여러 키워드 인자를 하나의 딕셔너리로 받음 |
| **언패킹** | 함수 호출 시 | 리스트/튜플을 개별 위치 인자로 전달 | 딕셔너리를 개별 키워드 인자로 전달 |

# 참고
## 함수와 반환

## 함수의 return, 반환의 원칙

  * 파이썬 함수는 언제나 단 하나의 값(객체)만 반환할 수 있음
  * 여러 값을 반환하는 경우에도 하나의 튜플로 패킹하여 반환

-----

```python
def get_user_info():
    name = 'Alice'
    age = 30
    # 콤마(,)로 여러 값을 반환하는 것처럼 보임
    return name, age

# 반환된 값을 user_data 변수에 담아 확인해보면
user_data = get_user_info()

# 단 하나의 튜플을 반환하는 것
print(user_data) # ('Alice', 30)
```
## 파이썬 함수의 반환 핵심

1.  파이썬 함수는 오직 **하나의 값(객체)**만 `return` 할 수 있음
2.  `return a, b, c` 처럼 콤마를 사용하면, 파이썬이 값들을 하나의 튜플로 자동 패킹하여 반환
3.  반환된 튜플은 각 변수에 언패킹하여 사용할 수 있음


# 람다 표현식
## 람다 표현식(Lambda expressions)

* 익명 함수를 만드는 데 사용되는 표현식
* 한 줄로 간단한 함수를 정의

---

## 람다 표현식 구조

* **`lambda` 키워드**
    * 람다 함수를 선언하기 위해 사용되는 키워드
* **매개변수**
    * 함수에 전달되는 매개변수들
    * 여러 개의 매개변수가 있을 경우 쉼표로 구분
* **표현식**
    * 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성

## 람다 표현식 예시

  * 간단한 연산이나 함수를 한 줄로 표현할 때 사용
  * 함수를 매개변수로 전달하는 경우에도 유용하게 활용

-----

### 기본 변환


```python
def addition(x, y):
    return x + y
```

```python
lambda x, y: x + y
```


-----

### 변수 할당 및 사용



```python
def addition(x, y):
    return x + y

result = addition(3, 5)
print(result) # 8
```

```python
addition = lambda x, y: x + y

result = addition(3, 5)
print(result) # 8
```

## 람다 표현식 활용 (with `map` 함수)

```python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1) # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2) # [1, 4, 9, 16, 25]
```