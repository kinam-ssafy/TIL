# JavaScript Basic Syntax 01

## 📚 목차

1. [데이터 타입](#데이터-타입)
2. [원시 자료형](#원시-자료형)
3. [연산자](#연산자)
4. [조건문](#조건문)
5. [반복문](#반복문)
6. [함수](#함수)
7. [참고](#참고)
8. [실습 문제](#실습-문제)
9. [핵심 정리](#핵심-정리)

---

## 🎯 학습 목표

장바구니 총액을 계산하고, 특정 금액이 넘으면 '무료 배송'을 적용하는 기능은 어떻게 만들까요?

1. 상품 정보를 데이터로 담고 연산자로 가격을 계산한 뒤, 반복문으로 모든 상품의 가격을 합산해야 합니다.

2. 마지막으로 조건문을 통해 무료 배송 여부를 판단하고 이 모든 과정을 하나의 함수로 묶어 완성할 수 있습니다.

하나의 기능을 만드는 데 필요한 **'데이터'**, **'연산자'**, **'반복문'**, **'조건문'**, **'함수'** 등 자바스크립트의 가장 기본적인 문법을 학습합니다.

---

## 데이터 타입

### 원시 자료형 (Primitive type)

- 값(value) 자체가 변수에 직접 저장되는 자료형
- **불변(immutable)**이며, 변수 간 할당 시 값이 복사
- **종류**: Number, String, Boolean, null, undefined

### 참조 자료형 (Reference type)

- 데이터가 저장된 메모리의 주소가 변수에 저장되는 자료형
- **가변(Mutable)**이며, 변수 간 할당 시 주소가 복사
- **종류**: Objects (Object, Array, Function)

> **⚠️ 주의**: 참조 자료형은 주소를 복사하므로 복사본을 수정하면 원본의 값도 함께 변경될 수 있어 주의해야 합니다.

> **💡 TIP**: 값이 불변이라는 것은 값의 일부를 직접 수정할 수 없다는 의미입니다.
> 예: `let str = 'ssafy'; str[0] = 'S';` 처럼 할당하는 것은 불가능

---

## 원시 자료형

### 자동 형변환

JavaScript는 조건문에서 값을 자동으로 boolean으로 변환합니다.

| 데이터 타입 | false | true |
|------------|-------|------|
| **undefined** | 항상 false | - |
| **null** | 항상 false | - |
| **Number** | 0, -0, NaN | 나머지 모든 경우 |
| **String** | '' (빈 문자열) | 나머지 모든 경우 |

---

## 연산자

### 연산자 종류

1. **할당 연산자**
2. **증가 & 감소 연산자**
3. **비교 연산자**
4. **동등 연산자**
5. **일치 연산자**
6. **논리 연산자**

### 1. 할당 연산자

오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

#### 단축 연산자
`X = X + 1`을 `X += 1`처럼 코드를 짧게 줄여주는 연산자

```javascript
let a = 0

a += 10
console.log(a)  // 10

a -= 3
console.log(a)  // 7

a *= 10
console.log(a)  // 70

a %= 7
console.log(a)  // 0
```

### 2. 증가 & 감소 연산자

#### 증가 연산자 (`++`)
피연산자를 증가(1을 더함)시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환

#### 감소 연산자 (`--`)
피연산자를 감소(1을 뺌)시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환

```javascript
let x = 3
const y = x++
console.log(x, y)  // 4 3

let a = 3
const b = ++a
console.log(a, b)  // 4 4
```

> **💡 권장**: 코드의 가독성을 위해 `a += 1`, `a -= 1`과 같이 더 명시적인 표현을 권장

### 3. 비교 연산자

피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과 값을 boolean으로 반환하는 연산자

```javascript
3 > 2       // true
3 < 2       // false
'A' < 'B'   // true
'Z' < 'a'   // true
'가' < '나'  // true
```

### 4. 동등 연산자 (`==`)

두 피연산자가 같은 값으로 평가되는지 비교한 후 boolean 값을 반환

- **'암묵적 타입 변환'**을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

```javascript
console.log(1 == 1)           // true
console.log('hello' == 'hello')  // true
console.log('1' == 1)         // true
console.log(0 == false)       // true
```

> **⚠️ 주의**: `0 == false`, `'' == []`가 true가 되는 등, 직관과 다른 암묵적 타입 변환이 일어나니 주의하세요.

> **💡 TIP**: 내용이 같아도 다른 객체이면 false입니다. `[1] == [1]`은 false이니 주의하세요.

### 5. 일치 연산자 (`===`)

두 피연산자의 **값과 타입이 모두 같은 경우** true를 반환

- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
- **특별한 경우를 제외하고는 예측하지 못한 결과를 방지하기 위해 일치 연산자(`===`) 사용을 권장**

```javascript
console.log(1 === 1)             // true
console.log('hello' === 'hello')  // true
console.log('1' === 1)           // false
console.log(0 === false)         // false
```

### 6. 논리 연산자

#### AND 연산 (`&&`)
```javascript
true && false  // false
true && true   // true
```

#### OR 연산 (`||`)
```javascript
false || false  // false
true || false   // true
```

#### NOT 연산 (`!`)
```javascript
!true   // false
!false  // true
```

#### 단축 평가
```javascript
1 && 0    // 0
0 && 4    // 0
4 && 7    // 7
```

---

## 조건문

### if 문

조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

```javascript
const name = 'customer'

if (name === 'admin') {
  console.log('관리자님 환영해요')
} else if (name === 'customer') {
  console.log('고객님 환영해요')
} else {
  console.log(`반갑습니다. ${name}님`)
}
```

### 삼항 연산자

간단한 조건부 로직을 간결하게 표현할 때 유용

**구조**: `condition ? expression1 : expression2`

- `condition`: 평가할 조건 (true 또는 false로 평가)
- `expression1`: 조건이 true일 경우 반환할 값 또는 표현식
- `expression2`: 조건이 false일 경우 반환할 값 또는 표현식

```javascript
const age = 20
const message = (age >= 18) ? '성인' : '미성년자'
console.log(message)  // 성인
```

> **💡 주의**: 복잡한 로직이나 대다수의 경우에는 가독성이 떨어질 수 있으므로 적절한 상황에서만 사용할 것

---

## 반복문

### 반복문 종류

1. **while**
2. **for**
3. **for...in**
4. **for...of**

### 1. while 반복문

조건문이 참이면 문장을 계속해서 수행

```javascript
let i = 0

while (i < 6) {
  console.log(i)
  i += 1
}
```

### 2. for 반복문

특정한 조건이 거짓으로 판별될 때까지 반복

**구조**: `for ([초기문]; [조건문]; [증감문]) { ... }`

```javascript
for (let i = 0; i < 6; i++) {
  console.log(i)
}
```

#### for 동작 원리

```javascript
for (let i = 0; i < 6; i++) {
  console.log(i)
}
```

1. 초기문: `let i = 0` 실행 (최초 1회만)
2. 조건문: `i < 6` 평가 → true면 실행
3. 코드 블록 실행: `console.log(i)`
4. 증감문: `i++` 실행
5. 2번으로 돌아가서 반복
6. 조건문이 false가 되면 반복 종료

### 3. for...in 반복문

객체의 **열거 가능한 속성(키)**에 대해 반복

```javascript
const object = {
  a: 'apple',
  b: 'banana'
}

for (const property in object) {
  console.log(property)        // a, b
  console.log(object[property]) // apple, banana
}
```

> **⚠️ 주의**: 배열에는 `for...in` 사용을 권장하지 않습니다.
> - 배열에 사용하면 인덱스를 문자열로 반환
> - 순서를 보장하지 않음

### 4. for...of 반복문

반복 가능한 객체(배열, 문자열 등)의 **값(value)**을 반복

```javascript
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
  console.log(number)  // 0, 1, 2, 3
}
```

> **💡 참고**: 객체는 반복 가능하지 않으므로 `for...of`를 직접 사용할 수 없습니다.

### for...in vs for...of

| 구분 | for...in | for...of |
|------|----------|----------|
| **대상** | 객체의 키(key) | 반복 가능한 객체의 값(value) |
| **반환** | 속성 이름(key) | 속성 값(value) |
| **배열 사용** | 권장하지 않음 | 권장 |
| **객체 사용** | 권장 | 사용 불가 |

---

## 함수

### 함수 정의

#### 1. 함수 선언식 (Function Declaration)

```javascript
function funcName() {
  // statements
}

function add(num1, num2) {
  return num1 + num2
}

add(2, 7)  // 9
```

- `function` 키워드 사용
- **호이스팅(hoisting)**의 영향을 받음

#### 2. 함수 표현식 (Function Expression)

```javascript
const funcName = function () {
  // statements
}

const sub = function (num1, num2) {
  return num1 - num2
}

sub(7, 2)  // 5
```

- 변수에 함수를 할당
- 호이스팅되지 않아 코드의 예측 가능성이 높아져 **사용이 권장됨**

#### 3. 기본 함수 매개변수 (Default Function Parameter)

인자가 전달되지 않을 경우를 대비해 기본값을 설정

```javascript
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

greeting()  // Hi Anonymous
```

### 화살표 함수 표현식 (Arrow Function Expression)

함수 표현식의 간결한 표현법

**구조**: `const arrow = (parameter) => { statements }`

```javascript
const arrow = function (name) {
  return `hello, ${name}`
}

// 1. function 키워드 제거 후 화살표 작성
const arrow = (name) => { return `hello, ${name}` }

// 2. 인자가 1개일 경우 () 생략 가능
const arrow = name => { return `hello, ${name}` }

// 3. 함수 본문이 return을 포함한 표현식 1개일 경우 {} & return 생략 가능
const arrow = name => `hello, ${name}`
```

### 매개변수

#### 1. 나머지 매개변수 (Rest Parameters)

임의의 수의 인자를 **배열**로 받음 (`...` 사용)

```javascript
const myFunc = function (param1, param2, ...restParams) {
  return [param1, param2, restParams]
}

myFunc(1, 2, 3, 4, 5)  // [1, 2, [3, 4, 5]]
myFunc(1, 2)           // [1, 2, []]
```

#### 2. 전개 구문 (Spread Syntax)

배열이나 객체를 펼쳐서 개별 요소로 확장 (`...` 사용)

```javascript
const myFunc = function (x, y, z) {
  return x + y + z
}

const numbers = [1, 2, 3]

myFunc(...numbers)  // 6
// myFunc(1, 2, 3)과 동일
```

#### 나머지 매개변수 vs 전개 구문

```javascript
// 나머지 매개변수: 여러 개를 하나로 묶음
const func1 = function (...params) {
  console.log(params)  // [1, 2, 3]
}
func1(1, 2, 3)

// 전개 구문: 하나를 여러 개로 펼침
const func2 = function (x, y, z) {
  console.log(x, y, z)  // 1 2 3
}
const array = [1, 2, 3]
func2(...array)
```

---

## 참고

### NaN 예시

**NaN**: "Not a Number"를 나타내는 값

```javascript
console.log(Number(undefined))  // NaN
console.log(Number('abc'))      // NaN
console.log('a' / 3)            // NaN
```

### null & undefined

#### '값이 없음'에 대한 표현이 null과 undefined 2가지인 이유

**1. 역사적 맥락**
- JavaScript가 처음 만들어질 때, `null`은 '객체가 없음'을 나타내기 위해 도입
- `undefined`는 나중에 추가되어 '값이 할당되지 않음'을 나타내게 됨

**2. typeof null의 결과가 "object"인 이유**
- 초기 버전에서 값의 타입을 나타내는 데 32비트 시스템을 사용
- 타입 태그로 하위 3비트를 사용했는데, '000'은 객체를 나타냄
- null은 모든 비트가 0인 특별한 값(NULL 포인터)으로 표현되었는데, 하필 객체 타입을 나타내는 태그 또한 000이었기 때문에 null을 객체로 잘못 판별하게 됨

```javascript
typeof null       // "object"
typeof undefined  // "undefined"
```

**3. ECMAScript의 표준화**
- ECMAScript 명세에서는 null을 원시 자료형으로 정의
- 그러나 typeof null의 결과는 역사적인 이유로 "object"를 유지
- ECMAScript 5 개발 중 이 문제를 수정하려는 시도가 있었지만, 이미 `typeof null === 'object'`라는 전제하에 만들어진 수많은 웹 사이트와의 하위 호환성 문제 때문에 수정되지 못함

```javascript
null == undefined   // true
null === undefined  // false
```

### 화살표 함수 심화

#### 1. 인자가 없다면 `()` 또는 `_`로 표시 가능

```javascript
const noArgs1 = () => 'No args'
const noArgs2 = _ => 'No args'
```

#### 2. 객체를 return 한다면

**2-1. return을 명시적으로 작성해야 함**
```javascript
const returnObject1 = () => { return { key: 'value' } }
```

**2-2. return을 작성하지 않으려면 객체를 소괄호로 감싸야 함**
```javascript
const returnObject2 = () => ({ key: 'value' })
```

---

## 실습 문제

### 연습 문제

1. 다양한 연산자
2. 기초 문법 디버깅
3. 조건문과 변수 선언
4. 연산자와 제어문
5. 제어문
6. 배열 순회
7. 배열과 객체 순회
8. 반복문과 제어문
9. 기초 문법 디버깅 - 반복문

---

## 확인 문제

### 문제

**1. 다음 중 원시 자료형(Primitive type)이 아닌 것은?**
- a) Number
- b) String
- c) Array ✅
- d) undefined

**2. null과 undefined에 대한 설명으로 틀린 것은?**
- a) null은 의도적인 '값 없음'을 의미한다.
- b) undefined는 값이 할당되지 않았음을 의미한다.
- c) typeof null의 결과는 'null'이다. ✅
- d) null == undefined는 true이다.

**3. `==`와 `===` 연산자의 주요 차이점은?**
- a) 연산 속도
- b) 타입 변환 여부 ✅
- c) 반환 값의 타입
- d) 객체 비교 가능 여부

