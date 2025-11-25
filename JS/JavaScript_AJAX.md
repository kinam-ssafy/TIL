# JavaScript AJAX

## 📚 목차

1. [비동기](#비동기)
2. [JavaScript와 비동기](#javascript와-비동기)
3. [JavaScript Runtime](#javascript-runtime)
4. [Ajax](#ajax)
5. [Axios](#axios)
6. [Axios 활용](#axios-활용)
7. [Ajax와 Axios](#ajax와-axios)
8. [Callback과 Promise](#callback과-promise)
9. [비동기 콜백](#비동기-콜백)
10. [프로미스](#프로미스)
11. [참고](#참고)
    - [비동기 처리와 사용자 경험](#비동기-처리와-사용자-경험)
    - [비동기 처리 적용 사례](#비동기-처리-적용-사례)
    - [비동기 처리 주의사항](#비동기-처리-주의사항)
12. [핵심 정리](#핵심-정리)

---

## 🎯 학습 목표

- 동기식과 비동기식 처리 방식의 차이점을 설명할 수 있다.
- 이벤트 루프를 통한 JS 비동기 처리 과정을 설명할 수 있다.
- Ajax를 통해 페이지 일부를 비동기적으로 업데이트한다.
- Axios 라이브러리를 사용해 비동기 HTTP 요청을 보낸다.
- then과 catch를 사용해 Promise의 성공과 실패를 처리한다.
- Promise chaining으로 콜백 지옥 없이 비동기 로직을 구성한다.
- API로 받은 데이터로 동적으로 DOM 요소를 조작할 수 있다.

---

## 🌟 시작하기

아래 코드의 실행 결과는 무엇일까요?

**후보 1)** A -> B -> C  
**후보 2)** A -> C -> B

```javascript
console.log('A');
setTimeout(() => {
  console.log('B');
}, 1000);
console.log('C');
```

코드의 실행 순서를 결정하는 자바스크립트의 비동기 처리 방식과 이벤트 루프에 대해서 학습합니다.

---

## 비동기

### Synchronous 란?

**동기 (Synchronous)**
- 프로그램의 실행 흐름이 순차적으로 진행
- 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식

### 동기(Synchronous) 실생활 예시

**카페 커피 주문**

```
[손님 1] 아메리카노 한 잔 주세요
         ↓
[바리스타] 아메리카노 하나요. 주문이 완료될 때까지 잠시만 기다려주세요.
         ↓
[손님 1] 네, 감사합니다. (커피가 나올 때까지 대기)
         ↓
[바리스타] 아메리카노 나왔습니다. 감사합니다.
         ↓
[손님 2] 카페라떼 두 잔 주세요
```

> **💡 핵심**: 손님 1의 주문이 완료되어야만 다음 손님의 주문을 진행할 수 있음

### 동기(Synchronous) 코드 예시

반복이 완료될 때까지 다음 작업(작업 2)이 시작되지 않음

```javascript
console.log('작업 1 시작')

const syncTask = function () {
  for (let i = 0; i < 1000000000; i++) {
    // 반복 실행 동안 잠시 대기
  }
  return '작업 완료'
}

const result = syncTask()
console.log(result)

console.log('작업 2 시작')
```

**출력 결과:**
```
작업 1 시작
(반복 실행 동안 잠시 대기)
작업 완료
작업 2 시작
```

---

## Asynchronous 란?

**비동기 (Asynchronous)**
- 특정 작업의 실행이 완료될 때까지 기다리지 않고 다음 작업을 즉시 실행하는 방식
- 한 작업의 완료 여부를 기다리지 않고 다른 작업을 동시에 수행할 수 있는 방식

### 비동기(Asynchronous) 실생활 예시 (1/3)

**카페 커피 주문**

```
[손님 1] 아메리카노 한 잔 주세요
         ↓
[바리스타] 아메리카노 하나요. 여기 진동 벨 드리겠습니다.
         ↓
[손님 1] 네, 감사합니다.
         ↓
[바리스타] 안녕하세요, 어떤 거 드릴까요?
         ↓
[손님 2] 카페라떼 두 잔 주세요
```

> **💡 핵심**: 손님 1의 커피가 만들어지는 동안 다음 손님의 주문을 처리할 수 있음

### 비동기(Asynchronous) 실생활 예시 (2/3) - 메일 전송

- Gmail에서 메일 전송을 누르면 받은 편지함으로 화면이 전환됨
- 실제로 메일 전송 작업이 완료된 후에 화면이 전환되는 것이 아니고 병렬적으로 별도로 처리됨
- 메일 전송 작업이 진행되는 중에도 사용자는 다른 작업을 진행할 수 있음

### 비동기(Asynchronous) 실생활 예시 (3/3) - 브라우저

- 브라우저는 웹페이지를 먼저 처리되는 요소부터 그려 나가며 처리가 오래 걸리는 것들은 별도로 처리가 완료되는 대로 병렬적으로 진행
- 이미지나 스크립트가 로드되는 동안에도 사용자는 페이지를 스크롤하거나 다른 요소와 상호작용할 수 있음

### 비동기(Asynchronous) 코드 예시

**콜백 함수**: 다른 함수에 인자로 전달되는 함수

```javascript
console.log('작업 1 시작')

const asyncTask = function (callback) {
  // 3초 뒤 기다렸다가 콜백 함수를 호출하는 함수
  setTimeout(() => {
    callback('작업 완료')
  }, 3000)
}

asyncTask((result) => {
  console.log(result)
})

console.log('작업 2 시작')
```

**출력 결과:**
```
작업 1 시작
작업 2 시작
(3초 대기)
작업 완료
```

> **💡 설명**: `setTimeout`은 비동기 함수라 코드를 즉시 실행하지 않고 3초 뒤에 실행하도록 예약만 한 뒤 바로 다음 코드로 넘어감. 따라서 '작업 2 시작'이 먼저 출력되고 3초가 지난 후에 예약되었던 콜백 함수가 실행

---

## Synchronous vs Asynchronous 특징

### Synchronous 특징

**장점:**
- 단순하고 예측 가능한 흐름
- 시작 순서대로 처리
- 앞의 작업이 먼저 끝나야만 다음 작업을 시작할 수 있음

**단점:**
- 시간이 오래 걸리는 작업이 실행되면 해당 작업이 끝날 때까지 프로그램 전체가 멈춤
- 시스템 자원의 낭비

### Asynchronous 특징

**장점:**
- 병렬적 수행
- 당장 처리를 완료할 수 없는 작업들은 백그라운드에서 실행되다 빨리 완료되는 작업부터 처리
- 시간이 오래 걸리는 작업을 백그라운드에 위임해 효율성 증가
- 프로그램이 멈추지 않아 사용자 경험(UX) 향상

**단점:**
- 작업의 시작 순서와 완료 순서가 다를 수 있어, 복잡한 흐름과 결과값을 처리해야 하므로 코드의 복잡성 증가

---

## JavaScript와 비동기

### Single Thread 언어, JavaScript

**JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어**

- 동시에 여러 작업을 처리할 수 없음
- 즉, JavaScript는 하나의 작업을 요청한 순서대로 처리할 수밖에 없음

**그렇다면 어떻게 Single Thread 언어인 JavaScript가 비동기 처리를 할 수 있을까?**

> **💡 TIP - Single Thread**: 작업을 처리할 때 실제로 작업을 수행하는 주체입니다. multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 것을 의미합니다.

---

## JavaScript Runtime

### JavaScript Runtime이란?

**JavaScript가 동작할 수 있는 환경 (Runtime)**

JavaScript는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요

**JavaScript Runtime 환경:**
- 브라우저
- Node.js

브라우저 환경에서 JavaScript의 비동기 처리 과정을 학습

> **💡 TIP - Node.js**: Chrome의 V8 JavaScript 엔진을 기반으로 하는 Server-Side 실행 환경

### 브라우저 환경과 JavaScript Runtime

**브라우저가 JavaScript 코드를 실행하는 환경 구성:**

```
┌─────────────────────────────────────┐
│      JavaScript Engine             │
│  ┌──────────────────────────────┐  │
│  │       Call Stack             │  │
│  │  (실행할 함수가 쌓이는 곳)    │  │
│  └──────────────────────────────┘  │
│                                     │
│         Web API                     │
│  (비동기 처리를 담당하는 곳)        │
│  - setTimeout                       │
│  - DOM API                          │
│  - AJAX 요청                        │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│       Task Queue                    │
│  (완료된 비동기 작업들이             │
│   실행을 기다리는 곳)                │
└─────────────────────────────────────┘
         │
         ▼
      Event Loop
   (Call Stack이 비면
   Task Queue의 작업을
   Call Stack으로 이동)
```

### 브라우저 환경의 JavaScript 비동기 처리 구성 요소

**1. JavaScript Engine의 Call Stack**
- 요청이 들어올 때마다 순차적으로 처리하는 Stack(LIFO)
- 기본적인 JavaScript의 Single Thread 작업 처리

**2. Web API**
- JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경
- 시간이 소요되는 작업을 처리 (setTimeout, DOM Event, AJAX 요청 등)

**3. Task Queue**
- 비동기 처리가 끝난 callback 함수가 대기하는 Queue(FIFO)

**4. Event Loop**
- 태스크(작업)가 들어오길 기다렸다가 태스크가 들어오면 이를 처리하고, 처리할 태스크가 없는 경우엔 잠드는 끊임없이 돌아가는 자바스크립트 내 루프
- Call Stack과 Task Queue를 지속적으로 모니터링
- Call Stack이 비어 있는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

### 비동기 처리 동작 방식

**전체 동작 순서:**

1. 모든 작업은 **Call Stack**(LIFO)으로 들어간 후 처리된다
2. 오래 걸리는 작업이 Call Stack으로 들어오면 **Web API**로 보내 별도로 처리하도록 한다
3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 **Task Queue**(FIFO)에 순서대로 들어간다
4. **Event Loop**가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된(가장 앞에 있는) 작업을 Call Stack으로 보낸다

### 비동기 처리 예시 코드

```javascript
console.log('Hi')

setTimeout(() => {
  console.log('Work')
}, 3000)

console.log('Bye')
```

**실행 과정:**

1. `console.log('Hi')` 실행
   - Call Stack에 추가
   - 실행 완료 후 제거
   - 출력: "Hi"

2. `setTimeout(() => {...}, 3000)` 실행
   - Call Stack에 추가
   - Web API로 타이머 작업 전달
   - Call Stack에서 제거

3. `console.log('Bye')` 실행
   - Call Stack에 추가
   - 실행 완료 후 제거
   - 출력: "Bye"

4. 3초 후 Web API의 타이머 완료
   - 콜백 함수가 Task Queue에 추가

5. Event Loop가 Call Stack이 비어있음을 확인
   - Task Queue의 콜백 함수를 Call Stack으로 이동

6. `console.log('Work')` 실행
   - 출력: "Work"

**최종 출력 결과:**
```
Hi
Bye
Work
```

---

## Ajax

### Ajax란?

**Ajax (Asynchronous JavaScript And XML)**
- XMLHttpRequest 기술을 사용해 복잡하고 동적인 웹 페이지를 구성하는 프로그래밍 방식

**Ajax 정의:**
- 비동기적인 웹 애플리케이션 개발을 위한 기술
- 브라우저와 서버 간의 데이터를 비동기적으로 교환하는 기술
- Ajax를 사용하면 페이지 전체를 새로고침 하지 않고도 동적으로 데이터를 불러와 화면을 갱신할 수 있음

**Ajax 이름 유래:**
- 초기에는 주로 XML 형식의 데이터를 주고받았기 때문에 이런 이름이 붙음
- 현재는 XML보다 JSON을 더 많이 사용

### XMLHttpRequest 객체

**XMLHttpRequest (XHR)**
- 서버와 상호작용할 때 사용하는 객체
- 페이지의 새로고침 없이도 데이터를 가져올 수 있음

> **💡 참고**: 이름에 XML이라는 단어가 들어가긴 하지만 XML뿐만 아니라 모든 종류의 데이터를 가져올 수 있음

### Ajax 실생활 예시

**비동기 웹 통신의 실생활 예시:**

1. **Gmail**
   - 메일을 작성하는 동안 자동 저장
   - 메일 전송 후에도 다른 메일함을 볼 수 있음

2. **Google Maps**
   - 지도를 이동하거나 확대/축소할 때 필요한 부분만 새로 불러옴
   - 페이지 전체를 새로고침하지 않음

3. **Youtube**
   - 댓글을 작성해도 동영상 재생이 멈추지 않음
   - 추천 동영상 목록이 계속 업데이트됨

4. **Facebook / Instagram**
   - 스크롤을 내리면 자동으로 새로운 게시물이 로드됨
   - 좋아요를 누르거나 댓글을 달아도 페이지가 새로고침되지 않음

### 기존 방식 vs Ajax 방식

**기존 방식:**
```
1. 클라이언트(브라우저)에서 form을 제출
   ↓
2. 서버는 요청 내용에 따라 데이터 처리 후 새로운 웹페이지를 작성
   ↓
3. 응답으로 완성된 HTML 페이지를 클라이언트에게 전달
   ↓
결과: 페이지가 깜빡이며 새로고침됨 (UX 저하)
```

**Ajax 방식:**
```
1. 클라이언트(브라우저)에서 필요한 데이터만 비동기적으로 요청
   ↓
2. 서버는 필요한 데이터만 처리해서 응답 (주로 JSON 형식)
   ↓
3. 클라이언트는 받은 데이터로 페이지의 일부분만 동적으로 갱신
   ↓
결과: 페이지 새로고침 없이 부드러운 사용자 경험 (UX 향상)
```

### Ajax의 핵심 기술

**Ajax는 하나의 기술이 아닌 기존의 여러 기술을 사용하는 "새로운 접근법"**

1. **XMLHttpRequest 객체**: 서버와 통신
2. **JavaScript**: 요청 전송 및 응답 처리
3. **DOM 조작**: 받은 데이터로 화면 일부 갱신

---

## Axios

### Axios란?

**Axios**
- 브라우저와 Node.js에서 사용할 수 있는 Promise 기반 HTTP 클라이언트 라이브러리

**Axios 특징:**
- 클라이언트 및 서버 사이에 HTTP 요청을 만들고 응답을 받는 데 사용되는 자바스크립트 라이브러리
- 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구
- 브라우저를 위한 XHR 객체 생성
- 간편한 API를 제공하며, Promise 기반의 비동기 요청을 처리
- 주로 웹 애플리케이션에서 서버와 통신할 때 사용

### Axios 설치

**CDN 방식:**

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

**npm 방식:**

```bash
npm install axios
```

### Axios 기본 구조

```javascript
axios({
  method: 'HTTP 메서드',
  url: '요청할 URL',
})
  .then(성공하면 수행할 콜백함수)
  .catch(실패하면 수행할 콜백함수)
```

**주요 메서드:**

```javascript
// GET 요청
axios.get(url)
  .then(response => {
    // 성공 처리
  })
  .catch(error => {
    // 실패 처리
  })

// POST 요청
axios.post(url, data)
  .then(response => {
    // 성공 처리
  })
  .catch(error => {
    // 실패 처리
  })
```

### 'then' & 'catch'

**then(callback)**
- 요청한 작업이 성공하면 callback 실행
- callback은 이전 작업의 성공 결과를 인자로 전달 받음

**catch(callback)**
- then()이 하나라도 실패하면 callback 실행 (남은 then은 중단)
- callback은 이전 작업의 실패 객체를 인자로 전달 받음

### Axios 기본 예시

**고양이 사진 가져오기:**

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const URL = 'https://api.thecatapi.com/v1/images/search'
  
  axios({
    method: 'get',
    url: URL,
  })
    .then((response) => {
      console.log(response)
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error)
      console.log('실패했다옹')
    })
  
  console.log('야옹야옹')
</script>
```

**출력 결과:**
```
야옹야옹
(response 객체 출력)
(response.data 출력)
```

> **💡 핵심**: Axios 요청은 비동기로 처리되므로 `console.log('야옹야옹')`이 먼저 실행됨

### 기본 요청 설정

```javascript
// 기본 URL 설정
axios.defaults.baseURL = 'https://api.example.com'

// 기본 헤더 설정
axios.defaults.headers.common['Authorization'] = 'Bearer token'
axios.defaults.headers.post['Content-Type'] = 'application/json'

// 타임아웃 설정
axios.defaults.timeout = 5000
```

---

## Axios 활용

### 고양이 이미지 가져오기 실습

**HTML 구조:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cat API</title>
</head>
<body>
  <button>냥냥펀치</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    console.log('고양이는 야옹')
    const URL = 'https://api.thecatapi.com/v1/images/search'

    const btn = document.querySelector('button')

    btn.addEventListener('click', () => {
      axios({
        method: 'get',
        url: URL,
      })
        .then((response) => {
          console.log(response)
          console.log(response.data)
          console.log(response.data[0].url)

          // 이미지 태그 생성
          const imgTag = document.createElement('img')
          imgTag.src = response.data[0].url
          document.body.appendChild(imgTag)
        })
        .catch((error) => {
          console.log(error)
          console.log('실패했다옹')
        })
    })

    console.log('야옹야옹')
  </script>
</body>
</html>
```

**실행 과정:**

1. 페이지 로드 시 "고양이는 야옹", "야옹야옹" 출력
2. 버튼 클릭 시 API 요청
3. 성공하면 고양이 이미지를 화면에 추가
4. 실패하면 "실패했다옹" 출력

### 정리

**Axios 요청은 비동기로 처리된다:**

```javascript
console.log('고양이는 야옹')  // 1. 동기

axios({...})  // 2. 비동기 (백그라운드에서 처리)
  .then()
  .catch()

console.log('야옹야옹')  // 3. 동기
```

**실행 순서:**
1. `console.log('고양이는 야옹')` → Call Stack에서 바로 실행
2. `axios()` → Web API로 전달되어 백그라운드에서 처리
3. `console.log('야옹야옹')` → Call Stack에서 바로 실행
4. axios 요청 완료 → then 콜백이 Task Queue로 이동
5. Event Loop → Call Stack이 비어있으면 then 콜백 실행

---

## Ajax와 Axios

### Ajax와 Axios 비교

| 구분 | Ajax (XMLHttpRequest) | Axios |
|------|----------------------|--------|
| **정의** | 브라우저 내장 객체 | 외부 라이브러리 |
| **사용법** | 복잡한 코드 필요 | 간결한 API 제공 |
| **Promise** | 지원 안 함 (콜백 사용) | Promise 기반 |
| **JSON 변환** | 수동으로 변환 필요 | 자동 변환 |
| **에러 처리** | 복잡 | 간단 (catch 사용) |
| **브라우저 호환성** | 모든 브라우저 | 대부분 브라우저 |

### XMLHttpRequest 예시

```javascript
const xhr = new XMLHttpRequest()
xhr.open('GET', 'https://api.example.com/data')

xhr.onload = function() {
  if (xhr.status === 200) {
    const data = JSON.parse(xhr.responseText)
    console.log(data)
  }
}

xhr.onerror = function() {
  console.log('요청 실패')
}

xhr.send()
```

### Axios 예시

```javascript
axios.get('https://api.example.com/data')
  .then(response => {
    console.log(response.data)
  })
  .catch(error => {
    console.log('요청 실패')
  })
```

---

## Callback과 Promise

### 비동기 콜백

**비동기 콜백**
- 비동기 작업이 완료된 후 실행될 함수를 미리 정의하여 전달하는 방식

**비동기 콜백의 한계 - 콜백 지옥 (Callback Hell)**

```javascript
// 콜백 지옥 예시
work1(function(result1) {
  work2(result1, function(result2) {
    work3(result2, function(result3) {
      work4(result3, function(result4) {
        work5(result4, function(result5) {
          console.log('최종 결과:', result5)
        })
      })
    })
  })
})
```

**콜백 지옥의 문제점:**
- 코드 가독성 저하
- 디버깅 어려움
- 에러 처리 복잡
- 유지보수 어려움

---

## 프로미스

### Promise란?

**Promise**
- JavaScript에서 비동기 작업의 최종 완료 또는 실패를 나타내는 객체
- 비동기 프로그래밍을 위한 오브젝트
- 미래의 어떤 상황에 대한 약속

### Promise의 3가지 상태

**1. Pending (대기)**
- 비동기 처리 로직이 아직 완료되지 않은 상태
- Promise 객체가 생성된 초기 상태

**2. Fulfilled (이행)**
- 비동기 처리가 완료되어 Promise가 결과 값을 반환해준 상태
- then()을 이용하여 처리 결과 값을 받을 수 있음

**3. Rejected (거부)**
- 비동기 처리가 실패하거나 오류가 발생한 상태
- catch()를 이용하여 에러를 처리할 수 있음

### Promise 기본 구조

```javascript
const promise = new Promise((resolve, reject) => {
  // 비동기 작업 수행
  
  if (/* 성공 조건 */) {
    resolve('성공 결과')
  } else {
    reject('실패 이유')
  }
})

promise
  .then(result => {
    // 성공 시 실행
    console.log(result)
  })
  .catch(error => {
    // 실패 시 실행
    console.log(error)
  })
  .finally(() => {
    // 성공/실패 여부와 관계없이 실행
    console.log('작업 완료')
  })
```

### then & catch의 chaining

**then(callback)**
- 요청한 작업이 성공하면 callback 실행
- callback은 이전 작업의 성공 결과를 인자로 전달받음

**catch(callback)**
- then()이 하나라도 실패하면 callback 실행
- callback은 이전 작업의 실패 객체를 인자로 전달받음

**chaining의 장점:**
- 작업의 순서를 보장
- 코드를 유지보수하기 편하게 작성
- 각각의 작업이 독립적으로 에러 처리 가능

**chaining의 주의사항:**
- then과 catch는 모두 항상 promise 객체를 반환
- 계속해서 chaining 할 수 있음
- axios로 처리한 비동기 로직이 항상 promise 객체를 반환
- then을 계속 이어 나가면서 작성할 수 있던 것

### Promise chaining 예시

**기존 콜백 방식:**

```javascript
work1(function(result1) {
  work2(result1, function(result2) {
    work3(result2, function(result3) {
      console.log('최종 결과:', result3)
    })
  })
})
```

**Promise chaining 방식:**

```javascript
work1()
  .then(result1 => {
    console.log('work1 결과:', result1)
    return work2(result1)
  })
  .then(result2 => {
    console.log('work2 결과:', result2)
    return work3(result2)
  })
  .then(result3 => {
    console.log('최종 결과:', result3)
  })
  .catch(error => {
    console.log('에러 발생:', error)
  })
```

### Promise chaining - 심화

**중간 과정 생략하기:**

```javascript
work1()
  .then(result1 => work2(result1))
  .then(result2 => work3(result2))
  .then(result3 => {
    console.log('최종 결과:', result3)
  })
  .catch(error => {
    console.log('에러 발생:', error)
  })
```

**화살표 함수 간소화:**

```javascript
work1()
  .then(work2)
  .then(work3)
  .then(result3 => {
    console.log('최종 결과:', result3)
  })
  .catch(error => {
    console.log('에러 발생:', error)
  })
```

### Axios with Promise chaining

**여러 고양이 사진 순차적으로 가져오기:**

```javascript
const URL = 'https://api.thecatapi.com/v1/images/search'

axios({
  method: 'get',
  url: URL,
})
  .then((response) => {
    console.log('1번째 고양이')
    const imgTag1 = document.createElement('img')
    imgTag1.src = response.data[0].url
    document.body.appendChild(imgTag1)
    
    return axios({ method: 'get', url: URL })
  })
  .then((response) => {
    console.log('2번째 고양이')
    const imgTag2 = document.createElement('img')
    imgTag2.src = response.data[0].url
    document.body.appendChild(imgTag2)
    
    return axios({ method: 'get', url: URL })
  })
  .then((response) => {
    console.log('3번째 고양이')
    const imgTag3 = document.createElement('img')
    imgTag3.src = response.data[0].url
    document.body.appendChild(imgTag3)
  })
  .catch((error) => {
    console.log(error)
    console.log('실패했다옹')
  })
```

> **💡 핵심**: 각 then은 이전 요청이 완료된 후에 실행되므로 순서가 보장됨

---

## 참고

### 비동기 처리와 사용자 경험

#### 동기식 처리의 한계 (1/3)

**동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨**

예시) 데이터가 매우 큰 문서를 불러올 때
- 서버에서 응답이 올 때까지 다른 작업을 할 수 없음
- 화면이 멈춘 것처럼 보임
- 사용자는 프로그램이 정지했다고 오해할 수 있음

#### 비동기 처리의 장점 (2/3)

**비동기 처리를 사용하면:**

- 시간이 오래 걸리는 작업(예: 데이터 로딩, API 호출)을 백그라운드에서 처리할 수 있음
- 주요 실행 흐름이 차단되지 않아 사용자 인터페이스가 계속 반응할 수 있음
- 데이터나 작업 결과가 준비되는 대로 순차적으로 화면에 표시할 수 있어, 사용자에게 진행 상황을 보여줄 수 있음

예시) 브라우저 다운로드
- 다운로드가 진행되는 동안에도 다른 탭을 사용할 수 있음
- 다운로드 진행 상황을 실시간으로 확인할 수 있음

#### 사용자 경험 향상 (3/3)

**비동기 처리를 통해:**

- 웹이 더 빠르고 반응적으로 느껴지게 할 수 있음
- 로딩 인디케이터나 부분적 콘텐츠 업데이트를 통해 사용자에게 진행 상황을 알려줄 수 있음
- 사용자는 전체 데이터가 로드되기를 기다리지 않고도 앱의 일부 기능을 사용할 수 있음

> **💡 TIP**: 비동기 처리에 대한 디테일한 개발은 사용자 경험을 많이 향상시킬 수 있습니다.
> 
> 예1) 요청 시작 즉시 로딩 스피너를 보여주면 사용자가 시스템이 멈췄다는 오해를 막을 수 있습니다.
> 
> 예2) 요청 실패 시 '다시 시도'와 같은 행동을 안내해야 합니다.

---

## 비동기 처리 적용 사례

### 실제 서비스에서의 비동기 처리

**1. 소셜 미디어 피드**
- 스크롤하면서 새로운 콘텐츠를 비동기적으로 로드
- 무한 스크롤 기능

**2. 검색 자동완성**
- 사용자가 입력하는 동안 실시간으로 추천 검색어를 제공
- 입력할 때마다 서버에 요청을 보내지만 타이핑을 방해하지 않음

**3. 대시보드**
- 여러 데이터 소스에서 정보를 비동기적으로 가져와 표시
- 각 위젯이 독립적으로 로드됨

**4. 실시간 채팅**
- 새 메시지를 주기적으로 확인하고 표시
- 메시지를 보내는 동안에도 다른 메시지를 받을 수 있음

**5. 이메일 클라이언트**
- 메일 목록을 보는 동안 백그라운드에서 새 메일 확인
- 첨부파일 다운로드 중에도 다른 메일을 읽을 수 있음

---

## 비동기 처리 주의사항

### 비동기 처리가 항상 최선은 아니다

**작업의 특성과 데이터의 중요도에 따라 적절히 선택해야 함**

#### 예시: 비동기 결제 처리

```javascript
// 1. (비동기) PG사(결제 대행사)에 결제 요청을 보냄
paymentAPI.request(orderData)
  .then(response => {
    // 2. (비동기) 결제 성공/실패 응답을 받음
    if (response.status === 'success') {
      // 3. (동기) 응답이 '성공'일 경우 우리 서버 데이터베이스에 
      //    주문 상태를 '결제 완료'로 기록
      return updateOrderStatus(response.orderId, 'paid')
    }
  })
  .then(result => {
    // 4. (동기) 사용자에게 '결제 완료' 페이지를 보여줌
    showCompletePage()
  })
  .catch(error => {
    showErrorPage()
  })
```

> **💡 핵심**: 하나의 작업이 완전히 끝난 것을 확인한 후 다음 작업을 순차적으로 실행해야 함

**동기적으로 처리해야 하는 경우:**
- 결제 처리와 같은 중요한 트랜잭션
- 순서가 중요한 데이터 처리
- 이전 단계의 결과가 다음 단계에 반드시 필요한 경우

**비동기적으로 처리할 수 있는 경우:**
- UI 업데이트
- 로그 전송
- 통계 데이터 수집
- 사용자 경험에 직접적인 영향을 주지 않는 작업

---

## 확인 문제

### 문제

**1. 한 작업이 끝날 때까지 기다리지 않고 다음 작업을 실행하는 방식은?**
- a) 동기 방식
- b) 비동기 방식 ✅
- c) 순차 방식
- d) 블로킹 방식

**2. JS 런타임에서 비동기 작업을 처리하는 곳은?**
- a) Call Stack
- b) Web API ✅
- c) Task Queue
- d) Event Loop

