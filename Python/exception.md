# 에러와 예외
## 디버깅

### 버그
bug | 소프트웨어에서 발생하는 오류 또는 결함 프로그램의 예상된 동작과 실제 동작 사이의 불일치

### 디버깅
Debugging | 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정 프로그램의 오작동 원인을 식별하여 수정하는 작업

* 디버깅은 코드 실행 과정에서 변수 값이나 흐름을 점검하며 문제의 정확한 위치와 원인을 찾아내는 과정입니다.  
* 효과적인 디버깅을 위해 단계별로 코드를 실행하거나 로그를 출력해 프로그램 상태를 확인합니다.  

### 디버깅 방법
**1. print 함수 활용**
* 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각

**2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용**
* breakpoint, 변수 조회 등

**3. Python tutor 활용 (단순 파이썬 코드인 경우)**

**4. 뇌 컴파일, 눈 디버깅 등**

### 에러
Error | 프로그램 실행 중에 발생하는 예외 상황

### 파이썬의 에러 유형

**문법 에러**
Syntax Error
프로그램의 구문이 올바르지 않은 경우 발생
(오타, 괄호 및 콜론 누락 등의 문법적 오류)

—

**예외**
Exception
프로그램 실행 중에 감지되는 에러

* 예외는 프로그램이 잘못된 동작을 시도할 때 자동으로 감지됩니다.
* 예를 들어, 리스트에 없는 값을 꺼내려 하면 예외가 발생합니다.
* 이런 상황을 처리하지 않으면 프로그램은 즉시 종료됩니다.

### 내장 예외
Built-in Exceptions | 예외 상황을 나타내는 예외 클래스들

* 내장 예외는 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용합니다.  
* 예를 들어 ZeroDivisionError는 0으로 나눌 때, FileNotFoundError는 없는 파일을 열 때 발생합니다. 이러한 예외를 사용하면 오류에 맞는 적절한 처리 방법을 적용할 수 있습니다.  


내장 예외들 이름 파스칼케이스

  * **ZeroDivisionError**: 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생

    ```python
    10/0
    # ZeroDivisionError: division by zero
    ```

  * **NameError**: 지역 또는 전역 이름을 찾을 수 없을 때 발생

    ```python
    print(name1)
    #NameError: name 'name1' is not defined
    ```

  * **TypeError**: 타입 불일치

    ```python
    '2' + 2 # TypeError: can only concatenate str (not "int") to str
    ```

  * **TypeError**: 인자 누락

    ```python
    sum() # TypeError: sum() takes at least 1 positional argument (0 given)
    ```

      * **TypeError**: 인자 초과

    ```python
    sum(1, 2, 3) #TypeError: sum() takes at most 2 arguments (3 given)
    ```

  * **TypeError**: 인자 타입 불일치

    ```python
    import random
    random.sample(1, 2)
    # TypeError: Population must be a sequence. For dicts or sets, use sorted(d).
    ```

  * **ValueError**: 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError처럼 더 구체적인 예외로 설명되지 않는 경우 발생

    ```python
    int('1.5') # ValueError: invalid literal for int() with base 10: '1.5'
    range(3).index(6) # ValueError: 6 is not in range
    ```

  * **IndexError**: 시퀀스 인덱스가 범위를 벗어남

    ```python
    empty_list = []
    empty_list[2]
    # IndexError: list index out of range
    ```
  * **KeyError**: 딕셔너리에 해당 키가 존재하지 않는 경우

    ```python
    person = {'name': 'Alice'}
    person['age'] # KeyError: 'age'
    ```

  * **ModuleNotFoundError**: 모듈을 찾을 수 없을 때

    ```python
    import hahaha
    #ModuleNotFoundError: No module named 'hahaha'
    ```

  * **ImportError**: import하려는 이름을 찾을 수 없을 때

    ```python
    from random import hahaha
    #ImportError: cannot import name 'hahaha' from 'random'
    ```


  * **KeyboardInterrupt**: 사용자가 Control-C 또는 Delete를 누를 때 발생

      * 무한루프 시 강제 종료

    <!-- end list -->

    ```python
    while True:
        continue
    # ...
    # Traceback (most recent call last):
    #  File "...", line 20, in <module>
    #    continue
    # KeyboardInterrupt
    # ...
    ```

  * **IndentationError**

      * 잘못된 들여쓰기와 관련된 문법 오류

    <!-- end list -->

    ```python
    for i in range(10):
    print(i)
    #IndentationError: expected an indented block after 'for' statement on line 19
    ```
    ---

    ## 예외 처리
(Exception Handling) | 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

* 예외 처리를 통해 오류가 발생해도 프로그램의 흐름을 안전하게 이어갈 수 있습니다.  
* Python에서는 try, except 구문을 사용해 특정 예외를 잡아내고 원하는 동작을 수행할 수 있습니다.  
* 예외 처리를 구현하면 프로그램 사용자에게 오류 메시지를 보여주거나 대체 로직을 실행할 수 있습니다.  

### 예외처리 사용 구문

  * **try**
      * 예외가 발생할 수 있는 코드 작성
  * **except**
      * 예외가 발생했을 때 실행할 코드 작성
  * **else**
      * 예외가 발생하지 않았을 때 실행할 코드 작성
  * **finally**
      * 예외 발생 여부와 상관없이 항상 실행할 코드 작성

<!-- end list -->

```python
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')
```

### try-except 구조