**4. 논리 연산자 중 단축 평가를 활용하는 코드는?**
- a) true && false
- b) 0 && 3 ✅
- c) 4 || 7
- d) !true

**5. 삼항 연산자에 대한 설명으로 올바른 것은?**
- a) 세 개의 피연산자를 가진다. ✅
- b) 항상 if문보다 가독성이 좋다.
- c) 조건이 거짓일 때 첫 번째 표현식을 반환한다.
- d) 반복문 내에서는 사용할 수 없다.

**6. 객체의 '키(key)'를 순회하기에 가장 적합한 반복문은?**
- a) for
- b) while
- c) for...in ✅
- d) for...of

**7. 배열의 '값(value)'을 순회하는 반복문은?**
- a) for
- b) while
- c) for...in
- d) for...of ✅

**8. 함수 선언식과 함수 표현식의 가장 큰 차이점은?**
- a) 매개변수 개수
- b) 반환 값 존재 여부
- c) 호이스팅 발생 여부 ✅
- d) 익명 함수 사용 가능 여부

**9. 임의의 수의 인자를 배열로 받는 매개변수 문법은?**
- a) 기본 매개변수
- b) 가변 매개변수
- c) 나머지 매개변수 ✅
- d) 전개 구문

**10. 화살표 함수로 옳게 축약된 것은?**
- a) `const arrow = name => { 'hello, ' + name }`
- b) `const arrow = name => 'hello, ' + name` ✅
- c) `const arrow = (name) => return 'hello, ' + name`
- d) `const arrow = => 'hello, ' + name`

