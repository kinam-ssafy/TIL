# JavaScript Ajax with Django

## 📚 목차

1. [Ajax와 서버](#ajax와-서버)
2. [Ajax with follow](#ajax-with-follow)
3. [비동기 팔로우 구현](#비동기-팔로우-구현)
4. [Ajax with likes](#ajax-with-likes)
5. [비동기 좋아요 구현](#비동기-좋아요-구현)
6. [핵심 정리](#핵심-정리)

---

## 🎯 학습 목표

- Django view에서 JsonResponse를 반환하여 비동기 요청에 응답한다.
- data-* 속성을 사용해 Django 데이터를 JavaScript로 전달한다.
- Axios 요청 시 헤더에 CSRF 토큰을 포함하여 전송할 수 있다.
- Axios를 활용해 팔로우 기능을 비동기적으로 구현할 수 있다.
- 서버의 JSON 응답을 받아 DOM을 동적으로 업데이트한다.
- 버블링을 활용해 여러 요소의 이벤트를 효율적으로 관리한다.

---

## 🌟 시작하기

인스타그램에서 '팔로우' 버튼을 클릭할 때, 페이지 새로고침 없이 버튼과 숫자만 바뀌는 기능, 어떻게 만들까요?

**이 기능은 브라우저(JavaScript)와 서버(Django)의 실시간 대화가 핵심입니다.**

1. 자바스크립트가 Axios로 Django에 "팔로우 요청"을 보내면  
   Django는 HTML 페이지 대신 처리 결과(JsonResponse)만 응답합니다.

2. 자바스크립트는 이 데이터를 받아 필요한 부분의 DOM만 직접 수정합니다.

이번 시간에는 Django와 JavaScript를 연결하는 방법을 학습합니다.

---

## Ajax와 서버

### [복습] Ajax란?

**Ajax (Asynchronous JavaScript and XML)**
- 비동기적인 웹 애플리케이션 개발을 위한 기술

**Ajax는 웹 페이지 전체를 새로고침하지 않고 백그라운드에서 서버와 데이터를 주고받는 비동기 통신 기술입니다.**

- 구글 지도 앱을 움직여도 끊김이 없고
- '좋아요'를 클릭할 때 페이지가 부분적으로만 바뀌는 것이 가능합니다.

즉, 웹 페이지를 데스크톱 애플리케이션처럼 동적이고 반응적으로 만들어주는 현대 웹의 핵심 기술 중 하나입니다.

### [복습] Ajax를 활용한 클라이언트-서버 간 동작

```
Client                          Server
  │                               │
  │  XHR 객체 생성 및 요청        │
  │  ──────────────────────────>  │
  │                               │
  │                               │  응답 데이터 생성
  │                               │  (JSON)
  │  <──────────────────────────  │
  │     JSON 데이터 응답          │
  │                               │
  │  Promise 객체를 활용해        │
  │  DOM 조작                     │
  │  (웹 페이지의 일부분만        │
  │   다시 로딩)                  │
```

---

## Ajax with follow

### 사전 준비

1. M:N 관계 모델링까지 진행된 Django 프로젝트 준비
2. 가상 환경 생성, 활성화 및 패키지 설치

---

## 비동기 팔로우 구현

### Ajax 적용 (1/14) - Axios CDN 작성

프로필 페이지에 axios CDN 작성

```html
<!-- accounts/profile.html -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
</script>
</body>
</html>
```

### Ajax 적용 (2/14) - QuerySelector

**QuerySelector**
- CSS 선택자에 맞는 첫 번째 HTML 요소를 찾아주는 명령어

**form 요소 선택을 위해 id 속성 지정 및 선택**

action과 method 속성은 삭제 → 요청은 axios로 대체할 예정

```html
<!-- accounts/profile.html -->
<form id="follow-form">
  {% csrf_token %}
  ...
</form>
```

```javascript
<!-- accounts/profile.html -->
const formTag = document.querySelector('#follow-form')
```

### Ajax 적용 (3/14) - preventDefault()

**preventDefault()**
- 이벤트에 할당된 브라우저의 기본 동작을 막는 명령어

**form 요소에 이벤트 핸들러 할당**

submit 이벤트의 기본 동작 취소하기

```javascript
<!-- accounts/profile.html -->
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
})
```

### Ajax 적용 (4/14) - axios 요청 코드 작성

```javascript
<!-- accounts/profile.html -->
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
  
  axios({
    method: 'post',
    url: `/accounts/${}/follow/`,
  })
})
```

**두 가지 문제:**
1. 요청 url에 필요한 사용자 pk는 어떻게 작성해야 할까?
2. CSRF 토큰은 어떻게 보내야 할까?

### Ajax 적용 (5/14) - url에 작성할 user pk 가져오기

**HTML → JavaScript로 데이터 전달**

```html
<!-- accounts/profile.html -->
<form id="follow-form" data-user-id="{{ person.pk }}">
  {% csrf_token %}
  ...
</form>
```

```javascript
<!-- accounts/profile.html -->
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
  
  // 세 가지 방법 모두 가능
  const userId = event.currentTarget.dataset.userId
  // const userId = this.dataset.userId
  // const userId = formTag.dataset.userId
})
```

### 'data-*' 속성

**data-* 속성**
- 사용자 지정 데이터 속성을 만들어 HTML과 DOM 사이에서 임의의 데이터를 교환하는 방법
- 모든 사용자 지정 데이터는 JavaScript에서 dataset 속성을 통해 접근

**주의사항:**
- 대소문자 여부에 상관없이 'xml' 문자로 시작 불가
- 세미콜론 포함 불가
- 대문자 포함 불가

```html
<div data-my-id="my-data"></div>

<script>
  const myId = event.target.dataset.myId
</script>
```

> **💡 참고**: [MDN data-* 속성 문서](https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*)

### Ajax 적용 (6/14) - 요청 url 작성 마무리

```javascript
<!-- accounts/profile.html -->
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
  
  const userId = event.currentTarget.dataset.userId
  
  axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
  })
})
```

### Ajax 적용 (7/14) - CSRF 토큰 가져오기

**문서상 input hidden 타입으로 존재하는 csrf token 데이터를 이제는 axios로 전송해야 함**

```html
<!-- accounts/profile.html -->
<form id="follow-form" data-user-id="1">
  <input 
    type="hidden" 
    name="csrfmiddlewaretoken" 
    value="naosSImLBsHaCR3oJPm3tcHDbgv52EfqD4XwBAprAKsYq1kM87jowjsgefg4wzbN"
  >
  
  {% if request.user in person.followers.all %}
    <input type="submit" value="UnFollow">
  {% else %}
    <input type="submit" value="Follow">
  {% endif %}
</form>
```

**input 요소를 선택해서 value 값을 가져오기**

### Ajax 적용 (8/14) - CSRF 토큰 선택

```javascript
<!-- accounts/profile.html -->
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
```

### Ajax 적용 (9/14) - CSRF 토큰을 axios 요청에 포함

```javascript
<!-- accounts/profile.html -->
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
  
  const userId = event.currentTarget.dataset.userId
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
  axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
    headers: {
      'X-CSRFToken': csrftoken,
    },
  })
})
```

### Ajax 적용 (10/14) - Django view 함수 수정

**기존 follow view 함수**

```python
# accounts/views.py
@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    
    return redirect('accounts:profile', person.username)
```

**수정된 follow view 함수**

```python
# accounts/views.py
from django.http import JsonResponse

@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
            is_followed = False
        else:
            person.followers.add(request.user)
            is_followed = True
    
    context = {
        'is_followed': is_followed,
        'followers_count': person.followers.count(),
        'followings_count': person.followings.count(),
    }
    
    return JsonResponse(context)
```

### Ajax 적용 (11/14) - 응답 데이터 확인

```javascript
<!-- accounts/profile.html -->
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
  
  const userId = event.currentTarget.dataset.userId
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
  axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
    headers: {
      'X-CSRFToken': csrftoken,
    },
  })
    .then((response) => {
      console.log(response)
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error)
    })
})
```

**개발자 도구에서 응답 데이터 확인:**
```javascript
{
  is_followed: true,
  followers_count: 1,
  followings_count: 0
}
```

### Ajax 적용 (12/14) - 팔로우 버튼 선택

```html
<!-- accounts/profile.html -->
<form id="follow-form" data-user-id="{{ person.pk }}">
  {% csrf_token %}
  
  {% if request.user in person.followers.all %}
    <input type="submit" value="UnFollow" id="follow-{{ person.pk }}">
  {% else %}
    <input type="submit" value="Follow" id="follow-{{ person.pk }}">
  {% endif %}
</form>
```

```javascript
<!-- accounts/profile.html -->
.then((response) => {
  const isFollowed = response.data.is_followed
  const followBtn = document.querySelector(`#follow-${userId}`)
})
```

### Ajax 적용 (13/14) - 버튼 텍스트 변경

```javascript
<!-- accounts/profile.html -->
.then((response) => {
  const isFollowed = response.data.is_followed
  const followBtn = document.querySelector(`#follow-${userId}`)
  
  if (isFollowed === true) {
    followBtn.value = 'UnFollow'
  } else {
    followBtn.value = 'Follow'
  }
})
```

### Ajax 적용 (14/14) - 팔로워 & 팔로잉 수 변경

```html
<!-- accounts/profile.html -->
<div>
  팔로잉: <span id="followings-count">{{ person.followings.all|length }}</span> /
  팔로워: <span id="followers-count">{{ person.followers.all|length }}</span>
</div>
```

```javascript
<!-- accounts/profile.html -->
.then((response) => {
  const isFollowed = response.data.is_followed
  const followersCount = response.data.followers_count
  const followingsCount = response.data.followings_count
  
  const followBtn = document.querySelector(`#follow-${userId}`)
  
  if (isFollowed === true) {
    followBtn.value = 'UnFollow'
  } else {
    followBtn.value = 'Follow'
  }
  
  const followersCountTag = document.querySelector('#followers-count')
  const followingsCountTag = document.querySelector('#followings-count')
  
  followersCountTag.textContent = followersCount
  followingsCountTag.textContent = followingsCount
})
```

### 비동기 팔로우 최종 코드

```javascript
<!-- accounts/profile.html -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const formTag = document.querySelector('#follow-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
  formTag.addEventListener('submit', function (event) {
    event.preventDefault()
    
    const userId = event.currentTarget.dataset.userId
    
    axios({
      method: 'post',
      url: `/accounts/${userId}/follow/`,
      headers: {
        'X-CSRFToken': csrftoken,
      },
    })
      .then((response) => {
        const isFollowed = response.data.is_followed
        const followersCount = response.data.followers_count
        const followingsCount = response.data.followings_count
        
        const followBtn = document.querySelector(`#follow-${userId}`)
        
        if (isFollowed === true) {
          followBtn.value = 'UnFollow'
        } else {
          followBtn.value = 'Follow'
        }
        
        const followersCountTag = document.querySelector('#followers-count')
        const followingsCountTag = document.querySelector('#followings-count')
        
        followersCountTag.textContent = followersCount
        followingsCountTag.textContent = followingsCount
      })
      .catch((error) => {
        console.log(error)
      })
  })
</script>
```

---

## Ajax with likes

### 비동기 좋아요 구현 개요

**상황:**
- 게시글 목록 페이지(index.html)에 여러 게시글이 있고
- 각 게시글마다 좋아요 버튼이 있음

**기존 팔로우와의 차이점:**
- 팔로우는 프로필 페이지에 버튼이 하나만 존재
- 좋아요는 한 페이지에 여러 개의 버튼이 존재

**구현 방법:**
- **이벤트 버블링(Event Bubbling)**을 활용하여 효율적으로 관리

---

## 비동기 좋아요 구현

### 비동기 좋아요 구현 - Ajax 적용 (1/12)

**index 페이지에 axios CDN 작성**

```html
<!-- articles/index.html -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
</script>
</body>
</html>
```

### Ajax 적용 (2/12) - 각 좋아요 form에 article pk 부여

```html
<!-- articles/index.html -->
{% for article in articles %}
  <div>
    <p>{{ article.user }}</p>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    
    <form class="like-forms" data-article-id="{{ article.pk }}">
      {% csrf_token %}
      
      {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
      {% else %}
        <input type="submit" value="좋아요" id="like-{{ article.pk }}">
      {% endif %}
    </form>
    <hr>
  </div>
{% endfor %}
```

### Ajax 적용 (3/12) - 이벤트 버블링을 활용한 이벤트 핸들러 등록

```javascript
<!-- articles/index.html -->
const articleContainer = document.querySelector('.article-container')

articleContainer.addEventListener('submit', function (event) {
  event.preventDefault()
  console.log(event.target)
})
```

**이벤트 버블링 (Event Bubbling):**
- 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고
- 이어서 부모 요소의 핸들러가 동작하는 현상
- 가장 최상단의 조상 요소를 만날 때까지 이 과정이 반복

### Ajax 적용 (4/12) - 이벤트가 form에서 발생했는지 확인

```javascript
<!-- articles/index.html -->
const articleContainer = document.querySelector('.article-container')

articleContainer.addEventListener('submit', function (event) {
  event.preventDefault()
  
  // 이벤트가 form 요소에서 발생했는지 확인
  if (event.target.classList.contains('like-forms')) {
    console.log('좋아요 form에서 발생')
  }
})
```

### Ajax 적용 (5/12) - axios 요청 작성

```javascript
<!-- articles/index.html -->
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

articleContainer.addEventListener('submit', function (event) {
  event.preventDefault()
  
  if (event.target.classList.contains('like-forms')) {
    const articleId = event.target.dataset.articleId
    
    axios({
      method: 'post',
      url: `/articles/${articleId}/likes/`,
      headers: {
        'X-CSRFToken': csrftoken,
      },
    })
  }
})
```

### Ajax 적용 (6/12) - Django view 함수 수정

```python
# articles/views.py
from django.http import JsonResponse

@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    
    context = {
        'is_liked': is_liked,
    }
    
    return JsonResponse(context)
```

### Ajax 적용 (7/12) - 응답 데이터 확인

```javascript
<!-- articles/index.html -->
axios({
  method: 'post',
  url: `/articles/${articleId}/likes/`,
  headers: {
    'X-CSRFToken': csrftoken,
  },
})
  .then((response) => {
    console.log(response)
    console.log(response.data)
  })
  .catch((error) => {
    console.log(error)
  })
```

### Ajax 적용 (8/12) - 좋아요 버튼 선택

```javascript
<!-- articles/index.html -->
.then((response) => {
  const isLiked = response.data.is_liked
  const likeBtn = document.querySelector(`#like-${articleId}`)
  
  console.log(likeBtn)
})
```

### Ajax 적용 (9/12) - 버튼 텍스트 변경

```javascript
<!-- articles/index.html -->
.then((response) => {
  const isLiked = response.data.is_liked
  const likeBtn = document.querySelector(`#like-${articleId}`)
  
  if (isLiked === true) {
    likeBtn.value = '좋아요 취소'
  } else {
    likeBtn.value = '좋아요'
  }
})
```

### Ajax 적용 (10/12) - 최종 코드

```javascript
<!-- articles/index.html -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const articleContainer = document.querySelector('.article-container')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
  articleContainer.addEventListener('submit', function (event) {
    event.preventDefault()
    
    if (event.target.classList.contains('like-forms')) {
      const articleId = event.target.dataset.articleId
      
      axios({
        method: 'post',
        url: `/articles/${articleId}/likes/`,
        headers: {
          'X-CSRFToken': csrftoken,
        },
      })
        .then((response) => {
          const isLiked = response.data.is_liked
          const likeBtn = document.querySelector(`#like-${articleId}`)
          
          if (isLiked === true) {
            likeBtn.value = '좋아요 취소'
          } else {
            likeBtn.value = '좋아요'
          }
        })
        .catch((error) => {
          console.log(error)
        })
    }
  })
</script>
```

### 버블링을 활용하지 않았다면? (1/3)

**1. 모든 좋아요 form에 각각 이벤트 핸들러를 직접 할당**

```javascript
<!-- articles/index.html -->
const likeForm1 = document.querySelector('#like-form-1')
const likeForm2 = document.querySelector('#like-form-2')
const likeForm3 = document.querySelector('#like-form-3')
// ...

likeForm1.addEventListener('submit', function (event) {
  // ...
})

likeForm2.addEventListener('submit', function (event) {
  // ...
})

likeForm3.addEventListener('submit', function (event) {
  // ...
})
```

**문제점:**
- 게시글이 많아질수록 코드가 길어짐
- 동적으로 추가되는 게시글에는 이벤트가 적용되지 않음
- 유지보수가 어려움

### 버블링을 활용하지 않았다면? (2/3)

**2. querySelectorAll을 사용해 전체 좋아요 버튼을 순회**

```javascript
<!-- articles/index.html -->
const formTags = document.querySelectorAll('.like-forms')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

formTags.forEach((formTag) => {
  formTag.addEventListener('submit', function (event) {
    event.preventDefault()
    
    const articleId = formTag.dataset.articleId
    
    axios({
      method: 'post',
      url: `/articles/${articleId}/likes/`,
      headers: {
        'X-CSRFToken': csrftoken,
      },
    })
      .then((response) => {
        const isLiked = response.data.is_liked
        const likeBtn = document.querySelector(`#like-${articleId}`)
        
        if (isLiked === true) {
          likeBtn.value = '좋아요 취소'
        } else {
          likeBtn.value = '좋아요'
        }
      })
  })
})
```

**문제점:**
- 각 form마다 이벤트 리스너를 등록해야 함
- 게시글이 100개면 100개의 이벤트 리스너가 생성됨
- 메모리 낭비
- 동적으로 추가되는 게시글에는 여전히 이벤트가 적용되지 않음

### 버블링을 활용하지 않았다면? (3/3)

**버블링 활용의 장점:**

✅ **하나의 이벤트 리스너로 모든 게시글 관리**
- 부모 요소 하나에만 이벤트 리스너 등록
- 메모리 효율적

✅ **동적으로 추가되는 게시글도 자동으로 처리**
- 새로운 게시글이 추가되어도 별도의 이벤트 등록 불필요

✅ **코드 간결성 및 유지보수 용이**
- 이벤트 핸들러 하나로 모든 게시글 처리

---

## 확인 문제

### 문제

**1. CSRF 문제를 해결하기 위해 axios 요청의 어느 부분에 토큰을 포함해야 하나요?**
- a) params
- b) data
- c) headers ✅
- d) url

**2. HTML 대신 JSON 형식의 데이터를 응답으로 보내기 위해 사용하는 클래스는?**
- a) HttpResponse
- b) JsonResponse ✅
- c) TemplateResponse
- d) FileResponse

**3. HTML 요소에 데이터를 저장하고 JS에서 이를 참조하기 위해 사용하는 속성은 무엇인가요?**
- a) id
- b) class
- c) data-* ✅
- d) name

**4. data-user-id="{{ person.pk }}"로 저장된 값을 JavaScript에서 가져오는 올바른 방법은?**
- a) event.target.userId
- b) event.target.data.userId
- c) event.target.dataset.userId ✅
- d) event.target.value.userId

**5. 한 페이지에 있는 여러 개의 '좋아요' 버튼을 효율적으로 관리하기 위한 가장 좋은 방법은?**
- a) 각 버튼에 개별적으로 addEventListener를 단다.
- b) querySelectorAll로 모든 버튼에 반복문으로 리스너를 단다.
- c) 버튼들의 공통 부모 요소에 addEventListener를 하나만 단다. ✅
- d) 각 버튼에 onclick 속성을 직접 작성한다.

**6. 이벤트 버블링을 활용할 때, 실제 클릭된 버튼을 특정하기 위해 사용하는 속성은?**
- a) event.target ✅
- b) event.currentTarget
- c) this
- d) event.parentElement

**7. 여러 개의 좋아요 버튼 중 특정 버튼의 value를 바꾸기 위해, 해당 버튼을 선택하는 방법은?**
- a) document.querySelector('input[type=submit]')
- b) document.querySelectorAll('.like-forms')
- c) document.querySelector('#like-' + articleId) ✅
- d) event.target.children[0]

**8. Django view 함수에서 요청이 Ajax인지 확인하는 방법으로 올바른 것은?**
- a) request.is_ajax()
- b) request.method == 'AJAX'
- c) request.headers.get('X-Requested-With') == 'XMLHttpRequest'
- d) 위 방법 모두 현재 Django에서 권장되지 않는다 ✅

**9. Django view에서 Ajax 요청에 대한 응답으로 팔로우 상태를 전달하려 합니다. context 딕셔너리로 가장 적절한 것은?**
- a) {'is_followed': True} ✅
- b) {'followed': 'ok'}
- c) {'status': 200}
- d) {'message': '성공'}

**10. 팔로워/언팔로우 후 팔로워 수를 화면에 비동기적으로 업데이트하려고 합니다. Django view에서 추가로 응답해야 할 데이터는?**
- a) person.username
- b) request.user.pk
- c) person.followers.count() ✅
- d) is_authenticated

### 정답 및 해설

**1. c) headers**
- CSRF 토큰은 보안을 위해 HTTP 요청의 헤더(headers)에 'X-CSRFToken'이라는 키로 포함하여 전송해야 합니다.

**2. b) JsonResponse**
- JsonResponse는 Python의 딕셔너리 같은 객체를 JSON 데이터 형식으로 변환하여 HTTP 응답을 생성합니다.

**3. c) data-***
- data-* 속성을 사용하면 HTML 요소에 사용자 정의 데이터를 저장하고 JS의 dataset 속성으로 쉽게 접근할 수 있습니다.

**4. c) event.target.dataset.userId**
- data- 뒤의 이름(user-id)이 카멜 케이스(userId)로 변환되어 dataset 객체의 속성으로 접근할 수 있습니다.

**5. c) 버튼들의 공통 부모 요소에 addEventListener를 하나만 단다**
- 이벤트 버블링을 활용하여 공통 부모에 이벤트 리스너를 하나만 등록하는 것이 가장 효율적이고 관리가 편합니다.

**6. a) event.target**
- event.target은 이벤트가 처음 발생한 가장 안쪽의 요소를 가리키므로 여러 버튼 중 어떤 버튼이 클릭됐는지 정확히 알 수 있습니다.

**7. c) document.querySelector('#like-' + articleId)**
- 각 버튼에 id="like-{{ article.pk }}"처럼 고유 ID를 부여하고 JS에서 해당 ID로 정확히 선택해야 합니다.

**8. d) 위 방법 모두 현재 Django에서 권장되지 않는다**
- 과거에는 is_ajax()나 헤더를 확인했지만, 최신 웹 개발에서는 fetch/axios 등 다양한 라이브러리를 사용하므로 더 이상 신뢰할 수 있는 방법이 아닙니다.

**9. a) {'is_followed': True}**
- JavaScript에서 명확하게 상태를 판단할 수 있도록 boolean 값을 담은 명시적인 키(key)를 사용하는 것이 좋습니다.

**10. c) person.followers.count()**
- 팔로우 상태 변경 후 갱신된 팔로워 수를 JavaScript로 전달해야 화면의 숫자도 업데이트할 수 있습니다.

---

## 핵심 정리

### 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| **JsonResponse** | JSON 형식으로 응답하는 객체 | `return JsonResponse(context)` |
| **data-* 속성** | HTML에 사용자 지정 데이터 저장 | `<div data-user-id="1">` |
| **CSRF 토큰 전송** | Axios 요청 헤더에 토큰을 포함 | `headers: {'X-CSRFToken': token}` |
| **XHR** | 서버와 비동기 통신하는 JS 객체 | 개발자 도구 Network 탭에서 확인 |
| **이벤트 버블링** | 이벤트가 부모로 전파되는 현상 | 공통 부모에 하나의 리스너 등록 |

---

## 요약 및 정리

### Ajax와 서버 연동

**Ajax 통신을 위해 Django 서버는 HTML 페이지가 아닌 데이터를 응답해야 함**

이때 JavaScript와 데이터를 주고받기 위한 몇 가지 방법이 필요:

#### JsonResponse
- Django view 함수에서 HTML을 렌더링하는 대신 JSON 형식의 데이터를 응답할 때 사용하는 객체

```python
context = {
    'is_followed': True,
    'followers_count': 10,
}
return JsonResponse(context)
```

#### data-* 속성
- HTML 요소에 `data-user-id="{{ user.pk }}"`와 같이 사용자 지정 데이터를 저장하는 방법
- JavaScript에서는 `element.dataset.userId`와 같이 dataset 속성을 통해 이 값에 접근 가능

```html
<form data-user-id="{{ person.pk }}">
```

```javascript
const userId = formTag.dataset.userId
```

#### CSRF 토큰
- input의 값을 가져온 후 Axios 요청의 headers에 `{ 'X-CSRFToken': csrftoken }` 형태로 포함하여 전송해야 함

```javascript
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

axios({
  headers: {
    'X-CSRFToken': csrftoken,
  },
})
```

---

### 비동기 팔로우 기능 구현

**기존의 동기 방식 팔로우 기능을 Ajax를 사용해 비동기 방식으로 전환하는 과정**

#### 클라이언트 (JavaScript)

1. form 태그에 submit 이벤트 리스너를 추가

2. `event.preventDefault()`를 호출하여 form의 기본 제출 동작(새로고침)을 막기

3. data-user-id 속성에서 팔로우할 사용자의 pk를 가져오기

4. CSRF 토큰을 가져와 Axios 요청 헤더에 포함하여 POST 요청을 보내기

5. 요청이 성공하면 `.then()` 블록에서 서버가 보낸 JsonResponse를 받기

6. 응답 받은 데이터 (is_followed, followers_count 등)를 사용해 팔로우 버튼의 문구와 팔로워 수를 동적으로 변경

```javascript
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
  
  const userId = event.currentTarget.dataset.userId
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
  axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
    headers: {
      'X-CSRFToken': csrftoken,
    },
  })
    .then((response) => {
      const isFollowed = response.data.is_followed
      const followersCount = response.data.followers_count
      
      const followBtn = document.querySelector(`#follow-${userId}`)
      
      if (isFollowed === true) {
        followBtn.value = 'UnFollow'
      } else {
        followBtn.value = 'Follow'
      }
      
      const followersCountTag = document.querySelector('#followers-count')
      followersCountTag.textContent = followersCount
    })
})
```

#### 서버 (Django)

1. follow view 함수에서 팔로워/언팔로우 로직을 처리

2. 처리 결과(팔로우 상태, 팔로워 수 등)를 담은 context 딕셔너리를 생성

3. redirect 대신 `JsonResponse(context)`를 반환하도록 수정

```python
@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
            is_followed = False
        else:
            person.followers.add(request.user)
            is_followed = True
    
    context = {
        'is_followed': is_followed,
        'followers_count': person.followers.count(),
        'followings_count': person.followings.count(),
    }
    
    return JsonResponse(context)
```

---

### 비동기 좋아요 기능 구현

**페이지에 여러 좋아요 버튼이 있을 때, 각 버튼마다 이벤트 리스너를 다는 것은 비효율적이므로 버블링 활용**

#### 구현 방식

1. 모든 좋아요 form을 감싸는 하나의 부모 요소(예: `<article class="article-container">`)에만 이벤트 리스너를 등록

2. 이벤트가 발생하면 버블링에 의해 부모 요소가 이벤트를 감지

3. 이벤트 핸들러 내에서 `event.target`을 사용하면, 실제로 어떤 자식 form에서 이벤트가 시작되었는지 알 수 있음

4. `event.target`을 이용해 해당 게시물의 pk를 얻고 이를 통해 서버에 비동기 요청을 보냄

5. 서버로부터 응답을 받으면 해당 articleId를 사용해 페이지에 있는 여러 버튼 중 하나를 선택하여 상태 업데이트

```javascript
const articleContainer = document.querySelector('.article-container')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

articleContainer.addEventListener('submit', function (event) {
  event.preventDefault()
  
  if (event.target.classList.contains('like-forms')) {
    const articleId = event.target.dataset.articleId
    
    axios({
      method: 'post',
      url: `/articles/${articleId}/likes/`,
      headers: {
        'X-CSRFToken': csrftoken,
      },
    })
      .then((response) => {
        const isLiked = response.data.is_liked
        const likeBtn = document.querySelector(`#like-${articleId}`)
        
        if (isLiked === true) {
          likeBtn.value = '좋아요 취소'
        } else {
          likeBtn.value = '좋아요'
        }
      })
  }
})
```

---

## 마무리

인스타그램에서 '팔로우' 버튼을 클릭할 때, 페이지 새로고침 없이 버튼과 숫자만 바뀌는 기능, 어떻게 만들까요?

### 전체 흐름 정리

```javascript
// 1. JavaScript → Django
axios({
  method: 'post',
  url: `/accounts/1/follow/`,
})
```

```python
# 2. Django → JavaScript
return JsonResponse({
  'is_followed': True,
  'followers_count': 100
})
```

```javascript
// 3. JavaScript → DOM 조작
const isFollowed = response.data.is_followed
const followBtn = document.querySelector(`#follow-${userId}`)
followBtn.value = 'UnFollow'
```

**핵심:**
1. 자바스크립트가 Axios로 Django에 "팔로우 요청"을 보냅니다.
2. Django는 HTML 페이지 대신 처리 결과(JsonResponse)만 응답합니다.
3. 자바스크립트는 이 데이터를 받아 필요한 부분의 DOM만 직접 수정합니다.

---

**작성일**: 2024  
**과정**: SSAFY JavaScript Ajax with Django