**3. 완료된 비동기 작업의 콜백 함수가 대기하는 곳은?**
- a) Call Stack
- b) Web API
- c) Task Queue ✅
- d) Event Loop

**4. Ajax 기술의 주된 목적은 무엇인가요?**
- a) 페이지 전체를 새로고침
- b) 서버 없이 웹페이지 동작
- c) 페이지 일부만 비동기 갱신 ✅
- d) JavaScript 코드 압축

**5. Promise 기반으로 Ajax 통신을 쉽게 하도록 돕는 라이브러리는?**
- a) jQuery
- b) Lodash
- c) Axios ✅
- d) React

**6. Axios 요청이 성공했을 때 실행되는 메서드는?**
- a) .then() ✅
- b) .catch()
- c) .finally()
- d) .error()

**7. Axios 요청이 실패했을 때 실행되는 메서드는?**
- a) .then()
- b) .catch() ✅
- c) .finally()
- d) .success()

**8. 콜백 함수가 계속 중첩되어 코드 가독성이 떨어지는 문제는?**
- a) 콜백 천국 (Callback Heaven)
- b) 콜백 지옥 (Callback Hell) ✅
- c) 콜백 체인 (Callback Chain)
- d) 콜백 루프 (Callback Loop)

**9. 비동기 작업의 최종 완료 또는 실패를 나타내는 객체는?**
- a) Callback
- b) AJAX
- c) Promise ✅
- d) Event

