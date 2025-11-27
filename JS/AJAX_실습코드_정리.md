# JavaScript AJAX 실습코드 정리

## 📚 목차

1. [동기 vs 비동기 처리](#1-동기-vs-비동기-처리)
   - 01-synchronous.html
   - 02-asynchronous.html
2. [Axios 기본 사용법](#2-axios-기본-사용법)
   - 03-axios.html
   - 04-cat-api.html
3. [Axios 실전 활용](#3-axios-실전-활용)
   - 05-cat-api-ad.html (실습 문제)
   - 05-sol-cat-api-ad.html (해답)
4. [비동기 콜백](#4-비동기-콜백)
   - 06-async-callback.html
5. [Promise Chaining](#5-promise-chaining)
   - 07-cat-api-ad-chaining.html
6. [Promise 심화](#6-promise-심화)
   - 99_1_promise.html
7. [async/await 기본](#7-asyncawait-기본)
   - 99_2_async_await_basic.html
8. [async/await 실전](#8-asyncawait-실전)
   - 99_3_async_await_cat_api.html
9. [Promise 고급 메서드](#9-promise-고급-메서드)
   - 99_4_promise_ad.html

---

## 1. 동기 vs 비동기 처리

### 01-synchronous.html - 동기 처리 예제

**교안 참조**: JavaScript_AJAX.md - "Synchronous 란?" 섹션

**학습 목표**: 동기 방식에서는 작업이 순차적으로 실행되며, 하나의 작업이 완료될 때까지 다음 작업이 대기함을 이해

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

    // 출력결과
    // 작업 1 시작
    // (반복 실행 동안 잠시 대기)
    // 작업 완료
    // 작업 2 시작
  </script>
</body>

</html>
```

**핵심 개념**:
- 동기(Synchronous) 방식은 코드가 **위에서 아래로 순차적으로** 실행됨
- `syncTask()` 함수의 긴 반복문이 끝날 때까지 다음 줄이 실행되지 않음
- 실행 순서가 보장되지만, **시간이 오래 걸리는 작업이 있으면 전체 프로그램이 멈춤**

**실생활 비유**: 
카페에서 손님 1의 커피가 완성될 때까지 손님 2는 주문조차 할 수 없는 상황

---

### 02-asynchronous.html - 비동기 처리 예제

**교안 참조**: JavaScript_AJAX.md - "Asynchronous 란?" 섹션

**학습 목표**: 비동기 방식에서는 시간이 걸리는 작업을 백그라운드에서 처리하고, 다른 작업을 계속 실행할 수 있음을 이해

```html
<!-- asynchrounous.html -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <script>
    console.log('작업 1 시작')

    const asyncTask = function (callBack) {
      setTimeout(() => {
        callBack('작업 완료')
      }, 3000)
    }

    asyncTask((result) => {
      console.log(result)
    })

    console.log('작업 2 시작')

    // 출력결과
    // 작업 1 시작
    // 작업 2 시작
    // 작업 완료
  </script>
</body>

</html>
```

**핵심 개념**:
- 비동기(Asynchronous) 방식은 시간이 걸리는 작업을 **백그라운드에서 처리**
- `setTimeout`은 3초를 기다리지만, 그동안 다음 코드(`console.log('작업 2 시작')`)가 먼저 실행됨
- 3초 후 콜백 함수가 실행되어 '작업 완료'가 출력됨

**실행 흐름**:
1. `console.log('작업 1 시작')` 실행 → Call Stack
2. `setTimeout`이 Web API로 전달됨 → 백그라운드에서 3초 타이머 시작
3. `console.log('작업 2 시작')` 실행 → Call Stack
4. 3초 후 콜백 함수가 Task Queue로 이동
5. Event Loop가 Call Stack이 비었을 때 콜백 함수를 Call Stack으로 이동
6. `console.log(result)` 실행 → '작업 완료' 출력

**실생활 비유**: 
카페에서 손님 1이 커피를 기다리는 동안 손님 2가 주문할 수 있고, 커피가 완성되면 진동벨로 알려주는 상황

---

## 2. Axios 기본 사용법

### 03-axios.html - Axios로 API 호출하기

**교안 참조**: JavaScript_AJAX.md - "Axios" 섹션

**학습 목표**: 
- Axios를 이용한 HTTP 요청 방법 이해
- Promise 객체와 .then()/.catch() 사용법 학습

```html
<!-- axios.html -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 1. axios 호출 결과를 변수에 저장하면 Promise 객체가 담김
    const promiseObj = axios({
      method: 'get',
      url: 'https://api.thecatapi.com/v1/images/search'
    })

    console.log(promiseObj) // Promise object

    // Promise 객체의 결과를 받으려면 .then() 사용
    promiseObj
      .then((response) => {
        console.log(response) // Response object
        console.log(response.data)  // Response data
      })
      .catch((error) => {
        console.error(error)
      })

    // // 2. 보통은 변수에 저장하지 않고 바로 체이닝
    // axios({
    //   method: 'get',
    //   url: 'https://api.thecatapi.com/v1/images/search'
    // })
    //   .then((response) => {
    //     console.log(response)
    //     console.log(response.data)
    //   })
    //   .catch((error) => {
    //     console.error(error)
    //   })
  </script>

</body>

</html>
```

**핵심 개념**:
- **Axios**는 Promise 기반의 HTTP 클라이언트 라이브러리
- `axios()` 함수를 호출하면 **Promise 객체**를 반환
- Promise는 비동기 작업의 완료 또는 실패를 나타내는 객체
- `.then(callback)`: 요청이 **성공**했을 때 실행
- `.catch(callback)`: 요청이 **실패**했을 때 실행

**Axios 기본 구조**:
```javascript
axios({
  method: 'HTTP 메서드',  // get, post, put, delete 등
  url: '요청할 URL'
})
  .then((response) => {
    // 성공 시 실행할 코드
    // response.data에 서버가 보낸 데이터가 담김
  })
  .catch((error) => {
    // 실패 시 실행할 코드
  })
```

**교안 연결**:
- **JavaScript_AJAX.md**의 "Axios 기본 구조" 참조
- Promise의 3가지 상태: Pending(대기), Fulfilled(성공), Rejected(실패)

---

### 04-cat-api.html - 비동기 실행 순서 확인

**교안 참조**: JavaScript_AJAX.md - "Axios 활용" 섹션

**학습 목표**: Axios 요청이 비동기로 처리되어 코드 실행 순서가 보장되지 않음을 이해

```html
<!-- cat-api.html -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    axios({
      method: 'get',
      url: 'https://api.thecatapi.com/v1/images/search',
    })
      .then((response) => {  // 성공한 경우
        console.log(response)
        console.log(response.data)
      })
      .catch((error) => {  // 실패한 경우
        console.log(error)
        console.log('실패했다옹')
      })
    console.log('야옹야옹')
  </script>
</body>

</html>
```

**실행 결과**:
```
야옹야옹
[Response 객체]
[Response.data 배열]
```

**핵심 개념**:
- `axios()` 호출 후 **즉시 다음 줄로 넘어감** (비동기 처리)
- `console.log('야옹야옹')`이 **먼저 실행됨**
- API 응답이 도착하면 그때 `.then()` 내부 코드가 실행됨

**실행 흐름**:
1. `axios()`가 Web API로 전달됨 (HTTP 요청 시작)
2. `console.log('야옹야옹')` 즉시 실행
3. 서버로부터 응답이 오면 `.then()` 내부 코드 실행

**교안 연결**:
- **JavaScript_AJAX.md**의 "정리" 부분 참조
- Event Loop와 Call Stack, Web API, Task Queue의 동작 원리

---

## 3. Axios 실전 활용

### 05-cat-api-ad.html - 실습 문제

**교안 참조**: JavaScript_AJAX.md - "고양이 이미지 가져오기 실습" 섹션

**학습 목표**: 이벤트와 Axios를 결합하여 사용자 인터랙션에 반응하는 웹 페이지 만들기

```html
<!-- cat-api-ad.html -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <button>냥냥펀치</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 목표: 버튼을 누르면 고양이 이미지를 출력하기
    // 주소: https://api.thecatapi.com/v1/images/search

  </script>
</body>

</html>
```

**문제**:
1. 버튼 요소를 선택하기
2. 버튼에 클릭 이벤트 리스너 추가하기
3. 클릭 시 Axios로 고양이 API 호출하기
4. 받은 이미지 URL로 `<img>` 태그 생성하여 화면에 추가하기

---

### 05-sol-cat-api-ad.html - 해답

**교안 참조**: JavaScript_AJAX.md - "고양이 이미지 가져오기 실습" 섹션

**학습 목표**: DOM 조작과 Axios를 결합한 실전 예제

```html
<!-- cat-api-ad.html -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <button>냥냥펀치</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const btn = document.querySelector('button')

    const getCats = function () {
      axios({
        method: 'get',
        url: 'https://api.thecatapi.com/v1/images/search'
      })
        .then((response) => {
          // 1. 응답 데이터에서 이미지 URL 추출
          const imgUrl = response.data[0].url
          
          // 2. img 태그 생성
          const imgElem = document.createElement('img')
          
          // 3. src 속성 설정
          imgElem.setAttribute('src', imgUrl)
          
          // 4. body에 추가
          document.body.appendChild(imgElem)
        })
        .catch((error) => {
          console.log(error)
          console.log('실패했다옹')
        })
      console.log('야옹야옹')
    }

    btn.addEventListener('click', getCats)
  </script>
</body>

</html>
```

**핵심 개념**:
- **이벤트 리스너**로 사용자 클릭에 반응
- **Axios**로 외부 API 데이터 가져오기
- **DOM 조작**으로 동적으로 이미지 추가

**실행 흐름**:
1. 버튼 클릭
2. `getCats` 함수 실행
3. `console.log('야옹야옹')` 즉시 출력 (비동기!)
4. API 요청 → 응답 대기
5. 응답 도착 → `.then()` 실행
6. 이미지 요소 생성 및 화면에 추가

**주의사항**:
- `console.log('야옹야옹')`은 이미지가 화면에 나타나기 **전**에 출력됨
- 이미지 로딩은 비동기적으로 처리되기 때문

**교안 연결**:
- **JavaScript_AJAX.md**의 "고양이 이미지 가져오기 실습" 참조
- **DOM01.md**의 DOM 조작 메서드 참조

---

## 4. 비동기 콜백

### 06-async-callback.html - 콜백 함수로 비동기 처리

**교안 참조**: JavaScript_AJAX.md - "비동기 콜백" 섹션

**학습 목표**: 콜백 함수를 이용한 비동기 처리 방법 이해

```html
<!-- async-callback.html -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <script>
    const asyncTask = function (callBack) {
      setTimeout(function () {
        console.log('비동기 작업 완료')
        callBack()
      }, 2000)
    }

    asyncTask(function () {
      console.log('작업 완료 후 콜백 실행')
    })
  </script>
</body>

</html>
```

**핵심 개념**:
- **콜백 함수**: 다른 함수의 인자로 전달되어 나중에 실행되는 함수
- 비동기 작업이 완료된 후 실행할 코드를 콜백 함수로 전달
- 2초 후 '비동기 작업 완료' → '작업 완료 후 콜백 실행' 순서로 출력

**콜백의 문제점 - 콜백 지옥(Callback Hell)**:
```javascript
// 여러 비동기 작업을 순차적으로 처리하면...
work1(function(result1) {
  work2(result1, function(result2) {
    work3(result2, function(result3) {
      work4(result3, function(result4) {
        console.log(result4)
      })
    })
  })
})
```
→ 코드가 점점 깊어져서 **가독성이 떨어지고 유지보수가 어려움**

**해결책**: Promise 사용!

**교안 연결**:
- **JavaScript_AJAX.md**의 "비동기 콜백" 섹션
- **JavaScript_AJAX.md**의 "콜백 지옥(Callback Hell)" 설명

---

## 5. Promise Chaining

### 07-cat-api-ad-chaining.html - Promise 체이닝

**교안 참조**: JavaScript_AJAX.md - "Promise chaining" 섹션

**학습 목표**: Promise chaining을 사용하여 여러 비동기 작업을 순차적으로 처리

```html
<!-- cat-api-ad.html -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <button>냥냥펀치</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const btn = document.querySelector('button')

    const getCats = function () {
      axios({
        method: 'get',
        url: 'https://api.thecatapi.com/v1/images/search'
      })
        .then((response) => {
          // 첫 번째 then: 데이터 추출
          const imgUrl = response.data[0].url
          return imgUrl  // 다음 then으로 전달
        })
        .then((url) => {
          // 두 번째 then: DOM 조작
          const imgElem = document.createElement('img')
          imgElem.setAttribute('src', url)
          document.body.appendChild(imgElem)
        })
        .catch((error) => {
          console.log(error)
          console.log('실패했다옹')
        })
      console.log('야옹야옹')
    }

    btn.addEventListener('click', getCats)
  </script>
</body>

</html>
```

**핵심 개념**:
- **Promise Chaining**: `.then()`을 연결하여 비동기 작업을 순차적으로 처리
- 각 `.then()`은 **이전 then의 return 값**을 다음 then의 인자로 받음
- 하나의 `.catch()`로 **모든 에러를 처리** 가능

**장점**:
1. **코드 가독성** 향상 (콜백 지옥 해결)
2. **작업 순서 보장**
3. **에러 처리 간편화**

**비교**:

**05-sol-cat-api-ad.html 방식**:
```javascript
.then((response) => {
  const imgUrl = response.data[0].url
  const imgElem = document.createElement('img')
  imgElem.setAttribute('src', imgUrl)
  document.body.appendChild(imgElem)
})
```

**07-cat-api-ad-chaining.html 방식**:
```javascript
.then((response) => {
  const imgUrl = response.data[0].url
  return imgUrl
})
.then((url) => {
  const imgElem = document.createElement('img')
  imgElem.setAttribute('src', url)
  document.body.appendChild(imgElem)
})
```

→ **관심사를 분리**하여 각 단계가 명확해짐

**교안 연결**:
- **JavaScript_AJAX.md**의 "Promise chaining" 섹션
- **JavaScript_AJAX.md**의 "then & catch의 chaining" 설명

---

## 6. Promise 심화

### 99_1_promise.html - Promise 객체 직접 만들기

**교안 참조**: JavaScript_AJAX.md - "프로미스" 섹션

**학습 목표**: 
- Promise 객체를 직접 생성하는 방법 학습
- resolve와 reject의 사용법 이해
- Promise chaining으로 여러 비동기 작업을 순차 처리

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
    // axios 는 이미 Promise를 예쁘게 포장해서 건네주는 라이브러리
    // 실무에서 직접적으로 setTimeout과 같은 비동기 함수를 직접 Promise로 감싸야 하는 순간이 옴

    // Promise 객체를 직접 만들고, 반환하는 비동기 함수를 만들어보자.
    // 예시) 랜덤으로 실패하는 함수
    function getRandomData() {
        return new Promise((resolve, reject) => {
            const success = Math.random() > 0.5;
            
            setTimeout(() => {
            if (success) {
                resolve("데이터 도착!"); // 성공 -> .then
            } else {
                reject("에러 발생!"); // 실패 -> .catch
            }
            }, 1000);
        });
    }
    
    /////////////////////////////////////////////////////
    // 랜덤으로 실패하는 함수를 호출
    getRandomData()
    .then(data => console.log(data))
    .catch(err => console.log(err));


    ////////////////////////////////
    // 3번 연속 호출해야 하는 경우 
    getRandomData()
    .then(data1 => {
        console.log("1번째 성공:", data1);
        console.log("--- 2. 시도 시작 ---");
        return getRandomData(); 
    })
    .then(data2 => {
        console.log("2번째 성공:", data2);
        console.log("--- 3. 시도 시작 ---");
        return getRandomData();
    })
    .then(data3 => {
        console.log("3번째 성공:", data3);
        console.log("=== 모든 작업 완료 ===");
    })
    .catch(err => {
        // 1, 2, 3번 중 하나라도 실패하면 바로 여기로 옴
        console.log("중간에 실패함:", err);
    });

</script>
</body>
</html>
```

**핵심 개념**:

**1. Promise 객체 생성**:
```javascript
new Promise((resolve, reject) => {
  // 비동기 작업 수행
  
  if (성공) {
    resolve(결과값)  // 성공 → .then()으로 전달
  } else {
    reject(에러)     // 실패 → .catch()로 전달
  }
})
```

**2. Promise의 3가지 상태**:
- **Pending(대기)**: 초기 상태, 비동기 작업 진행 중
- **Fulfilled(이행)**: 작업 성공, `resolve()` 호출됨
- **Rejected(거부)**: 작업 실패, `reject()` 호출됨

**3. Promise Chaining**:
```javascript
getRandomData()
  .then(data1 => {
    console.log("1번째 성공:", data1);
    return getRandomData();  // 다음 then으로 Promise 전달
  })
  .then(data2 => {
    console.log("2번째 성공:", data2);
    return getRandomData();
  })
  .then(data3 => {
    console.log("3번째 성공:", data3);
  })
  .catch(err => {
    // 어느 단계에서든 실패하면 여기로 옴
    console.log("중간에 실패함:", err);
  });
```

**실행 흐름**:
1. 첫 번째 `getRandomData()` 호출 → 1초 대기
2. 성공하면 "1번째 성공" 출력, 두 번째 `getRandomData()` 반환
3. 두 번째 작업 성공하면 "2번째 성공" 출력, 세 번째 `getRandomData()` 반환
4. 세 번째 작업 성공하면 "3번째 성공", "모든 작업 완료" 출력
5. **중간에 하나라도 실패하면** 나머지 `.then()`은 건너뛰고 `.catch()` 실행

**교안 연결**:
- **JavaScript_AJAX.md**의 "프로미스" 섹션
- **JavaScript_AJAX.md**의 "Promise의 3가지 상태" 참조

---

## 7. async/await 기본

### 99_2_async_await_basic.html - async/await 문법

**교안 참조**: JavaScript_AJAX.md (async/await 관련 내용은 교안에 없지만, Promise의 발전된 형태)

**학습 목표**: 
- async/await 문법으로 비동기 코드를 동기 코드처럼 작성
- try-catch로 에러 처리하기

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
        /*
        then 을 사용하면 코드도 길어지고, 디버깅도 어렵고, 흐름 제어하기도 까다롭다!
        비동기 코드를 동기 코드처럼 작성하고 싶다. (파이썬처럼 그냥 위에서 아래로 흐르게 하고 싶다!)
        그래서 등장한 게 "async" 와 "await"
        
        async
        - 함수 선언부 앞에 작성
        - 함수 내부에서 await 키워드를 사용할 수 있게 해줌 (주된 이유)
        - async가 작성된 함수는 무조건 Promise 객체를 반환

        await
        - Promise 객체를 반환하는 함수 앞에 작성
        - Promise 객체가 완료(Resolve) 될 때까지 코드 실행을 잠시 멈추고, 결과가 나오면 값만 가져와서 반환 
            - 만약, await 앞의 함수가 Promise 객체를 반환하지 않으면 그냥 무시하고 넘어감
        - async 함수로 선언된 곳 안에서만 await를 사용할 수 있음
        */
        
        // [Async/Await 방식: 3번 연속 호출]
    
    //////////////////////////////////////////
    // 99.1 promise.html 파일을 async/await로 개선한 버전 
    function getRandomData() {
        return new Promise((resolve, reject) => {
            const success = Math.random() > 0.5;
            
            setTimeout(() => {
            if (success) {
                resolve("데이터 도착!"); // 성공 -> .then
            } else {
                reject("에러 발생!"); // 실패 -> .catch
            }
            }, 1000);
        });
    }

    async function main() {
        try {
            // 1번째 시도
            const data1 = await getRandomData(); // Wait!
            console.log("1번째 성공:", data1);

            // 2번째 시도
            const data2 = await getRandomData(); // Wait!
            console.log("2번째 성공:", data2);

            // 3번째 시도
            const data3 = await getRandomData(); // Wait!
            console.log("3번째 성공:", data3);
            
            // for (let i = 1; i <= 3; i++) {
            //     console.log(`--- ${i}번째 시도 시작 ---`);
                
            //     const data = await getRandomData(); 
            //     console.log(`${i}번째 성공:`, data);
            // }

        } catch (err) {
            console.log("중간에 실패함:", err);
        }
    }

    // 최상단이기 때문에 await를 작성하지 않아도 되고, 작성해도 됨
    main();  
    </script>
</body>
</html>
```

**핵심 개념**:

**1. async 키워드**:
```javascript
async function functionName() {
  // 함수 내부에서 await 사용 가능
  // 이 함수는 항상 Promise를 반환
}
```

**2. await 키워드**:
```javascript
const result = await somePromise();
// somePromise()가 완료될 때까지 기다림
// 완료되면 결과값을 result에 저장
// 그 다음 줄로 넘어감
```

**3. try-catch로 에러 처리**:
```javascript
try {
  const data = await somePromise();
  // 성공 시 실행
} catch (error) {
  // 실패 시 실행
  console.log(error);
}
```

**Promise vs async/await 비교**:

**Promise 방식 (99_1_promise.html)**:
```javascript
getRandomData()
  .then(data1 => {
    console.log("1번째 성공:", data1);
    return getRandomData();
  })
  .then(data2 => {
    console.log("2번째 성공:", data2);
    return getRandomData();
  })
  .then(data3 => {
    console.log("3번째 성공:", data3);
  })
  .catch(err => {
    console.log("중간에 실패함:", err);
  });
```

**async/await 방식 (99_2_async_await_basic.html)**:
```javascript
async function main() {
  try {
    const data1 = await getRandomData();
    console.log("1번째 성공:", data1);

    const data2 = await getRandomData();
    console.log("2번째 성공:", data2);

    const data3 = await getRandomData();
    console.log("3번째 성공:", data3);
  } catch (err) {
    console.log("중간에 실패함:", err);
  }
}
```

**async/await의 장점**:
1. **코드가 위에서 아래로 읽힘** (마치 동기 코드처럼)
2. **디버깅이 쉬움**
3. **가독성이 훨씬 좋음**
4. **조건문, 반복문 사용이 자연스러움**

**주의사항**:
- `await`는 반드시 `async` 함수 안에서만 사용 가능
- `await`는 Promise를 반환하는 함수 앞에서만 의미가 있음

---

## 8. async/await 실전

### 99_3_async_await_cat_api.html - 고양이 API with async/await

**교안 참조**: JavaScript_AJAX.md - "Axios 활용" (async/await 방식으로 변환)

**학습 목표**: 실제 API 호출을 async/await로 처리하기

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cat API (Async/Await)</title>
</head>

<body>
  <button>냥냥펀치</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const btn = document.querySelector('button')

    // 함수 앞에 async 키워드 추가
    const getCats = async function () {
      
      // 에러 처리를 위해 try-catch 블록 사용
      try {
        // Promise 객체를 반환하는 axios 함수 앞에 await를 붙여서, 결과가 반환될 때까지 대기 
        const response = await axios({
          method: 'get',
          url: 'https://api.thecatapi.com/v1/images/search'
        })

        // 4. 첫 번째 .then에서 하던 일 (데이터 가져오기)
        // await 덕분에 response 변수를 바로 사용할 수 있음
        const imgUrl = response.data[0].url

        // 5. 두 번째 .then에서 하던 일 (화면 그리기)
        const imgElem = document.createElement('img')
        imgElem.setAttribute('src', imgUrl)
        document.body.appendChild(imgElem)

        // [주의!] 원래 코드에서는 이 로그가 요청 보내자마자(이미지 뜨기 전) 나왔지만,
        // async/await에서는 여기까지 순서대로 실행되므로 "이미지가 뜬 뒤에" 나옵니다.
        // 결국 async/await 는 코드가 우리가 읽는 순서(위 -> 아래)대로 정확하게 실행시킨다는 장점이 있음 
        console.log('야옹야옹')

      } catch (error) {
        console.log(error)
        console.log('실패했다옹')
      }
    }

    btn.addEventListener('click', getCats)
  </script>
</body>

</html>
```

**기존 Promise 방식 (07-cat-api-ad-chaining.html)과 비교**:

**Promise 방식**:
```javascript
const getCats = function () {
  axios({ method: 'get', url: URL })
    .then((response) => {
      const imgUrl = response.data[0].url
      return imgUrl
    })
    .then((url) => {
      const imgElem = document.createElement('img')
      imgElem.setAttribute('src', url)
      document.body.appendChild(imgElem)
    })
    .catch((error) => {
      console.log('실패했다옹')
    })
  console.log('야옹야옹')  // 이미지 뜨기 전에 출력됨
}
```

**async/await 방식**:
```javascript
const getCats = async function () {
  try {
    const response = await axios({ method: 'get', url: URL })
    const imgUrl = response.data[0].url
    const imgElem = document.createElement('img')
    imgElem.setAttribute('src', imgUrl)
    document.body.appendChild(imgElem)
    console.log('야옹야옹')  // 이미지 뜬 후에 출력됨
  } catch (error) {
    console.log('실패했다옹')
  }
}
```

**핵심 차이점**:
1. **실행 순서 명확화**: async/await는 코드를 읽는 순서대로 실행
2. **변수 사용 간편**: 중간 return 없이 바로 변수에 할당
3. **에러 처리 통합**: try-catch로 모든 에러를 한 곳에서 처리

**주의사항**:
- Promise 방식에서는 `console.log('야옹야옹')`이 API 호출과 동시에 실행
- async/await 방식에서는 `await` 때문에 API 응답을 기다린 후 실행
- **실행 순서가 달라짐을 반드시 이해해야 함!**

---

## 9. Promise 고급 메서드

### 99_4_promise_ad.html - Promise.all, Promise.allSettled, Promise.race

**교안 참조**: JavaScript_AJAX.md (고급 Promise 메서드는 교안에 없는 추가 내용)

**학습 목표**: 
- 여러 Promise를 효율적으로 처리하는 방법
- Promise.all, Promise.allSettled, Promise.race의 차이 이해

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
        // 그러면 모든 곳에 async/await를 도배해야할까? 
        // 예시) 1초, 1.5초, 2초 걸리는 작업들을 다 처리한 후에 결과값을 출력해야 하는 경우
        function getBurger() {
            return new Promise(resolve => setTimeout(() => resolve("햄버거"), 1000));
        }
        function getFries() {
            return new Promise(resolve => setTimeout(() => resolve("감자튀김"), 1500));
        }
        function getCoke() {
            return new Promise(resolve => setTimeout(() => resolve("콜라"), 2000));
        }

        async function order() {
            console.time("주문 시간");

            const burger = await getBurger(); // 1초 대기
            const fries = await getFries();   // 1.5초 대기
            const coke = await getCoke();     // 2초 대기

            console.log(`${burger}, ${fries}, ${coke}`);
            console.timeEnd("주문 시간"); // 총 4.5초 이상 소요
        }

        // 함수 실행!
        // 워터폴 현상 발생!! => 서로 상관없는 작업들임에도 불구하고, 앞의 작업이 끝날 때까지 기다리는 비효율적인 현상
        order();


        // 해결 방법) Promise.all 활용
        // 순서를 고려하지 않고 호출해도 괜찮은 경우 사용 (함수 호출 순서가 중요하다면 await를 써야함)
        // 단점: 하나라도 실패하면 에러 발생 
        async function promiseAllOrder() {
            // 1. 주문을 전부 넣음 (Promise 객체 3개가 동시에 생성되면서 작업 시작)
            // await를 붙이지 않았으므로 멈추지 않고 변수에 'Promise 객체'가 담깁니다.
            const burgerPromise = getBurger();
            const friesPromise = getFries();
            const cokePromise = getCoke();

            // 2. Promise.all로 "이 3개가 다 끝날 때까지" 한 번만 기다림
            const [burger, fries, coke] = await Promise.all([getBurger(), getFries(), getCoke()]);

            console.log(result); // ["햄버거", "감자튀김", "콜라"]
            console.timeEnd("주문 시간"); // 약 2초 소요 (가장 오래 걸리는 작업 시간만큼만 걸림)
        }

        promiseAllOrder();

        ////////////////////////////
        // 알아두면 좋은 추가 Promise 메서드
        // 1. Promise.allSettled()
        const getCokeError = () => new Promise((_, reject) => setTimeout(() => reject(new Error("콜라 기계 고장")), 500));

        async function promiseSettledOrder() {
            const results = await Promise.allSettled([
                getBurger(), // 성공 (3초)
                getFries(),  // 성공 (1초)
                getCokeError()    // 실패 (0.5초)
            ]);

            /* status: pending(대기), fulfilled(성공), rejected(실패)
            [
                { status: 'fulfilled', value: '햄버거' },      // 성공
                { status: 'fulfilled', value: '감자튀김' },    // 성공
                { status: 'rejected', reason: Error: 콜라 기계 고장 } // 실패
            ]
            */
            console.log(results);

            // 성공한 음식만이라도 손님상에 내보내기
            const successMenu = results
                .filter(item => item.status === 'fulfilled') // 성공한 것만 필터링
                .map(item => item.value);

            console.log(`손님, 죄송하지만 콜라는 빼고 ${successMenu}만 준비했습니다.`);
        }

        promiseSettledOrder();

        ////////////////////////
        // 2. Promise.race()
        // 실제로는 주어진 시간안에 처리되지 않으면, 여러 다른 서버에 요청하는 용도로 사용

        // 2초 뒤에 무조건 에러
        const timeoutLimit = () => new Promise((_, reject) => {
            setTimeout(() => reject("주문 취소"), 2000);
        });

        async function promiseRaceOrder() {
            try {
                // 햄버거 (3초 걸림 - 느림)
                // 타임아웃 (2초 걸림 - 더 빠름)
                const winner = await Promise.race([
                    getBurger(), 
                    timeoutLimit()
                ]);
                
                // 햄버거가 2초보다 빨랐다면 여기가 실행되겠지만...
                console.log("받은 음식:", winner);

            } catch (error) {
                // 타임아웃(2초)이 햄버거(3초)보다 먼저 끝나서 '에러(reject)'
                console.log("결과:", error); // "시간 초과! 주문 취소"
            }
        }

        promiseRaceOrder();
    </script>
</body>
</html>
```

**핵심 개념**:

### 1. 워터폴 현상 문제

**문제 상황**:
```javascript
const burger = await getBurger();  // 1초 대기
const fries = await getFries();    // 1.5초 대기
const coke = await getCoke();      // 2초 대기
// 총 4.5초 소요
```

→ 서로 **독립적인 작업**인데도 순차적으로 기다림 (비효율적!)

### 2. Promise.all() - 병렬 처리

**해결책**:
```javascript
const [burger, fries, coke] = await Promise.all([
  getBurger(),   // 3개 동시 시작
  getFries(),
  getCoke()
]);
// 약 2초 소요 (가장 오래 걸리는 작업만큼만)
```

**특징**:
- 여러 Promise를 **동시에 실행**
- **모두 성공**하면 결과 배열 반환
- **하나라도 실패**하면 즉시 에러 발생 (나머지 무시)

**사용 시기**: 
- 서로 독립적인 여러 API 호출
- 모든 작업이 성공해야만 하는 경우

### 3. Promise.allSettled() - 실패 허용

```javascript
const results = await Promise.allSettled([
  getBurger(),    // 성공
  getFries(),     // 성공
  getCokeError()  // 실패
]);

// 결과: 
// [
//   { status: 'fulfilled', value: '햄버거' },
//   { status: 'fulfilled', value: '감자튀김' },
//   { status: 'rejected', reason: Error }
// ]
```

**특징**:
- **모든 Promise가 완료될 때까지 대기**
- 성공/실패 여부와 관계없이 **모든 결과를 반환**
- 각 결과는 `status`와 `value` 또는 `reason`을 포함

**사용 시기**: 
- 일부 실패해도 괜찮은 경우
- 성공한 작업만 추려서 처리하고 싶을 때

### 4. Promise.race() - 가장 빠른 것만

```javascript
const winner = await Promise.race([
  getBurger(),      // 3초
  timeoutLimit()    // 2초
]);
// timeoutLimit()이 먼저 완료 (에러 발생)
```

**특징**:
- 여러 Promise 중 **가장 먼저 완료된 것**의 결과만 반환
- 나머지는 무시됨

**사용 시기**: 
- 타임아웃 구현
- 여러 서버에 동시 요청 후 가장 빠른 응답 사용
- 속도 경쟁이 필요한 경우

**비교 정리**:

| 메서드 | 대기 조건 | 실패 처리 | 반환값 |
|--------|----------|----------|--------|
| **Promise.all** | 모두 완료 | 하나라도 실패 시 즉시 에러 | 모든 결과의 배열 |
| **Promise.allSettled** | 모두 완료 | 실패해도 계속 진행 | 모든 결과(성공/실패) 배열 |
| **Promise.race** | 첫 번째 완료 | 첫 번째 결과에 따름 | 첫 번째 결과만 |

---

## 🎯 학습 정리

### 비동기 처리 발전 과정

1. **콜백 함수** → 콜백 지옥 문제 발생
2. **Promise** → then/catch 체이닝으로 가독성 개선
3. **async/await** → 동기 코드처럼 작성 가능

### 각 방식의 장단점

**콜백 방식**:
- ✅ 단순한 비동기 처리에 적합
- ❌ 중첩되면 가독성 저하

**Promise 방식**:
- ✅ 콜백 지옥 해결
- ✅ 체이닝으로 순서 보장
- ❌ 코드가 길어질 수 있음

**async/await 방식**:
- ✅ 가독성 최고
- ✅ 동기 코드처럼 작성
- ✅ 디버깅 쉬움
- ❌ 병렬 처리 시 주의 필요 (Promise.all 활용)

### 실무 권장 사항

1. **새 코드는 async/await 사용**
2. **병렬 처리가 필요하면 Promise.all 활용**
3. **일부 실패 허용 시 Promise.allSettled**
4. **타임아웃 필요 시 Promise.race**

---

## 📝 참고 자료

**교안 참조**:
- JavaScript_AJAX.md - 전체 섹션
- DOM01.md - DOM 조작 메서드
- JavaScript_Controlling_Event.md - 이벤트 리스너

**API 테스트**:
- The Cat API: https://api.thecatapi.com/v1/images/search
- 무료로 사용 가능한 고양이 이미지 API

**MDN 문서**:
- Promise: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise
- async/await: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/async_function
- Fetch API: https://developer.mozilla.org/ko/docs/Web/API/Fetch_API

---

**작성일**: 2024  
**과정**: SSAFY JavaScript AJAX 실습
**기반 교안**: JavaScript_AJAX.md