### 정답 해설

**1. Array**
- Array는 객체(Object)에 속하는 참조 자료형이므로, 원시 자료형이 아닙니다.

**2. typeof null의 결과는 'null'이다**
- JavaScript 초기 버전의 오류로 인해 `typeof null`은 'object'를 반환합니다.

**3. 타입 변환 여부**
- `==`는 타입을 변환하여 비교하지만, `===`는 타입까지 엄격하게 비교합니다.

**4. 0 && 3**
- `&&` 연산자는 첫 피연산자가 참일 경우 뒤를 쳐다보지 않고 그대로 중지합니다.

**5. 세 개의 피연산자를 가진다**
- `조건 ? 참일때_표현식 : 거짓일때_표현식` 구조로 3개의 피연산자를 사용합니다.

**6. for...in**
- `for...in`은 객체의 열거 가능한 속성(키)에 대해 반복하는 데 사용됩니다.

**7. for...of**
- `for...of`는 배열과 같은 반복 가능한 객체의 각 요소(값)를 순회하는 데 사용됩니다.

**8. 호이스팅 발생 여부**
- 함수 선언식은 호이스팅되어 선언 전에 호출 가능하지만, 함수 표현식은 그렇지 않습니다.

**9. 나머지 매개변수**
- 나머지 매개변수(`...rest`)는 정해지지 않은 수의 인자들을 배열로 모아줍니다.