**10. Promise의 장점이 아닌 것은?**
- a) 콜백 지옥 문제 해결
- b) 비동기 코드의 순차적 표현
- c) 에러 처리의 일원화
- d) 항상 동기적으로 동작 ✅

### 정답 및 해설

**1. b) 비동기 방식**
- 비동기 방식은 특정 작업의 완료를 기다리지 않고 다른 작업을 동시에 수행하여 효율성을 높입니다.

**2. b) Web API**
- 브라우저 환경의 Web API가 시간이 걸리는 비동기 작업을 JavaScript 엔진 대신 처리합니다.

**3. c) Task Queue**
- Web API에서 완료된 비동기 작업의 콜백 함수가 Task Queue에서 순서를 기다립니다.

**4. c) 페이지 일부만 비동기 갱신**
- Ajax는 페이지 전체를 새로고침하지 않고 필요한 데이터만 비동기적으로 받아와 화면 일부를 갱신합니다.

**5. c) Axios**
- Axios는 Promise 기반의 HTTP 클라이언트 라이브러리로 간편하게 비동기 통신을 구현할 수 있습니다.

**6. a) .then()**
- then() 메서드는 Promise가 성공적으로 이행되었을 때 실행될 콜백 함수를 등록합니다.

**7. b) .catch()**
- catch() 메서드는 Promise가 실패(거부)했을 때 실행될 에러 처리 콜백 함수를 등록합니다.