try-except 구조 | 
```python
try:
# 예외가 발생할 수 있는 코드
except 예외:
# 예외 처리 코드

```

* try 블록 안에는 예외가 발생할 수 있는 코드를 작성합니다.
* except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성합니다.  
* 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동합니다.
```

### else & finally

  * else 블록은 예외가 발생하지 않았을 때 추가 작업을 진행
  * finally 블록은 예외 발생 여부와 상관없이 항상 실행할 코드를 작성

<!-- end list -->

```python
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')
```


# 참고
## 예외 처리 주의사항

### 내장 예외의 상속 계층구조 주의 (1/2)

  * 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함

<!-- end list -->

```python
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except Exception:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.') # 이 블록에 도달하지 못함
except:
    print('에러가 발생하였습니다.')
```

※ `except Exception`이 모든 예외를 먼저 가로채기 때문에, 그 아래에 있는 `ZeroDivisionError` 전용 처리 코드는 절대 실행되지 않습니다.
※ 항상 범용적인 예외 처리(Exception)는 마지막에 두어야 합니다.

### as 키워드

  * 예외객체 : 예외가 발생했을 때 예외에 대한 정보를 담고 있는 객체
  * except 블록에서 예외 객체를 받아 상세한 예외 정보를 활용 가능

<!-- end list -->

```python
my_list = []
try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')

# list index out of range가 발생했습니다.
```

※ 빈 리스트에서 잘못된 인덱스를 참조할 때 IndexError 예외가 발생하는 예시입니다.
※ `error` 변수에 담긴 예외 메시지를 출력하면 구체적인 오류 내용을 쉽게 확인할 수 있습니다.

### try-except와 if-else

  * try-except와 if-else를 함께 사용할 수 있음

<!-- end list -->

```python
try:
    x = int(input('숫자를 입력하세요: '))
    if x < 0:
        print('음수는 허용되지 않습니다.')
    else:
        print('입력한 숫자:', x)
except ValueError:
    print('오류 발생')
```

※ 입력값이 정수가 아니면 ValueError 예외가 발생해 오류 메시지를 출력합니다.
※ 정상 입력이면 음수인지 양수인지 구분해 각각 다른 문장을 출력합니다.

### EAFP
"Easier to Ask for Forgiveness than Permission"
예외처리를 중심으로 코드를 작성하는 접근 방식 (try-except)

—

### LBYL
"Look Before You Leap"
값 검사를 중심으로 코드를 작성하는 접근 방식 (if-else)

```python
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')
```

**EAFP**

```python
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```

**LBYL**


### 접근 방식 비교

| EAFP | LBYL |
|---|---|
| "일단 실행하고 예외를 처리" | "실행하기 전에 조건을 검사" |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행 | 코드 실행 전 조건문을 사용하여 예외 상황을 미리 검사하고, 예외 상황을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라, 예외가 발생한 후에 예외를 처리 | 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수 있음 |
| 예외 상황을 예측하기 어려운 경우에 유용 | 예외 상황을 미리 방지하고 싶을 때 유용 |

---


## 핵심 키워드
### 개념 정리표

| 개념 | 설명 | 예시 |
|---|---|---|
| 상속 (Inheritance) | 부모 클래스의 속성과 메서드를 자식 클래스가 물려받는 기능 | `class Student(Person):` |
| 오버라이딩 (Overriding) | 부모 클래스의 메서드를 자식 클래스에서 같은 이름으로 재정의 | `def talk(self):` (자식 클래스에서 다시 정의) |
| super() | 부모 클래스의 메서드를 호출할 때 사용하는 내장 함수 | `super().__init__(name, age)` |
| 다중 상속 | 둘 이상의 클래스를 동시에 상속받는 구조 | `class Child(Mom, Dad):` |
| MRO (Method Resolution Order) | 다중 상속 시 메서드를 탐색하는 우선 순서 | `ClassName.mro()` |
| 예외 처리 (try-except) | 프로그램 실행 중 발생하는 예외를 처리하는 구조 | `try: ... except ZeroDivisionError:` |
| else-finally | try에서 예외가 없으면 else가 실행되고, finally는 항상 실행되는 구문 | `else-finally` |
---

## 요약
* **상속(Inheritance)**
    * 기존 클래스(부모)의 속성과 메서드를 새로운 클래스(자식)가 물려받아 코드 재사용이 가능
    * 중복 코드를 줄이고, 계층 구조를 만들어 유지보수성 향상

* **메서드 오버라이딩(Overriding)**
    * 자식 클래스가 부모의 메서드를 같은 이름으로 재정의하여 동작을 변경
    * 객체의 특성에 맞는 동작을 구현할 수 있음

* **super() 함수**
    * 부모 클래스의 메서드를 명시적 클래스명 없이 호출 가능
    * 다중 상속에서도 MRO 순서에 따라 올바르게 작동함

* **다중 상속과 MRO**
    * 여러 클래스를 동시에 상속받을 수 있고, Python은 MRO(Method Resolution Order)를 통해 어떤 부모의 메서드를 먼저 사용할지 결정함

* **예외(Exception) 처리**
    * 실행 중 발생할 수 있는 오류를 try-except 구문으로 처리하여 프로그램의 안정성 확보
    * else, finally, as를 통해 세부 동작 및 예외 정보 활용 가능

* **예외 처리 스타일: EAFP vs LBYL**
    * EAFP: 먼저 시도하고, 실패 시 처리 (Python 권장 방식)
    * LBYL: 먼저 조건을 검사한 후 실행



