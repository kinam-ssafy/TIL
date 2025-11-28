# JavaScript Basic Syntax 01 실습 코드 정리

## 📚 목차

1. [데이터 타입](#1-데이터-타입)
2. [원시 자료형](#2-원시-자료형)
3. [자동 형변환](#3-자동-형변환)
4. [연산자](#4-연산자)
5. [조건문](#5-조건문)
6. [반복문](#6-반복문)
7. [for...in과 for...of](#7-forin과-forof)
8. [함수 매개변수](#8-함수-매개변수)
9. [전개 구문](#9-전개-구문)
10. [화살표 함수](#10-화살표-함수)

---

## 1. 데이터 타입

**파일명**: `01-data-types.html`

JavaScript의 원시 자료형과 참조 자료형의 차이를 이해하는 실습

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
    // === 원시 자료형 (Primitive type) ===
    // 값 자체가 변수에 직접 저장되며, 불변(immutable)
    
    const a = 'bar'
    console.log(a) // 'bar'

    // 문자열 메서드를 사용해도 원본은 변경되지 않음
    console.log(a.toUpperCase()) // 'BAR'
    console.log(a) // 'bar' (원본 유지)

    // 변수 간 할당 시 값이 복사됨
    let b = 10
    let c = b  // b의 값(10)이 c에 복사됨
    c = 20     // c만 변경
    console.log(b) // 10 (b는 변경되지 않음)
    console.log(c) // 20

    // === 참조 자료형 (Reference type) ===
    // 데이터가 저장된 메모리 주소가 변수에 저장됨, 가변(mutable)
    
    // 배열 예시
    const arr1 = [1, 2, 3]
    const arr2 = arr1  // arr1의 주소가 arr2에 복사됨 (같은 배열을 참조)
    arr2.push(4)       // arr2를 통해 배열 수정
    
    console.log(arr1) // [1, 2, 3, 4] (arr1도 변경됨!)
    console.log(arr2) // [1, 2, 3, 4]
    // arr1과 arr2는 같은 배열을 참조하므로 하나를 수정하면 둘 다 영향받음

    // 객체 예시
    const obj1 = { name: 'Alice', age: 30 }
    const obj2 = obj1  // obj1의 주소가 obj2에 복사됨 (같은 객체를 참조)
    
    obj2.age = 40      // obj2를 통해 객체 수정
    
    console.log(obj1.age) // 40 (obj1도 변경됨!)
    console.log(obj2.age) // 40
    // obj1과 obj2는 같은 객체를 참조하므로 하나를 수정하면 둘 다 영향받음
  </script>
</body>
</html>
```

**핵심 개념:**
- **원시 자료형**: Number, String, Boolean, null, undefined
  - 값이 직접 저장되고, 복사 시 값이 복사됨
  - 불변(immutable)이므로 원본이 변경되지 않음
- **참조 자료형**: Object, Array, Function
  - 메모리 주소가 저장되고, 복사 시 주소가 복사됨
  - 가변(mutable)이므로 하나를 수정하면 같은 것을 참조하는 모든 변수에 영향

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 데이터 타입 섹션

---

## 2. 원시 자료형

**파일명**: `02-primitive-types.html`

JavaScript의 원시 자료형 종류와 특징을 익히는 실습

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
    // === Number (숫자) ===
    // 정수와 실수를 구분하지 않고 모두 Number 타입
    const a = 13 
    const b = -5 
    const c = 3.14 
    const d = 2.998e8      // 과학적 표기법 (2.998 × 10^8)
    const e = Infinity     // 양의 무한대
    const f = -Infinity    // 음의 무한대
    const g = NaN          // Not a Number (숫자가 아님)
    
    const k = 13.0
    // console.log(a == k)   // true (값 비교)
    // console.log(a === k)  // true (값과 타입 비교)
    // console.log(0.1 + 0.2)  // 0.30000000000000004 (부동소수점 오차)

    // === String (문자열) ===
    const firstName = 'Tony'
    const lastName = 'Stark'
    const fullName = firstName + lastName  // + 로 문자열 결합 가능
    console.log(fullName) // 'TonyStark'

    // 템플릿 리터럴 (Template literals)
    // 백틱(`)을 사용하여 변수를 문자열에 삽입
    const age = 100 
    const message = `홍길동은 ${age}세입니다.`
    console.log(message) // '홍길동은 100세입니다.'

    // === null (값이 없음을 의도적으로 나타냄) ===
    let x = null
    console.log(x) // null
    console.log(typeof x)  // 'object' (JavaScript의 버그, 실제로는 원시 타입)
    console.log(10 + x)  // 10 (null은 숫자 연산에서 0으로 취급)

    // === undefined (값이 할당되지 않은 상태) ===
    let y 
    console.log(y)  // undefined
    console.log(typeof y)  // 'undefined'
    console.log(10 + y)  // NaN (undefined와 연산하면 NaN)

    // === Boolean (참/거짓) ===
    let m = true
    let n = false
    console.log(typeof m)  // 'boolean'
    console.log(10 > 5)  // true
    console.log(10 < 5)  // false
  </script>
</body>
</html>
```

**핵심 개념:**
- **Number**: 정수와 실수를 구분하지 않음, Infinity, -Infinity, NaN 포함
- **String**: 문자열, `+`로 결합, 템플릿 리터럴(`${변수}`)로 삽입
- **null**: 개발자가 의도적으로 '값이 없음'을 표현
- **undefined**: 값이 할당되지 않은 상태 (시스템이 자동 할당)
- **Boolean**: true, false 두 가지 값

**주의사항:**
- `typeof null`은 `'object'`를 반환 (JavaScript의 역사적 버그)
- `0.1 + 0.2`는 `0.3`이 아니라 `0.30000000000000004` (부동소수점 오차)

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 원시 자료형 섹션

---

## 3. 자동 형변환

**파일명**: `03-type-coercion.html`

조건문에서 값이 boolean으로 자동 변환되는 규칙을 익히는 실습

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
    // JavaScript는 조건문에서 값을 자동으로 boolean으로 변환
    
    // === Number의 boolean 변환 ===
    console.log(Boolean(0));    // false (0은 거짓)
    console.log(Boolean(10));   // true (0이 아닌 숫자는 참)
    console.log(Boolean(NaN));  // false (NaN은 거짓)

    // === String의 boolean 변환 ===
    // console.log(Boolean(""));        // false (빈 문자열은 거짓)
    // console.log(Boolean("hello"));   // true (내용이 있는 문자열은 참)
    // console.log(Boolean("0"));       // true (문자 '0'은 참, 숫자 0과 다름!)

    // === null과 undefined의 boolean 변환 ===
    // console.log(Boolean(null));      // false (null은 거짓)
    // console.log(Boolean(undefined)); // false (undefined는 거짓)

    // === 객체와 배열의 boolean 변환 ===
    // console.log(Boolean([]));        // true (빈 배열도 참!)
    // console.log(Boolean({}));        // true (빈 객체도 참!)
  </script>
</body>
</html>
```

**핵심 개념:**

| 데이터 타입 | false | true |
|------------|-------|------|
| **undefined** | 항상 false | - |
| **null** | 항상 false | - |
| **Number** | 0, -0, NaN | 나머지 모든 경우 |
| **String** | '' (빈 문자열) | 나머지 모든 경우 |
| **Object/Array** | - | 항상 true (빈 객체/배열도 true!) |

**주의사항:**
- `"0"` (문자열)은 true, `0` (숫자)은 false
- `[]` (빈 배열)과 `{}` (빈 객체)는 true

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 원시 자료형 > 자동 형변환 섹션

---

## 4. 연산자

**파일명**: `04-operators.html`

JavaScript의 다양한 연산자를 익히는 실습

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
    // === 할당 연산자 ===
    let a = 0

    a += 10  // a = a + 10
    console.log(a)  // 10

    a -= 3   // a = a - 3
    console.log(a)  // 7

    a *= 10  // a = a * 10
    console.log(a)  // 70

    a %= 7   // a = a % 7 (나머지)
    console.log(a)  // 0

    // === 증감 연산자 ===
    // 후위 증가 (x++): 현재 값을 반환한 후 증가
    let x = 3
    const y = x++  // y에는 3이 할당되고, 그 후 x가 4가 됨
    console.log(x, y)  // 4, 3

    // 전위 증가 (++x): 먼저 증가한 후 값을 반환
    let m = 3
    const n = ++m  // m을 먼저 4로 증가시킨 후 n에 할당
    console.log(m, n)  // 4, 4

    // === 비교 연산자 ===
    console.log(3 > 2)      // true
    console.log(3 < 2)      // false
    console.log('A' < 'B')  // true (알파벳 순서)
    console.log('Z' < 'a')  // true (대문자 < 소문자)
    console.log('가' < '나') // true (한글 순서)

    // === 동등 연산자 (==) ===
    // 타입을 자동 변환하여 값만 비교
    console.log(1 == 1)            // true
    console.log('hello' == 'hello') // true
    console.log('1' == 1)          // true (문자열 '1'을 숫자 1로 변환)
    console.log(0 == false)        // true (0과 false가 같다고 판단)

    // === 일치 연산자 (===) ===
    // 타입과 값 모두 비교 (권장!)
    console.log(1 === 1)            // true
    console.log('hello' === 'hello') // true
    console.log('1' === 1)          // false (타입이 다름)
    console.log(0 === false)        // false (타입이 다름)

    // === 논리 연산자 ===
    // AND (&&): 모두 true여야 true
    console.log(true && false);  // false
    console.log(true && true);   // true

    // OR (||): 하나라도 true면 true
    console.log(false || true);  // true
    console.log(false || false); // false

    // NOT (!): 반대 값
    console.log(!true);  // false

    // === (중요) 단축 평가 (Short-circuit Evaluation) ===
    // AND (&&) 연산: 첫 번째 falsy 값 또는 마지막 값 반환
    console.log(1 && 0);  // 0 (0이 falsy이므로 0 반환)
    console.log(0 && 1);  // 0 (0이 falsy이므로 바로 0 반환)
    console.log(4 && 7);  // 7 (둘 다 truthy이므로 마지막 값 반환)

    // OR (||) 연산: 첫 번째 truthy 값 또는 마지막 값 반환
    console.log(1 || 0);  // 1 (1이 truthy이므로 바로 1 반환)
    console.log(0 || 1);  // 1 (0이 falsy이므로 다음 값 확인)
    console.log(4 || 7);  // 4 (4가 truthy이므로 바로 4 반환)

    /* 단축평가 활용 예시
    
    1. 단축평가 활용 예시 (Positive)
    let user = null;
    const name = user || "Guest"; // user가 Falsy(null)이므로 "Guest"
    console.log(name); // "Guest"

    2. 단축평가 활용 예시 (Negative - 버그 발생)
    let score = 0; // 0점은 유효한 점수
    let currentScore = score || 50; // 0이 Falsy라서 50이 됨 (버그!)
    console.log(currentScore); // 50

    3. 단축평가 활용 예시 (해결책)
    let score = 0;
    let currentScore;

    if (score === null || score === undefined) {
        currentScore = 50; // null이나 undefined일 때만 기본값
    } else {
        currentScore = score;
    }
    console.log(currentScore); // 0 (정상!)

    4. 최종 해결책 (ES2020 도입) - Null 병합 연산자 (??)
    let score = 0;
    // score가 null이나 undefined가 아니므로(0임), 왼쪽 값(0)을 그대로 사용
    const currentScore = score ?? 50;
    console.log(currentScore); // 0 

    let user = null;
    const name = user ?? "Guest";
    console.log(name); // "Guest"
    */
  </script>
</body>
</html>
```

**핵심 개념:**
- **할당 연산자**: `+=`, `-=`, `*=`, `%=` 등
- **증감 연산자**: `x++` (후위), `++x` (전위)
- **비교 연산자**: `>`, `<`, `>=`, `<=`
- **동등 연산자 (==)**: 타입 변환 후 비교 (사용 비권장)
- **일치 연산자 (===)**: 타입과 값 모두 비교 (권장!)
- **논리 연산자**: `&&` (AND), `||` (OR), `!` (NOT)
- **단축 평가**: 논리 연산자의 특별한 동작 (값 자체를 반환)

**주의사항:**
- 특별한 경우가 아니면 항상 `===`를 사용할 것
- `||`를 기본값 설정에 사용할 때 0이나 빈 문자열 주의 → `??` 사용 권장

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 연산자 섹션

---

## 5. 조건문

**파일명**: `05-if-statement.html`

if 문과 삼항 연산자를 사용한 조건 처리 실습

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
    // === if 문 ===
    // 조건이 true일 때 코드 블록 실행
    const name = 'customer'

    if (name === 'admin') {
      console.log('관리자님 환영해요')
    } else if (name === 'customer') {
      console.log('고객님 환영해요')  // 이 부분 실행됨
    } else {
      console.log(`반갑습니다. ${name}님`)
    }

    // === 삼항 연산자 (Ternary Operator) ===
    // 구조: 조건 ? 참일때_값 : 거짓일때_값
    const age = 20
    const message = (age >= 18) ? '성인' : '미성년자'
    console.log(message) // '성인'

    // 주의: 조건이 2개가 넘어가면 가급적 if 문을 쓰자!
    // 삼항 연산자는 간단한 조건에만 사용하는 것이 가독성에 좋음
  </script>
</body>
</html>
```

**핵심 개념:**
- **if 문**: 조건에 따라 코드 블록 실행
  - `if`, `else if`, `else` 사용
- **삼항 연산자**: 간단한 조건부 값 할당
  - `조건 ? 참일때값 : 거짓일때값`
  - 복잡한 로직에는 사용 지양 (가독성 저하)

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 조건문 섹션

---

## 6. 반복문

**파일명**: `06-loops-and-iteration.html`

while, for, for...in, for...of 반복문을 익히는 실습

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
    // === while 반복문 ===
    // 조건이 참인 동안 반복
    let i = 0

    while (i < 6) {
      console.log(i)  // 0, 1, 2, 3, 4, 5
      i += 1
    }

    // === for 반복문 ===
    // 초기문; 조건문; 증감문 형태
    for (let i = 0; i < 6; i++) {
      console.log(i)  // 0, 1, 2, 3, 4, 5
    }

    console.log(i)  // ReferenceError: i is not defined
    // for 문 안에서 선언한 i는 블록 스코프이므로 밖에서 접근 불가

    // === for...in 반복문 ===
    // 객체의 key(속성 이름)를 순회
    const object = {
      a: 'apple',
      b: 'banana'
    }

    for (const property in object) {
      console.log(property)          // 'a', 'b' (키)
      console.log(object[property])  // 'apple', 'banana' (값)
    }

    // === for...of 반복문 ===
    // 반복 가능한 객체(배열, 문자열 등)의 value를 순회
    const numbers = [0, 1, 2, 3]
    
    // 잘못된 사용 예시 (for...in을 배열에 사용)
    for (const number in numbers) {
      console.log(number)  // 0, 1, 2, 3 (인덱스가 출력됨!)
    }

    // 올바른 사용 예시 (for...of를 배열에 사용)
    const myStr = 'apple'
    for (const str of myStr) {
      console.log(str)  // 'a', 'p', 'p', 'l', 'e' (값)
    }

    // === for...in과 for...of의 차이 ===
    const arr = ['a', 'b', 'c']

    // for...in: 인덱스(키) 반환
    for (const i in arr) {
      console.log(i)  // 0, 1, 2 (인덱스)
    }

    // for...of: 값 반환
    for (const i of arr) {
      console.log(i)  // 'a', 'b', 'c' (값)
    }
  </script>
</body>
</html>
```

**핵심 개념:**
- **while**: 조건이 참인 동안 반복
- **for**: 초기화, 조건, 증감을 한 줄에 작성
- **for...in**: 객체의 **키(key)**를 순회 (배열에는 비권장)
- **for...of**: 반복 가능한 객체의 **값(value)**을 순회 (배열 권장)

**주의사항:**
- 배열에는 `for...of` 사용 (값에 직접 접근)
- 객체에는 `for...in` 사용 (키로 접근)
- `for...in`을 배열에 사용하면 인덱스가 반환됨

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 반복문 섹션

---

## 7. for...in과 for...of

**파일명**: `07-forin-and-forof.html`

for...in과 for...of의 차이를 명확히 이해하는 실습

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
    // === for...in 반복문 ===
    // 객체의 열거 가능한 속성(키)에 대해 반복

    // Array (배열에는 비권장)
    // const arr1 = ['a', 'b', 'c']

    // for (const elem in arr1) {
    //   console.log(elem) // 0, 1, 2 (인덱스가 문자열로 반환)
    // }

    // Object (객체에 권장)
    // const capitals1 = {
    //   korea: '서울',
    //   japan: '도쿄',
    //   china: '베이징'
    // }

    // for (const capital in capitals1) {
    //   console.log(capital) // 'korea', 'japan', 'china' (키)
    // }

    //////////////////////////////////////////////////////////////////////

    // === for...of 반복문 ===
    // 반복 가능한 객체의 값(value)에 대해 반복

    // Array (배열에 권장)
    const arr2 = ['a', 'b', 'c']

    for (const elem of arr2) {
      console.log(elem) // 'a', 'b', 'c' (값)
    }

    // Object (객체에는 사용 불가)
    const capitals2 = {
      korea: '서울',
      japan: '도쿄',
      china: '베이징',
    }

    for (const capital of capitals2) {
      console.log(capital) // TypeError: capitals2 is not iterable
      // 객체는 반복 가능(iterable)하지 않으므로 for...of 사용 불가
    }
  </script>
</body>
</html>
```

**핵심 개념:**

| 구분 | for...in | for...of |
|------|----------|----------|
| **대상** | 객체의 키(key) | 반복 가능한 객체의 값(value) |
| **반환** | 속성 이름(key) | 속성 값(value) |
| **배열 사용** | 비권장 (인덱스 반환) | 권장 (값 반환) |
| **객체 사용** | 권장 | 사용 불가 (TypeError) |

**주의사항:**
- **배열**: `for...of` 사용 권장
- **객체**: `for...in` 사용 (객체는 iterable이 아니므로 `for...of` 불가)
- `for...in`을 배열에 사용하면 인덱스가 문자열로 반환되고 순서 보장 안됨

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 반복문 > for...in vs for...of 섹션

---

## 8. 함수 매개변수

**파일명**: `08-function-parameters.html`

기본 매개변수, 나머지 매개변수, 매개변수와 인자 관계를 익히는 실습

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
    // === 기본 함수 매개변수 (Default Parameter) ===
    // 인자가 전달되지 않을 경우 기본값 설정
    const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
    }

    greeting()         // 'Hi Anonymous' (기본값 사용)
    greeting('Alice')  // 'Hi Alice'

    // === 나머지 매개변수 (Rest Parameters) ===
    // 임의의 수의 인자를 배열로 받음
    const myFunc = function (param1, param2, ...restParams) {
      return [param1, param2, restParams]
    }

    myFunc(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    myFunc(1, 2)          // [1, 2, []]
    // param1: 1, param2: 2, restParams: [3, 4, 5]

    // === 매개변수 > 인자 (부족한 인자는 undefined 할당) ===
    const threeArgs = function (param1, param2, param3) {
      return [param1, param2, param3]
    }

    threeArgs()       // [undefined, undefined, undefined]
    threeArgs(1)      // [1, undefined, undefined]
    threeArgs(2, 3)   // [2, 3, undefined]

    // === 매개변수 < 인자 (넘치는 인자는 사용하지 않음) ===
    const noArgs = function () {
      return 0
    }
    noArgs(1, 2, 3)   // 0 (인자를 무시)

    const twoArgs = function (param1, param2) {
      return [param1, param2]
    }
    twoArgs(1, 2, 3)  // [1, 2] (3은 무시)
  </script>
</body>
</html>
```

**핵심 개념:**
- **기본 매개변수**: `function(param = 'default')` 형태로 기본값 설정
- **나머지 매개변수**: `function(...rest)` 형태로 여러 인자를 배열로 받음
- **매개변수 > 인자**: 부족한 인자는 `undefined`로 자동 할당
- **매개변수 < 인자**: 넘치는 인자는 무시됨

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 함수 > 매개변수 섹션

---

## 9. 전개 구문

**파일명**: `09-spread-syntax.html`

전개 구문(Spread Syntax)을 사용한 인자 전달과 나머지 매개변수 실습

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
    // === 전개 구문 (Spread Syntax) - 함수 호출 시 인자 확장 ===
    function myFunc(x, y, z) {
      return x + y + z
    }

    let numbers = [1, 2, 3]

    // 배열을 펼쳐서 개별 인자로 전달
    console.log(myFunc(...numbers)) // 6
    // myFunc(1, 2, 3)과 동일

    // === 나머지 매개변수 (Rest Parameters) - 압축 용도 ===
    function myFunc2(x, y, ...restArgs) {
      return [x, y, restArgs]
    }
    
    console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
    // x: 1, y: 2, restArgs: [3, 4, 5] (여러 인자를 배열로 묶음)
    
    console.log(myFunc2(1, 2))          // [1, 2, []]
    // restArgs는 빈 배열
  </script>
</body>
</html>
```

**핵심 개념:**
- **전개 구문 (`...`)**: 배열이나 객체를 **펼쳐서** 개별 요소로 확장
  - 함수 호출 시: `myFunc(...array)` → 배열을 개별 인자로 전달
  - 배열 결합 시: `[...arr1, ...arr2]` → 두 배열 합치기
- **나머지 매개변수 (`...rest`)**: 여러 개를 **하나로 묶음**
  - 함수 정의 시: `function(...rest)` → 여러 인자를 배열로 받음

**구분 방법:**
```javascript
// 전개 구문: 하나를 여러 개로 펼침
const arr = [1, 2, 3]
myFunc(...arr)  // myFunc(1, 2, 3)과 동일

// 나머지 매개변수: 여러 개를 하나로 묶음
function func(...rest) {  // rest = [1, 2, 3]
  console.log(rest)
}
func(1, 2, 3)
```

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 함수 > 매개변수 > 전개 구문 섹션

---

## 10. 화살표 함수

**파일명**: `99-arrow-function.html`

화살표 함수의 특수한 경우를 익히는 실습

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
    // === 1. 인자가 없다면 () or _ 로 표시 가능 ===
    const noArgs1 = () => 'No args'
    const noArgs2 = _ => 'No args'
    
    console.log(noArgs1())  // 'No args'
    console.log(noArgs2())  // 'No args'

    // === 2-1. 객체를 return 한다면 return을 명시적으로 작성해야 함 ===
    const returnObject1 = () => { 
      return { key: 'value' } 
    }
    console.log(returnObject1())  // { key: 'value' }

    // === 2-2. return을 작성하지 않으려면 객체를 소괄호로 감싸야 함 ===
    const returnObject2 = () => ({ key: 'value' })
    console.log(returnObject2())  // { key: 'value' }

    // 잘못된 예시 (중괄호를 객체로 인식하지 못함)
    // const returnObject3 = () => { key: 'value' }
    // 위 코드는 에러 발생 (중괄호가 함수 블록으로 인식됨)
  </script>
</body>
</html>
```

**핵심 개념:**
- **인자가 없을 때**: `()` 또는 `_` 사용 가능
- **객체 반환 시**:
  - 명시적 return: `() => { return { key: 'value' } }`
  - 축약형: `() => ({ key: 'value' })` (소괄호로 감싸기!)

**주의사항:**
- `() => { key: 'value' }`는 작동하지 않음
  - 중괄호가 함수 블록으로 인식되어 객체로 인식되지 않음
- 객체를 반환할 때는 **반드시 소괄호로 감싸거나** return을 명시해야 함

**참고 교안**: `JavaScript_Basic_Syntax_01.md` - 참고 > 화살표 함수 심화 섹션

---

## 실습 순서 추천

1. **01-data-types.html**: 원시/참조 자료형 차이 이해
2. **02-primitive-types.html**: 원시 자료형 종류 익히기
3. **03-type-coercion.html**: 자동 형변환 규칙 학습
4. **04-operators.html**: 다양한 연산자 사용법
5. **05-if-statement.html**: 조건문 작성
6. **06-loops-and-iteration.html**: 반복문 기초
7. **07-forin-and-forof.html**: for...in과 for...of 차이 명확히
8. **08-function-parameters.html**: 함수 매개변수 다루기
9. **09-spread-syntax.html**: 전개 구문 활용
10. **99-arrow-function.html**: 화살표 함수 특수 케이스

---

## 핵심 개념 요약표

| 개념 | 설명 | 예시 |
|------|------|------|
| **원시 자료형** | 값 직접 저장, 불변 | Number, String, Boolean, null, undefined |
| **참조 자료형** | 주소 저장, 가변 | Object, Array, Function |
| **템플릿 리터럴** | 변수를 문자열에 삽입 | `` `${name}님 환영합니다` `` |
| **일치 연산자 (===)** | 타입과 값 모두 비교 | `1 === 1` (true), `'1' === 1` (false) |
| **단축 평가** | 논리 연산자가 값 자체 반환 | `1 && 0` → `0`, `1 || 0` → `1` |
| **for...in** | 객체의 키 순회 | `for (const key in obj)` |
| **for...of** | 배열의 값 순회 | `for (const val of arr)` |
| **나머지 매개변수** | 여러 인자를 배열로 | `function(...rest)` |
| **전개 구문** | 배열/객체를 펼침 | `myFunc(...array)` |
| **화살표 함수** | 간결한 함수 표현 | `const func = () => {}` |

---

## 주의사항 체크리스트

- [ ] `var` 사용하지 않기 (let, const만 사용)
- [ ] 비교 시 `===` 사용하기 (`==` 지양)
- [ ] 배열에는 `for...of`, 객체에는 `for...in` 사용
- [ ] `typeof null`은 `'object'`를 반환 (버그)
- [ ] 화살표 함수로 객체 반환 시 소괄호로 감싸기
- [ ] `0`, `''`, `null`, `undefined`, `NaN`은 falsy 값
- [ ] 빈 배열 `[]`, 빈 객체 `{}`는 truthy 값
- [ ] 단축 평가 사용 시 0이나 빈 문자열 주의

---

**작성일**: 2024  
**참고 교안**: SSAFY JavaScript_Basic_Syntax_01.md