**8. b) 콜백 지옥 (Callback Hell)**
- 비동기 처리를 위해 콜백 함수가 계속 중첩되면 코드의 가독성이 떨어지고 유지보수가 어려워집니다.

**9. c) Promise**
- Promise는 비동기 작업의 결과를 나타내는 객체로 콜백 지옥 문제를 해결하기 위해 등장했습니다.

**10. d) 항상 동기적으로 동작**
- Promise는 비동기 작업의 결과를 나타내는 객체로 비동기 처리를 위해 사용됩니다.

---

## 핵심 정리

### 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| **비동기 처리** | 다음 작업을 기다리지 않고 동시 처리 | `setTimeout(func, 3000)` |
| **이벤트 루프** | 콜 스택이 비면 큐의 작업을 이동 | Call Stack, Web API, Task Queue |
| **Ajax** | 페이지 새로고침 없이 데이터 교환 | 실시간 검색어 순위, 지도 이동 |
| **Axios** | Promise 기반의 HTTP 요청 라이브러리 | `axios.get(URL)` |
| **Promise** | 비동기 작업의 결과를 나타내는 객체 | `axios.get(URL).then(func)` |

---

## 요약 및 정리

### 동기와 비동기

**동기 (Synchronous)**
- 프로그램의 실행 흐름이 순서대로 진행되는 방식
- 하나의 작업이 끝나야 다음 작업을 시작

