
목차

상속
- 상속 기본 개념
- 부모 클래스와 자식 클래스
- 메서드 오버라이딩
- 다중 상속
- super() 메서드

에러와 예외
- 디버깅
- 에러


예외 처리
- try & except
- 복수 예외 처리
- else & finally

참고
- 예외 처리 주의사항
- 예외 객체 다루기
- EAFP & LBYL
- 클래스의 의미와 활용


## 상속 Inheritance 
 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것  

### 상속이 필요한 이유
**1. 코드 재사용**
* 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
* 기존 클래스를 수정하지 않고도 기능을 확장할 수 있음  

**2. 계층 구조**
* 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
* 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음


**3. 유지 보수의 용이성**
* 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
* 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

```python
class Animal:
    def eat(self):
        print('먹는 중')

class Dog(Animal):
    def bark(self):
        print('멍멍')

my_dog = Dog()
my_dog.bark() # 멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat() # 먹는 중
```
> 자식 클래스를 정의할 때 반드시 상속하려는 부모 클래스 이름을 함께 선언할 것


### 상속 없이 구현하는 경우(1/2)

  * 상속 없이 구현하는 경우 학생/교수 정보를 별도로 표현하기 어려움
  * Person class만 사용하는 경우 학생과 교수가 가지는 각각의 고유 속성을 표현하기 어려움. 나이와 이름만으로는 직업 정보를 나타낼 수 없음

<!-- end list -->

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk() # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk() # 반갑습니다. 박교수입니다.
```

### 상속 없이 구현하는 경우(2/2)

  * 상속 없이 구현하는 경우 교수/학생 클래스를 각각 선언하여 구현함  
  * 클래스를 각각 분리했지만 메서드가 중복으로 정의될 수 있음  

<!-- end list -->

```python
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self): # 중복
        print(f'반갑습니다. {self.name}입니다.')
```

```python
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self): # 중복
        print(f'반갑습니다. {self.name}입니다.')
```

※ 중복되고 있는 공통 속성인 name, age와 메서드 talk를 부모 클래스에서 한 번만 정의하고, 필요한 클래스들이 이 부모 클래스를 물려받아 사용할 수 있습니다.  


### 메서드 오버라이딩
Method Overriding | 부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의하는 것  

* 자식 클래스에서 메서드를 다시 정의하면, 부모 클래스의 메서드 대신 자식 클래스의 메서드가 실행됩니다.  
* 오버라이딩은 동일한 이름과 매개변수를 사용하지만, 내부 동작을 원하는 대로 바꿀 수 있게 해줍니다.  
* 부모 클래스의 기능을 유지하면서도 일부 동작을 맞춤형으로 바꾸고 싶을 때 유용합니다.  


### 메서드 오버라이딩 예시

  * 자식 클래스가 부모 클래스의 메서드를 덮어써서 새로운 동작을 구현할 수 있음  
  * Animal class를 상속받은 Dog 클래스에서 eat 메서드를 다시 정의하는 것  

<!-- end list -->

```python
class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 부모 클래스(Animal)의 eat 메서드를 재정의(오버라이딩)
    def eat(self):
        print('Dog가 먹는 중')

my_dog = Dog()
my_dog.eat() # Dog가 먹는 중
```


### 참고 오버로딩 (Overloading)

  * 같은 이름, 다른 파라미터를 가진 여러 메서드를 정의하는 것(파이썬은 미지원)
  * 파이썬은 실제로 하나의 메서드만 인식하며, 인자의 형태가 다르다는 이유로 메서드를 여러 개 구분하여 불러주지 않음
  * 아래 예시 코드의 파이썬은 마지막으로 선언된 메서드만 인식함

<!-- end list -->

```python
class Example:
    def do_something(self, x):
        print('첫 번째 do_something 메서드:', x)

    # 파이썬에서는 메서드가 "이름"이 같으면 앞선 정의를 덮어버림
    def do_something(self, x, y):
        print('두 번째 do_something 메서드:', x, y)

example = Example()

# TypeError: do_something() missing 1 required positional argument: 'y'
example.do_something(10)
```
> 인자가 다르다고 다르게 보지 않음.  
> 함수 이름이 같아서 덮어씀


## 다중 상속
* 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있습니다.  
* 상속받은 모든 클래스의 요소를 활용 가능합니다.  
* 중복된 속성이나 메서드가 있는 경우 **상속 순서**에 의해 결정됩니다.  

### 다이아몬드 문제 (The diamond problem)
* 두 클래스 B와 C가 A에서 상속되고 클래스 D가 B와 C 모두에서 상속될 때 발생하는 모호함

### 파이썬에서의 해결책

  * MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록을 생성
  * 부모 클래스로부터 상속된 속성을 정해진 내부 알고리즘에 따라 검색  
  * 이 순서는 기본적으로 왼쪽에서 오른쪽으로 진행되며, 계층 구조에서 중복되는 클래스는 한 번만 확인  
  * 그래서, 속성이 D에서 발견되지 않으면, B에서 찾고, 거기에서도 발견되지 않으면, C에서 찾고, 이런 식으로 진행됨  

<!-- end list -->

```python
class D(B, C):
    pass
```
----

### super()
super() | 메서드 해석 순서(MRO)에 따라, 현재 클래스의 부모(상위) 클래스의 메서드나 속성에 접근할 수 있게 해주는 내장 함수  

* `super()`를 사용하면 직접 부모 클래스 이름을 적지 않아도 MRO에 따라 자동으로 올바른 메서드를 찾아 실행할 수 있습니다.  
* 다중 상속에서 `super()`를 호출하면 상속 순서에 맞춰 여러 부모 클래스의 메서드를 순차적으로 실행할 수 있습니다.  
* 생성자나 오버라이딩된 메서드에서 `super()`를 호출하면 부모 클래스의 초기화 로직을 그대로 활용 가능합니다.  


### super() 특징
* 단순히 "부모 클래스의 메서드를 호출"하기 위한 용도뿐만 아니라, 다중 상속(Multiple Inheritance)이 있을 때도 올바른 순서(MRO)에 따라 상위 클래스의 메서드를 찾아 실행하기 위해 `super()`를 사용  

### super()의 2가지 사용 사례
**1. 단일 상속 구조**  
**2. 다중 상속 구조**  

```python
class Student(Person):
    def __init__(self, name, age, number, email, student_id):  
        # super()를 통해 Person의 __init__ 메서드 호출
        super().__init__(name, age, number, email)
        self.student_id = student_id
```
> 나중에 Person이라는 클래스 이름이 바뀌거나 구조가 바뀌어도 그대로 사용 가능해서 유지보수성 향상   

