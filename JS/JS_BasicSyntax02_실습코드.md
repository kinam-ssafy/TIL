# JavaScript Basic Syntax 02 실습 코드 정리

## 📚 목차

1. [객체 (Object)](#1-객체-object)
2. [this 키워드](#2-this-키워드)
3. [추가 객체 문법](#3-추가-객체-문법)
4. [JSON](#4-json)
5. [배열 (Array)](#5-배열-array)
6. [배열 메서드](#6-배열-메서드)
7. [Array Helper Methods](#7-array-helper-methods)
8. [배열 순회](#8-배열-순회)
9. [배열과 전개 구문](#9-배열과-전개-구문)
10. [참고: 클래스](#10-참고-클래스)
11. [참고: 콜백 함수](#11-참고-콜백-함수)
12. [참고: 비동기](#12-참고-비동기)
13. [참고: forEach break](#13-참고-foreach-break)
14. [참고: reduce 메서드](#14-참고-reduce-메서드)
15. [실습 문제](#15-실습-문제)

---

## 1. 객체 (Object)

**파일명**: `01-object.html`

객체의 생성, 조회, 추가, 수정, 삭제, in 연산자, 메서드 호출을 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 객체 생성 ===
    const user = {
      name: 'Alice',
      'key with space': true,  // 띄어쓰기가 있는 키는 따옴표로 감싸기
      greeting: function () {
        return 'hello'
      }
    }

    // === 속성 조회 ===
    // 점 표기법 (정적인 접근)
    console.log(user.name) // 'Alice'
    
    // 대괄호 표기법 (동적인 접근)
    // console.log(user.'key with space')  // SyntaxError (점 표기법으로는 불가능)
    console.log(user['key with space']) // true

    // === 속성 추가 ===
    user.address = 'korea'
    console.log(user) 
    // {name: 'Alice', key with space: true, address: 'korea', greeting: ƒ}

    // === 속성 수정 ===
    user.name = 'Bella'
    console.log(user.name) // 'Bella'

    // === 속성 삭제 ===
    delete user.name
    console.log(user) 
    // {key with space: true, address: 'korea', greeting: ƒ}

    // === in 연산자 ===
    // 속성이 객체에 존재하는지 확인
    console.log('greeting' in user) // true
    console.log('country' in user)  // false

    // === 메서드 호출 ===
    console.log(user.greeting()) // 'hello'

    // === 1. 객체 표기법 비교 ===
    // 점 표기법: 정적인 변수 (키를 직접 명시)
    // 대괄호 표기법: 동적인 변수 (변수로 키 접근 가능)
    const user2 = { name: "Alice", age: 30 };

    for (let key in user2) {
      console.log(user2.key);   // undefined (key라는 속성을 찾음)
      console.log(user2[key]);  // "Alice", 30 (변수 key의 값으로 접근)
    }

    // === 2. in 연산자 주의사항 ===
    const user3 = { name: "Alice" };

    // in 연산자는 프로토타입 체인까지 확인
    console.log("name" in user3);      // true (자신의 속성)
    console.log("toString" in user3);  // true (조상의 속성!)

    // 해결 방법 1 (Classic): .hasOwnProperty()
    console.log(user3.hasOwnProperty("name"));     // true
    console.log(user3.hasOwnProperty("toString")); // false (자신의 속성이 아님)

    // 해결 방법 2 (ES2022): Object.hasOwn()
    // Object.create()로 생성한 객체는 hasOwnProperty가 없을 수 있음 => 에러 방지
    console.log(Object.hasOwn(user3, "name"));     // true
    console.log(Object.hasOwn(user3, "toString")); // false
  </script>
</body>
</html>
```

**핵심 개념:**
- **객체 생성**: 중괄호 `{}`로 생성, `key: value` 쌍으로 구성
- **점 표기법**: `object.key` (정적인 접근)
- **대괄호 표기법**: `object[key]` (동적인 접근, 변수 사용 가능)
- **in 연산자**: 속성 존재 여부 확인 (프로토타입 체인까지 확인)
- **hasOwnProperty()**: 자신의 속성인지만 확인 (프로토타입 제외)

**주의사항:**
- 띄어쓰기가 있는 키는 대괄호 표기법으로만 접근 가능
- `in` 연산자는 상속받은 속성까지 확인하므로, 자신의 속성만 확인하려면 `hasOwnProperty()` 사용

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 객체, 구조 및 속성 섹션

---

## 2. this 키워드

**파일명**: `02-this-keyword.html`

this 키워드의 동작 방식과 화살표 함수에서의 차이를 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 메서드와 this 예시 ===
    const person = {
      name: 'Alice',
      greeting: function () {
        return `Hello my name is ${this.name}`
      },
    }

    console.log(person.greeting()) // 'Hello my name is Alice'
    // this는 메서드를 호출한 객체(person)를 가리킴

    // === 1.1 단순 호출 ===
    // 일반 함수의 this는 전역 객체(window)를 가리킴
    const myFunc = function () {
      return this
    }
    console.log(myFunc()) // window

    // === 1.2 메서드 호출 ===
    // 메서드의 this는 메서드를 호출한 객체를 가리킴
    const myObj = {
      data: 1,
      myFunc: function () {
        return this
      }
    }
    console.log(myObj.myFunc()) // myObj

    // === 2. 중첩된 함수에서의 this 문제 ===
    // === 2.1 일반 함수 ===
    const myObj2 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        // forEach의 콜백 함수는 일반 함수로 호출됨
        this.numbers.forEach(function (number) {
          console.log(this) // window (전역 객체!)
          // 콜백 함수는 단순 호출이므로 this가 window를 가리킴
        })
      }
    }
    console.log(myObj2.myFunc())

    // === 2.2 화살표 함수 (문제 해결) ===
    const myObj3 = {
      numbers: [1, 2, 3],
      myFunc: function () {
        // 화살표 함수는 자신만의 this를 가지지 않음
        // 상위 스코프(myFunc)의 this를 그대로 사용
        this.numbers.forEach((number) => {
          console.log(this) // myObj3 (상위 함수의 this)
        })
      }
    }
    console.log(myObj3.myFunc())
  </script>
</body>
</html>
```

**핵심 개념:**
- **this**: 함수를 **호출하는 방법**에 따라 가리키는 대상이 달라짐
  - 단순 호출: 전역 객체 (window)
  - 메서드 호출: 메서드를 호출한 객체
- **화살표 함수의 this**: 자신만의 this를 가지지 않고, 상위 스코프의 this를 참조

**주의사항:**
- 중첩된 함수(콜백 함수 등)에서 this를 사용할 때는 화살표 함수 사용 권장
- "누가 점(`.`)을 찍어 호출했는가?"를 생각하면 this를 이해하기 쉬움

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - this 섹션

---

## 3. 추가 객체 문법

**파일명**: `03-extra-object-syntax.html`

단축 속성, 단축 메서드, 계산된 속성, 구조 분해 할당, 전개 구문, Optional Chaining을 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 1. 단축 속성 (Shorthand Property) ===
    // 키 이름과 값 변수명이 같으면 축약 가능
    const name = 'Alice'
    const age = 30

    // 단축 속성 전
    // const user = {
    //   name: name,
    //   age: age
    // }

    // 단축 속성 후
    const user = {
      name,  // name: name과 동일
      age    // age: age와 동일
    }

    // === 2. 단축 메서드 (Shorthand Method) ===
    // function 키워드 생략 가능

    // 단축 메서드 전
    // const myObj1 = {
    //   myFunc: function () {
    //     return 'Hello'
    //   }
    // }

    // 단축 메서드 후
    const myObj1 = {
      myFunc() {  // function 키워드 생략
        return 'Hello'
      }
    }

    // === 3. 계산된 속성 (Computed Property Name) ===
    // 키를 대괄호로 감싸서 동적으로 생성
    const product = prompt('물건 이름을 입력해주세요')
    const prefix = 'my'
    const suffix = 'property'

    const bag = {
      [product]: 5,              // 변수 값을 키로 사용
      [prefix + suffix]: 'value' // 표현식 결과를 키로 사용
    }

    console.log(bag) // {연필: 5, myproperty: 'value'}

    // === 4. 구조 분해 할당 (Destructuring Assignment) ===
    // 객체의 속성을 변수로 쉽게 추출
    const userInfo = {
      firstName: 'Alice',
      userId: 'alice123',
      email: 'alice123@gmail.com'
    }

    // 구조 분해 할당 전
    // const firstName = userInfo.firstName
    // const userId = userInfo.userId
    // const email = userInfo.email

    // 구조 분해 할당 후
    // const { firstName } = userInfo
    // const { firstName, userId } = userInfo
    const { firstName, userId, email } = userInfo
    console.log(firstName, userId, email) // 'Alice' 'alice123' 'alice123@gmail.com'

    // 구조 분해 할당 활용 - 함수 매개변수
    // 구조 분해 할당 활용 전
    // function printInfo(userInfo) {
    //   console.log(`이름: ${userInfo.firstName}, 이메일: ${userInfo.email}`)
    // }
    // printInfo(userInfo)

    // 구조 분해 할당 활용 후
    function printInfo({ firstName, email }) {
      console.log(`이름: ${firstName}, 이메일: ${email}`)
    }
    printInfo(userInfo) // '이름: Alice, 이메일: alice123@gmail.com'

    // === 5. 전개 구문 (Spread Syntax) ===
    // 객체를 펼쳐서 새로운 객체 생성 (얕은 복사)
    const obj = { a: 2, c: 3, d: 4 }
    const newObj = {...obj, a: 1, e: 5 }  // obj를 펼치고, a 덮어쓰기, e 추가
    console.log(newObj) // {a: 1, c: 3, d: 4, e: 5}

    // === 6. 유용한 객체 메서드 ===
    const profile = {
      name: 'Alice',
      age: 30
    }

    console.log(Object.keys(profile))    // ['name', 'age'] (키 배열)
    console.log(Object.values(profile))  // ['Alice', 30] (값 배열)
    console.log(Object.entries(profile)) // [['name', 'Alice'], ['age', 30]] (키-값 쌍 배열)

    // === 7. Optional Chaining (?.) ===
    // 중첩된 객체의 속성에 안전하게 접근
    const userData = {
      name: 'Alice',
      greeting: function () {
        return 'hello'
      }
    }

    // 예전 방식 (&&로 체크)
    console.log(userData.address && userData.address.street) // undefined

    // Optional Chaining 사용 전 (에러 발생!)
    // console.log(userData.address.street) 
    // Uncaught TypeError: Cannot read properties of undefined (reading 'street')

    // Optional Chaining 사용 후 (안전하게 접근)
    console.log(userData.address?.street) // undefined (에러 없이 undefined 반환)

    // 함수에도 Optional Chaining 사용 가능
    // console.log(userData.nonMethod()) 
    // Uncaught TypeError: userData.nonMethod is not a function
    
    console.log(userData.nonMethod?.()) // undefined (에러 없이 undefined 반환)
    
    // === Optional Chaining 주의사항 ===
    // 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
    // user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문
    
    // Bad (user도 ?로 체크하면 user 자체가 없는 문제를 놓칠 수 있음)
    // userData?.address?.street

    // Good (user는 반드시 있어야 하므로 ? 없이 접근)
    userData.address?.street
  </script>
</body>
</html>
```

**핵심 개념:**
- **단축 속성**: 키와 값 변수명이 같으면 `{name}` 형태로 축약
- **단축 메서드**: `function` 키워드 생략 가능
- **계산된 속성**: `[변수]` 형태로 동적 키 생성
- **구조 분해 할당**: `const {key} = obj` 형태로 속성 추출
- **전개 구문**: `{...obj}` 형태로 객체 복사 및 병합
- **Optional Chaining**: `obj?.prop` 형태로 안전한 속성 접근

**주의사항:**
- Optional Chaining은 존재하지 않아도 괜찮은 속성에만 사용
- 반드시 있어야 하는 속성에 `?`를 사용하면 오류를 놓칠 수 있음

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 추가 객체 문법 섹션

---

## 4. JSON

**파일명**: `04-json.html`

JavaScript 객체와 JSON 간 변환을 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === JavaScript 객체 ===
    const jsObject = {
      coffee: 'Americano',
      iceCream: 'Cookie and cream'
    }

    // === Object → JSON (문자열로 변환) ===
    const objToJson = JSON.stringify(jsObject)
    console.log(objToJson)  
    // '{"coffee":"Americano","iceCream":"Cookie and cream"}' (문자열)
    console.log(typeof objToJson)  // 'string'

    // === JSON → Object (객체로 변환) ===
    const jsonToObj = JSON.parse(objToJson)
    console.log(jsonToObj)  
    // { coffee: 'Americano', iceCream: 'Cookie and cream' } (객체)
    console.log(typeof jsonToObj)  // 'object'
  </script>
</body>
</html>
```

**핵심 개념:**
- **JSON (JavaScript Object Notation)**: 데이터 교환을 위한 텍스트 형식
- **JSON.stringify()**: JavaScript 객체 → JSON 문자열
- **JSON.parse()**: JSON 문자열 → JavaScript 객체

**주의사항:**
- JSON은 **문자열**이므로 직접 조작 불가
- 객체로 파싱한 후에야 속성에 접근 가능

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - JSON 섹션

---

## 5. 배열 (Array)

**파일명**: `05-array.html`

배열의 기본 구조와 요소 접근, 수정을 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 배열 생성 ===
    const names = ['Alice', 'Bella', 'Cathy']

    // === 배열 요소 접근 (인덱스는 0부터 시작) ===
    console.log(names[0]) // 'Alice'
    console.log(names[1]) // 'Bella'
    console.log(names[2]) // 'Cathy'

    // === 배열 길이 ===
    console.log(names.length) // 3

    // === 배열 요소 수정 ===
    names[1] = 'Dan'
    console.log(names) // ['Alice', 'Dan', 'Cathy']
  </script>
</body>
</html>
```

**핵심 개념:**
- **배열**: 순서가 있는 데이터의 집합
- **인덱스**: 0부터 시작하는 위치 값
- **length**: 배열의 길이 (요소 개수)
- **요소 수정**: `array[index] = newValue` 형태로 수정

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 배열 섹션

---

## 6. 배열 메서드

**파일명**: `06-array-method.html`

push, pop, shift, unshift 메서드를 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    const names = ['Alice', 'Bella', 'Cathy']

    // === pop(): 배열 끝 요소 제거 및 반환 ===
    console.log(names.pop()) // 'Cathy' (제거된 요소 반환)
    console.log(names)       // ['Alice', 'Bella']

    // === push(): 배열 끝에 요소 추가 ===
    names.push('Dan')
    console.log(names) // ['Alice', 'Bella', 'Dan']

    // === shift(): 배열 앞 요소 제거 및 반환 ===
    console.log(names.shift()) // 'Alice' (제거된 요소 반환)
    console.log(names)         // ['Bella', 'Dan']

    // === unshift(): 배열 앞에 요소 추가 ===
    names.unshift('Eric')
    console.log(names) // ['Eric', 'Bella', 'Dan']
  </script>
</body>
</html>
```

**핵심 개념:**

| 메서드 | 위치 | 동작 | 반환 값 | 성능 |
|--------|------|------|---------|------|
| **push()** | 끝 | 추가 | 새 배열 길이 | 빠름 |
| **pop()** | 끝 | 제거 | 제거된 요소 | 빠름 |
| **unshift()** | 앞 | 추가 | 새 배열 길이 | 느림 (비권장) |
| **shift()** | 앞 | 제거 | 제거된 요소 | 느림 (비권장) |

**주의사항:**
- `unshift()`와 `shift()`는 모든 요소를 이동시켜야 하므로 성능이 떨어짐
- 가능하면 `push()`와 `pop()` 사용 권장

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 배열 메서드 섹션

---

## 7. Array Helper Methods

**파일명**: `07-array-helper-methods.html`

forEach와 map 메서드를 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 콜백 함수 예시 1 (인라인 함수) ===
    const numbers = [1, 2, 3]
    numbers.forEach(function (num) {
      console.log(num)  // 1, 2, 3
    })

    // === 콜백 함수 예시 2 (변수에 저장) ===
    const callBackFunction = function (num) {
      console.log(num)
    }
    numbers.forEach(callBackFunction)  // 1, 2, 3

    // === forEach ===
    const names = ['Alice', 'Bella', 'Cathy']

    // 일반 함수 표기
    names.forEach(function (name) {
      console.log(name)  // 'Alice', 'Bella', 'Cathy'
    })

    // 화살표 함수 표기 (권장)
    names.forEach((name) => {
      console.log(name)  // 'Alice', 'Bella', 'Cathy'
    })

    // forEach의 매개변수 활용
    const result = names.forEach(function (name, index, array) {
      console.log(`${name} / ${index} / ${array}`)
      return 'aaa'  // forEach는 반환 값을 무시
    })
    console.log(result)  // undefined (forEach는 항상 undefined 반환)

    // === map ===
    // 1. for...of와 비교
    const persons = [
      { name: 'Alice', age: 20 },
      { name: 'Bella', age: 21 }
    ]

    // 1.1 for...of 방식
    let result1 = []
    for (const person of persons) {
      result1.push(person.name)
    }
    console.log(result1)  // ['Alice', 'Bella']

    // 1.2 map 방식 (더 간결하고 의도가 명확)
    const result2 = persons.map(function (person) {
      return person.name
    })
    console.log(result2)  // ['Alice', 'Bella']

    // 2. 화살표 함수 표기
    const result3 = names.map(function (name) {
      return name.length
    })

    const result4 = names.map((name) => {
      return name.length
    })
    console.log(result3) // [5, 5, 5]
    console.log(result4) // [5, 5, 5]

    // 3. 커스텀 콜백 함수
    const myCallbackFunc = function (number) {
      return number * 2
    }
    const doubleNumber = numbers.map(myCallbackFunc)
    console.log(doubleNumber) // [2, 4, 6]
  </script>
</body>
</html>
```

**핵심 개념:**

| 메서드 | 기능 | 반환 값 | 사용 목적 |
|--------|------|---------|-----------|
| **forEach** | 배열 각 요소에 함수 실행 | undefined | 반복 작업 수행 |
| **map** | 배열 각 요소에 함수 실행 | 새 배열 | 변환된 새 배열 생성 |

**주의사항:**
- `forEach`는 반환 값이 없으므로 변환 작업에는 부적합
- `map`은 원본 배열을 변경하지 않고 새 배열을 반환 (불변성)

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - Array Helper Method, forEach, map 섹션

---

## 8. 배열 순회

**파일명**: `08-array-iteration.html`

for loop, for...of, forEach의 차이를 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 배열 순회 종합 ===
    const names = ['Alice', 'Bella', 'Cathy']

    // === 1. for loop ===
    // 인덱스를 이용한 접근
    for (let idx = 0; idx < names.length; idx++) {
      console.log(names[idx])  // 'Alice', 'Bella', 'Cathy'
    }

    // === 2. for...of ===
    // 값에 직접 접근
    for (const name of names) {
      console.log(name)  // 'Alice', 'Bella', 'Cathy'
    }

    // === 3. forEach (권장) ===
    // 콜백 함수로 각 요소 처리
    names.forEach((name) => {
      console.log(name)  // 'Alice', 'Bella', 'Cathy'
    })
  </script>
</body>
</html>
```

**배열 순회 방법 비교:**

| 방식 | 특징 | break/continue | 권장도 |
|------|------|----------------|--------|
| **for loop** | 인덱스 제어 가능 | 가능 | 인덱스 필요 시 |
| **for...of** | 값에 직접 접근 | 가능 | 간단한 순회 |
| **forEach** | 콜백 함수 사용 | 불가능 | 배열 조작 시 권장 |

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 배열 순회 종합 섹션

---

## 9. 배열과 전개 구문

**파일명**: `09-array-with-spread-syntax.html`

배열에서 전개 구문을 사용하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 배열 복사 및 결합 (전개 구문 사용) ===
    let parts = ['어깨', '무릎']
    let lyrics = ['머리', ...parts, '발']
    // parts 배열을 펼쳐서 lyrics에 삽입

    console.log(lyrics) // ['머리', '어깨', '무릎', '발']
  </script>
</body>
</html>
```

**핵심 개념:**
- **전개 구문 (`...`)**: 배열을 펼쳐서 개별 요소로 확장
- 배열 복사, 배열 결합, 배열 중간 삽입 등에 유용
- 원본 배열은 변경되지 않음 (새 배열 생성)

**주의사항:**
- 전개 구문은 **얕은 복사**만 수행
- 중첩 배열이나 객체는 참조가 복사됨

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 배열 with 전개 구문 섹션

---

## 10. 참고: 클래스

**파일명**: `99_1-class.html`

클래스를 사용한 객체 생성 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 클래스 정의 ===
    class Member {
      // 생성자: new로 객체 생성 시 자동 호출
      constructor(name, age) {
        this.name = name
        this.age = age
      }
      
      // 메서드 정의
      sayHi() {
        console.log(`Hi, I am ${this.name}`)
      }
    }

    // === 클래스로 객체 생성 ===
    const member1 = new Member('Alice', 20)

    console.log(member1)      // Member { name: 'Alice', age: 20 }
    console.log(member1.name) // 'Alice'
    member1.sayHi()           // 'Hi, I am Alice'

    // === [참고] 생성자 함수 표현 방식 (과거) ===
    // function Member(name, age) {
    //   this.name = name
    //   this.age = age
    //   this.sayHi = function () {
    //     console.log(`Hi, I am ${this.name}`)
    //   }
    // }
  </script>
</body>
</html>
```

**핵심 개념:**
- **클래스**: 객체를 생성하기 위한 템플릿 (붕어빵 틀)
- **constructor**: 객체 생성 시 자동 호출되는 생성자 메서드
- **new 연산자**: 클래스로부터 새 객체 인스턴스 생성
- **메서드**: 클래스 내부에 정의된 함수

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 참고 > 클래스 섹션

---

## 11. 참고: 콜백 함수

**파일명**: `99_2-callback.html`

콜백 함수의 유연성을 이해하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    const numbers = [1, 2, 3, 4];

    // === 콜백 함수 1: 각 요소를 두 배로 만드는 함수 ===
    const double = function (number) {
      return number * 2;
    };

    // === 콜백 함수 2: 각 요소를 제곱하는 함수 ===
    const square = function (number) {
      return number * number;
    };

    // === 1. double 콜백 사용 ===
    const doubledNumbers = numbers.map(double);
    console.log(doubledNumbers); // [2, 4, 6, 8]

    // === 2. square 콜백 사용 ===
    const squaredNumbers = numbers.map(square);
    console.log(squaredNumbers); // [1, 4, 9, 16]

    // 같은 map 메서드지만 어떤 콜백 함수를 전달하느냐에 따라 결과가 달라짐
  </script>
</body>
</html>
```

**핵심 개념:**
- **콜백 함수의 유연성**: 같은 메서드에 다른 콜백 함수를 전달하여 다양한 동작 수행
- 함수를 인자로 전달함으로써 코드의 재사용성과 유연성 향상

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 참고 > 콜백 함수의 이점 섹션

---

## 12. 참고: 비동기

**파일명**: `99_3-asynchronous.html`

비동기 처리의 기본 개념을 이해하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === 비동기적 측면 ===
    console.log('a')

    // setTimeout: 지정된 시간(3000ms = 3초) 후에 콜백 함수 실행
    setTimeout(() => {
      console.log('b')
    }, 3000)

    console.log('c')

    // === 출력 결과 ===
    // a (즉시 실행)
    // c (즉시 실행)
    // b (3초 후 실행)

    // setTimeout은 비동기로 실행되므로 
    // 기다리지 않고 다음 코드(console.log('c'))를 바로 실행
  </script>
</body>
</html>
```

**핵심 개념:**
- **비동기 처리**: 코드가 순차적으로 실행되지 않고, 특정 작업을 기다리지 않고 다음 코드를 실행
- **setTimeout**: 지정된 시간 후에 콜백 함수를 실행하는 비동기 함수

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 참고 > 콜백 함수의 이점 > 비동기적 측면 섹션

---

## 13. 참고: forEach break

**파일명**: `99_4-break-foreach.html`

forEach에서 break를 대체하는 some과 every 메서드 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    const array = [1, 2, 3, 4, 5]

    // === some 메서드 ===
    // 배열의 요소 중 적어도 하나라도 콜백 함수를 통과하는지 테스트
    // 콜백 함수가 true를 반환하면 즉시 순회 중단하고 true 반환
    const isEvenNumber = array.some(function (element) {
      return element % 2 === 0
    })

    console.log(isEvenNumber) // true (2가 짝수이므로)

    // === every 메서드 ===
    // 배열의 모든 요소가 콜백 함수를 통과하는지 테스트
    // 콜백 함수가 false를 반환하면 즉시 순회 중단하고 false 반환
    const isAllEvenNumber = array.every(function (element) {
      return element % 2 === 0
    })

    console.log(isAllEvenNumber) // false (1이 홀수이므로)

    ////////////////////////////////////////////////

    // === forEach를 break 하는 대안 ===
    // some과 every의 특징을 이용하여 마치 forEach에서 break를 사용하는 것처럼 구현
    const names = ['Alice', 'Bella', 'Cathy']

    // === 1. some 활용 ===
    // 콜백 함수가 true를 반환하면 즉시 중단
    names.some(function (name) {
      console.log(name) // 'Alice', 'Bella'
      if (name === 'Bella') {
        return true  // true를 반환하면 순회 중단
      }
      return false
    })

    // === 2. every 활용 ===
    // 콜백 함수가 false를 반환하면 즉시 중단
    names.every(function (name) {
      console.log(name) // 'Alice', 'Bella'
      if (name === 'Bella') {
        return false  // false를 반환하면 순회 중단
      }
      return true
    })
  </script>
</body>
</html>
```

**핵심 개념:**

| 메서드 | 동작 | 중단 조건 | 반환 값 |
|--------|------|-----------|---------|
| **some** | 하나라도 조건 만족 시 true | true 반환 시 | true/false |
| **every** | 모두 조건 만족 시 true | false 반환 시 | true/false |

**참고 교안**: `JavaScript_Basic_Syntax_02.md` - 참고 > forEach에서 break 사용하기 섹션

---

## 14. 참고: reduce 메서드

**파일명**: `99_5-reduce.html`

reduce 메서드의 다양한 활용법을 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // === reduce 메서드 ===
    // https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
    // 배열의 각 요소에 대해 콜백 함수를 실행하고, 하나의 결과값을 반환
    // 배열을 원하는 특정 형태의 값으로 변환 (숫자, 문자열, 객체, 배열)

    /*
      구조: array.reduce(callBackFunction, initialValue)
      
      - callBackFunction: 배열을 처리할 콜백함수
        - accumulator (acc, 필수): 누적값, 이전 콜백이 return한 값
        - currentValue (cur, 필수): 현재 처리 중인 요소
        - currentIndex (idx, 선택): 현재 요소의 인덱스
        - array (arr, 선택): reduce를 호출한 원본 배열
      - initialValue: 누적을 시작할 초기값
    */

    // === 예시 1. 숫자 합계 구하기 ===
    const numbers = [1, 2, 3, 4, 5];

    const sum = numbers.reduce((accumulator, current) => {
      console.log(`누적값(acc): ${accumulator}, 현재값(cur): ${current}`);
      return accumulator + current;
    }, 0);  // 초기값 0

    console.log('최종 결과:', sum);  // 15
    // 0 + 1 = 1
    // 1 + 2 = 3
    // 3 + 3 = 6
    // 6 + 4 = 10
    // 10 + 5 = 15

    // === 예시 2. 배열 → 객체로 변환 ===
    // '이름'을 key로, '등장 횟수'를 value로 하는 객체를 만들자!
    const names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'];

    const nameCounts = names.reduce((countMap, name) => {
      // countMap[name]이 없으면 0, 있으면 그 값에 1을 더함
      countMap[name] = (countMap[name] ?? 0) + 1;

      return countMap;  // 수정된 객체를 다음 순회에 반환
    }, {});  // 초기값은 빈 객체 {}

    console.log(nameCounts);  // {Alice: 3, Bob: 2, Charlie: 1}

    // === 예시 3. 배열 → 배열 (map과 filter 한 번에 적용) ===
    // 체이닝으로 한다면?
    // const result = nums.filter(n => n % 2 === 0).map(n => n * 2);

    const nums = [1, 2, 3, 4, 5];
    const result = nums.reduce((newArray, current) => {
      // 짝수인지 검사 (filter 역할)
      if (current % 2 === 0) {
        // 2배를 해서 newArray에 추가 (map 역할)
        newArray.push(current * 2);
      }

      // 다음 순회에 수정된 배열을 반환
      return newArray;
    }, []); // 초기값은 빈 배열 []

    console.log(result); // [4, 8]
  </script>
</body>
</html>
```

**핵심 개념:**
- **reduce**: 배열을 순회하며 하나의 값으로 **축약(reduce)**
- **accumulator**: 이전 콜백의 반환 값이 누적되는 변수
- **initialValue**: 누적을 시작할 초기값 (첫 번째 accumulator 값)

**활용 예시:**
1. 숫자 합계/평균 계산
2. 배열 → 객체 변환 (그룹화)
3. filter + map 동시 적용
4. 중첩 배열 평탄화

**참고 자료**: [MDN reduce 문서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

---

## 15. 실습 문제

### 문제 1: 학생 평균 점수 계산

**파일명**: `01.html` / `01_answer.html`

forEach를 사용하여 전체 학생의 평균 점수를 계산하는 문제

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // forEach를 사용하여 전체 학생의 평균 점수를 계산하세요.
    const students = [
      { name: '김철수', score: 85 },
      { name: '이영희', score: 92 },
      { name: '박민수', score: 78 },
      { name: '정지원', score: 90 }
    ]

    // === 정답 ===
    let numberOfStudent = students.length
    let sumOfScores = 0

    students.forEach((student) => {
      sumOfScores += student.score
    })

    const result = sumOfScores / numberOfStudent
    console.log(result)  // 86.25
  </script>
</body>
</html>
```

**풀이 포인트:**
1. `forEach`로 배열 순회
2. 각 학생의 점수를 `sumOfScores`에 누적
3. 총합을 학생 수로 나누어 평균 계산

---

### 문제 2: 짝수/홀수 처리

**파일명**: `02.html` / `02_answer.html`

forEach를 사용하여 짝수는 2배, 홀수는 3을 더하는 문제

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // forEach를 사용하여 다음 작업을 수행하세요:
    // 1. 짝수는 2배로 증가
    // 2. 홀수는 3을 더하기
    // 결과를 새 배열에 저장
    const numbers = [1, 2, 3, 4, 5]
    
    // === 정답 ===
    const result = []

    numbers.forEach((number) => {
      // 1. 짝수면 2배
      if (number % 2 === 0) {
        result.push(number * 2)
      // 2. 홀수면 3을 더함
      } else {
        result.push(number + 3)
      }
    })
    
    console.log(result)  // [4, 4, 6, 8, 8]
  </script>
</body>
</html>
```

**풀이 포인트:**
1. 빈 배열 `result` 준비
2. `forEach`로 순회하며 조건 확인
3. 짝수/홀수에 따라 다른 연산 후 `push`

---

### 문제 3: 도서관 시스템

**파일명**: `03.html` / `03_answer.html`

forEach와 reduce를 사용하여 도서 관리 시스템 구현

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    const library = {
      books: [
        { id: 1, title: '자바스크립트 완벽 가이드', status: 'available' },
        { id: 2, title: '파이썬 기초', status: 'borrowed' },
        { id: 3, title: 'HTML/CSS 입문', status: 'available' }
      ],
      borrowHistory: [
        { bookId: 2, userId: 'user1', date: '2024-10-20' },
        { bookId: 1, userId: 'user2', date: '2024-10-15' },
        { bookId: 1, userId: 'user2', date: '2024-10-23' }
      ]
    }

    // forEach를 사용하여 다음을 구현하세요:
    // 1. 현재 대출 가능한 도서 목록
    // 2. 특정 사용자(user2)의 대출 이력

    // === 정답 1: 대출 가능 도서 ===
    const availableBooks = []
    library.books.forEach((book) => {
      if (book.status === 'available') {
        availableBooks.push(book.title)
      }
    })
    console.log(availableBooks)
    // ['자바스크립트 완벽 가이드', 'HTML/CSS 입문']

    // === 정답 2: user2 대출 이력 (reduce 활용) ===
    const user2History = library.borrowHistory.reduce((historyList, record) => {
      if (record.userId === 'user2') {
        // bookId로 책 정보 찾기
        const book = library.books.find(b => b.id === record.bookId);
        
        historyList.push({
          title: book ? book.title : '알 수 없는 책',
          date: record.date
        });
      }

      return historyList;
    }, []);
    
    console.log(user2History)
    // [
    //   { title: '자바스크립트 완벽 가이드', date: '2024-10-15' },
    //   { title: '자바스크립트 완벽 가이드', date: '2024-10-23' }
    // ]
  </script>
</body>
</html>
```

**풀이 포인트:**
1. **대출 가능 도서**: `forEach`로 `status === 'available'` 필터링
2. **user2 대출 이력**: 
   - `reduce`로 빈 배열에서 시작
   - `userId === 'user2'` 조건 확인
   - `find`로 bookId에 해당하는 책 정보 찾기
   - 제목과 날짜를 객체로 만들어 배열에 추가

---

## 실습 순서 추천

1. **01-object.html**: 객체 기본 다루기
2. **02-this-keyword.html**: this 이해하기
3. **05-array.html**: 배열 기본
4. **06-array-method.html**: 배열 메서드
5. **07-array-helper-methods.html**: forEach, map
6. **08-array-iteration.html**: 배열 순회 비교
7. **03-extra-object-syntax.html**: 고급 객체 문법
8. **04-json.html**: JSON 변환
9. **09-array-with-spread-syntax.html**: 전개 구문
10. **99_1-class.html**: 클래스
11. **99_2-callback.html**: 콜백 함수 유연성
12. **99_3-asynchronous.html**: 비동기 기초
13. **99_4-break-foreach.html**: some, every
14. **99_5-reduce.html**: reduce 활용
15. **01~03.html**: 실습 문제 풀이

---

## 핵심 메서드 요약표

| 메서드 | 기능 | 반환 값 | 원본 수정 |
|--------|------|---------|-----------|
| **push()** | 끝에 추가 | 새 길이 | O |
| **pop()** | 끝 제거 | 제거된 요소 | O |
| **shift()** | 앞 제거 | 제거된 요소 | O |
| **unshift()** | 앞에 추가 | 새 길이 | O |
| **forEach()** | 각 요소에 함수 실행 | undefined | X |
| **map()** | 각 요소 변환 | 새 배열 | X |
| **filter()** | 조건 만족 요소만 | 새 배열 | X |
| **reduce()** | 하나의 값으로 축약 | 누적 값 | X |
| **some()** | 하나라도 조건 만족 | true/false | X |
| **every()** | 모두 조건 만족 | true/false | X |
| **find()** | 조건 만족 첫 요소 | 요소 또는 undefined | X |

---

## 주의사항 체크리스트

- [ ] `var` 사용하지 않기 (let, const만 사용)
- [ ] 객체 속성 접근 시 띄어쓰기 있으면 대괄호 표기법
- [ ] `in` 연산자 대신 `hasOwnProperty()` 사용 권장
- [ ] 중첩 함수에서 this 사용 시 화살표 함수 권장
- [ ] Optional Chaining은 필수가 아닌 속성에만 사용
- [ ] `forEach`는 반환 값이 없음 (undefined)
- [ ] `map`은 새 배열 반환 (원본 불변)
- [ ] `unshift`, `shift`는 성능상 비권장
- [ ] 전개 구문은 얕은 복사만 수행
- [ ] `reduce` 사용 시 초기값 설정 필수

---

**작성일**: 2024  
**참고 교안**: SSAFY JavaScript_Basic_Syntax_02.md