**비동기 (Asynchronous)**
- 특정 작업이 끝날 때까지 기다리지 않고 다음 작업을 바로 실행하는 방식
- 시간이 오래 걸리는 작업은 백그라운드에서 처리하고 프로그램은 멈추지 않고 다른 작업을 계속 수행할 수 있어 사용자 경험을 향상

### JavaScript의 비동기 처리

**JavaScript는 한 번에 하나의 일만 처리할 수 있는 싱글 스레드(Single Thread) 언어**

하지만 브라우저나 Node.js 같은 JavaScript 런타임 환경 덕분에 비동기 처리가 가능

**이벤트 루프 (Event Loop)**

JavaScript 런타임은 다음과 같은 요소들로 비동기 동작을 관리:

- **Call Stack**: 실행할 코드(함수)가 순서대로 쌓이는 공간
- **Web API**: setTimeout이나 Ajax 요청 같은 비동기 작업을 처리하는 곳
- **Task Queue**: Web API에서 처리된 비동기 작업의 콜백 함수가 대기하는 줄
- **Event Loop**: Call Stack이 비어 있을 때, Task Queue에 있는 콜백 함수를 Call Stack으로 옮겨 실행시키는 역할

### Ajax와 Axios

**Ajax (Asynchronous JavaScript and XML)**
- 웹 페이지 전체를 새로고침하지 않고 백그라운드에서 서버와 데이터를 주고받아 페이지의 일부만 동적으로 업데이트하는 기술