**10. const arrow = name => 'hello, ' + name**
- 본문이 한 줄의 표현식이면 중괄호와 return을 동시에 생략할 수 있습니다.

---

## 핵심 정리

### 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| **원시 자료형** | 값이 직접 저장되는 불변 데이터 | Number, String, Boolean 등 |
| **일치 연산자 (===)** | 값과 타입이 모두 같은지 비교 | `'1' === 1 // false` |
| **for...of 반복문** | 반복 가능한 객체의 값을 반복 | `for (const item of arr) { ... }` |
| **함수 표현식** | 변수에 함수를 할당하여 정의 | `const sub = function () { }` |
| **화살표 함수** | 함수 표현식의 간결한 표현법 | `const arrow = () => { }` |
| **나머지 매개변수** | 여러 인자를 배열로 받는 매개변수 | `function (...args) { }` |
| **전개 구문 (...)** | 반복 가능한 항목을 펼치는 문법 | `myFunc(...numbers)` |

### 요약 및 정리

#### JavaScript의 데이터 타입은 크게 두 가지

**원시 자료형 (Primitive type)**
- 변수에 값이 직접 저장되는 자료형
- Number, String, Boolean, null, undefined가 여기에 해당
- 데이터가 불변(immutable)이며, 다른 변수에 할당할 때 값이 복사

**참조 자료형 (Reference type)**
- 객체의 메모리 주소가 변수에 저장되는 자료형
- Object, Array, Function 등이 여기에 해당
- 데이터가 가변(mutable)이며, 다른 변수에 할당할 때 주소가 복사되어 원본과 사본이 서로 영향을 줌

#### 원시 자료형의 종류

- **Number**: 정수와 실수를 모두 표현하는 숫자 자료형
- **String**: 텍스트 데이터를 나타내며, `+` 연산자로 문자열을 결합 가능
- **템플릿 리터럴**: 백틱(\`)을 사용해 변수를 `${}` 형태로 문자열에 쉽게 삽입할 수 있는 방식
- **null & undefined**:
  - null은 개발자가 의도적으로 '값이 없음'을 나타낼 때 사용
  - undefined는 '값이 할당되지 않음'을 시스템이 나타낼 때 사용
- **Boolean**: true와 false를 나타내는 논리 자료형

#### 비교 연산자

**동등 연산자 (==)**
- 두 피연산자의 타입을 일치시킨 후 값을 비교
- 이 과정에서 예측하기 어려운 결과가 나올 수 있어 사용 시 주의가 필요

**일치 연산자 (===)**
- 두 피연산자의 값과 타입을 모두 비교하여, 암묵적 타입 변환을 하지 않음
- 더 엄격하고 예측 가능하므로 이 연산자의 사용이 권장

**논리 연산자**
- `&&`(AND), `||`(OR), `!`(NOT)가 있으며, 단축 평가를 지원

#### 반복문

**for...in**
- 객체의 키(key)를 순회, 배열에는 부적합
- 배열에 사용하면 인덱스를 문자열로 반환하고 순서를 보장하지 않아 권장되지 않음

**for...of**
- 배열 등 반복 가능한 객체의 값(value)을 순회
- 객체는 반복 가능하지 않으므로 직접 사용할 수 없음

#### 함수

**함수 정의 방법:**

1. **함수 선언식**
   - `function funcName() { }` 형태로 정의하며, 호이스팅(hoisting)의 영향을 받음

2. **함수 표현식**
   - `const funcName = function() { }` 형태로 변수에 함수를 할당
   - 호이스팅되지 않아 코드의 예측 가능성이 높아져 사용이 권장됨

3. **화살표 함수**
   - `const arrow = () => { }` 형태로 함수 표현식을 더 간결하게 작성하는 방법
   - 함수 본문이 한 줄이면 `{}`와 `return`을 생략할 수 있음

**매개변수:**
- **기본 매개변수**: `function (name = 'Anonymous')` 처럼 인자가 전달되지 않을 경우를 대비해 기본값을 설정
- **나머지 매개변수**: `function (...args) { }` 형태로 작성하며, 정해지지 않은 수의 인자들을 배열로 받을 수 있음
- **전개 구문 (...)**: `myFunc(...numbers)`처럼 배열이나 반복 가능한 객체를 펼쳐서 함수의 인자로 전달할 때 사용

---

## 실습 예제

### 장바구니 총액 계산 함수

장바구니 총액을 계산하고, 특정 금액이 넘으면 '무료 배송'을 적용하는 기능:

```javascript
const calculateCartTotal = function (items) {
  let total = 0;
  
  for (const item of items) {
    total += item.price * item.quantity;
  }
  
  if (total >= 50000) {
    console.log(`총액: ${total}원 (무료 배송)`);
  } else {
    console.log(`총액: ${total}원`);
  }
};
```

---

**작성일**: 2024
**과정**: SSAFY JavaScript Basic Syntax 01