**Axios**
- Ajax 통신을 쉽게 할 수 있도록 도와주는 JavaScript 라이브러리
- Promise를 기반으로 동작하여 비동기 HTTP 요청을 간편하게 처리

### 비동기 처리 관리: Callback과 Promise

**비동기 콜백**
- 비동기 작업이 완료된 후 실행될 함수를 미리 정의하여 전달하는 방식
- 하지만 여러 비동기 작업을 순차적으로 처리할 때 콜백 함수가 계속 중첩되어 코드가 깊어지는 콜백 지옥(Callback Hell) 문제가 발생할 수 있음

**Promise**
- 콜백 지옥을 해결하기 위해 등장한 객체로 비동기 작업의 최종 성공 또는 실패를 의미
- `then(callback)`: Promise가 성공적으로 완료되었을 때 실행할 콜백 함수를 등록
- `catch(callback)`: Promise가 실패했을 때 실행할 콜백 함수를 등록
- **Promise Chaining**: then 메서드를 체인처럼 연결하여 여러 비동기 작업을 순서대로 가독성 높게 처리 가능

---

## 마무리

**"아래 코드의 실행 결과는 무엇일까요?"**

```javascript
console.log('A');
setTimeout(() => {
  console.log('B');
}, 1000);
console.log('C');
```

**답: A -> C -> B**

**동작 과정:**

1. `console.log('A')`와 `console.log('C')`는 즉시 콜 스택(Call Stack)에서 실행됩니다.

2. `setTimeout`은 Web API로 보내져 타이머가 동작하고 지정된 시간이 지난 후 콜백 함수가 Task Queue로 이동하여 대기합니다.

3. 이벤트 루프는 Call Stack을 살펴보다가 Call Stack이 비게 되면 Task Queue의 작업을 콜 스택으로 옮겨 `console.log('B')`가 마지막으로 실행됩니다.

---

**작성일**: 2024  
**과정**: SSAFY JavaScript AJAX
