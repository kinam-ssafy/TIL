# 강의 교안 확인 문제 정리

## Intro & DesignPattern

---

**1. 클라이언트와 서버 구조에서, 사용자의 요청을 받아 처리하는 역할을 하는 것은?**
a) 클라이언트
b) 서버
c) 프레임워크
d) 데이터베이스

**2. 웹 프레임워크의 주요 목적은?**
a) 웹 서버를 구축한다
b) 웹 개발에 필요한 코드를 줄이고 구조화를 돕는다
c) 운영 체제를 만든다
d) 하드웨어를 제어한다

**3. Django가 포함하는 구성요소 중 하나가 아닌 것은?**
a) Models
b) Templates
c) Views
d) Compilers

**4. 가상 환경을 사용하는 이유는?**
a) 컴퓨터의 메모리를 늘리기 위해
b) 특정 프로젝트마다 독립적인 파이썬 패키지를 관리하기 위해
c) 웹 브라우저 성능을 높이기 위해
d) 인터넷 속도를 빠르게 하기 위해

---

**5. 다음 중 Django 프로젝트 생성 명령어로 올바른 것은?**
a) django create project
b) python startproject djangoapp
c) django-admin startproject myproject
d) pip install project

---

**6. 소프트웨어 설계 시 반복적으로 나타나는 문제를 해결하기 위한 일반적인 방법을 무엇이라 하는가?**
a) 알고리즘
b) 변수
c) 디자인 패턴
d) 프레임워크

---

**7. Django에서 'App'의 역할로 적절한 것은?**
a) 전체 서버를 운영한다
b) 웹사이트 전체 구조를 담당한다
c) 하나의 기능 또는 모듈 단위를 구성한다
d) Python 인터프리터를 실행한다

---

**8. venv 모듈을 이용해 가상환경을 생성하는 명령어는?**
a) python install venv
b) python manage.py runserver
c) python -m venv myenv
d) pip install venv create

**9. 다음 중 Django의 주요 특징으로 올바르지 않은 것은?**
a) MTV 디자인 패턴을 기반으로 한다
b) 보안 기능이 내장되어 있다
c) 고정된 HTML 템플릿만 사용 가능하다
d) ORM(Object Relational Mapping)을 제공한다

---

**10. Django에서 render() 함수의 주된 목적은 무엇인가?**
a) URL을 등록한다
b) 정적 파일을 저장한다
c) 데이터를 템플릿에 전달하여 응답을 반환한다
d) 데이터베이스를 초기화한다

---

**11. 새로 만든 Django 앱을 프로젝트에 등록하기 위해 설정해야 하는 파일은?**
a) urls.py
b) settings.py
c) views.py
d) models.py

---

**12. MTV 패턴에서 사용자에게 보여지는 화면을 구성하는 요소는 무엇인가?**
a) Model
b) Template
c) View
d) URLconf


## 정답 및 해설

---

**1. 서버** 2. **b) 웹 개발에 필요한 코드를 줄이고 구조화를 돕는다** 3. **d) Compilers** 4. **b) 특정 프로젝트마다 독립적인 파이썬 패키지를 관리하기 위해** 5. **c) django-admin startproject myproject** 6. **c) 디자인 패턴** 7. **c) 하나의 기능 또는 모듈 단위를 구성한다** 8. **c) python -m venv myenv** 9. **c) 고정된 HTML 템플릿만 사용 가능하다** 10. **c) 데이터를 템플릿에 전달하여 응답을 반환한다** 11. **b) settings.py** 12. **b) Template**

---


**1. 서버는 클라이언트로부터 요청을 받고 처리한 결과를 클라이언트에게 전달하는 역할을 함.**
**2. 웹 프레임워크는 웹 애플리케이션 개발을 효율적으로 할 수 있도록 미리 정의된 구조와 기능을 제공함.**
**3. Django는 MTV(Model, Template, View) 패턴을 기반으로 하며, Compiler는 포함하지 않음.**
**4. 가상 환경은 프로젝트별로 필요한 파이썬 패키지를 격리하여 관리할 수 있도록 도와줌.**
**5. `python -m venv 환경이름` 명령어로 파이썬 가상환경을 생성할 수 있음.**
**6. Django 프로젝트는 `django-admin startproject 프로젝트이름` 명령어로 생성됨.**
**7. 디자인 패턴은 자주 마주치는 설계 문제를 해결하기 위한 표준화된 해결 방법임.**
**8. Django App은 특정 기능을 담당하는 코드 집합으로, 프로젝트 내에서 여러 개의 App을 운영할 수 있음.**
**9. Django는 다양한 템플릿 엔진을 사용할 수 있으며, HTML 템플릿에 고정되지 않음.**
**10. render() 함수는 요청, 템플릿 이름, context 데이터를 받아 템플릿을 렌더링한 HTTP 응답을 반환함.**
**11. settings.py의 INSTALLED_APPS 항목에 앱 이름을 추가하여 Django가 해당 앱을 인식하고 사용함.**
**12. Template은 사용자에게 보여질 웹페이지 화면을 정의하며 HTML로 작성됨.**



----------------------------------------


















## Templates & URLs

**1. Django에서 템플릿 시스템을 사용하는 주요 목적은?**

a) 데이터베이스를 관리하기 위해  
b) HTML과 Python 코드를 분리하여 작성하기 위해  
c) 사용자 인증을 처리하기 위해  
d) 프로젝트 디렉터리를 만들기 위해

**2. Django Template Language(DTL)에서 변수 출력 시 사용하는 문법은?**

a) `{{ 변수명 }}`  
b) `{% 변수명 %}`  
c) `(( 변수명 ))`  
d) `[ 변수명 ]`

**3. 템플릿 상속 시, 하위 템플릿이 상속하는 상위 템플릿을 지정할 때 사용하는 태그는?**

a) `{% include %}`  
b) `{% import %}`  
c) `{% extends %}`  
d) `{% template %}`

**4. HTML form을 통해 데이터를 전송할 때 사용하는 HTTP 메서드가 아닌 것은?**

a) GET  
b) POST  
c) DELETE  
d) FETCH

**5. form 태그에 action 속성이 없을 경우 기본으로 동작하는 경로는?**

a) 루트 경로(/)  
b) 이전 페이지  
c) 현재 페이지  
d) form이 있는 템플릿의 상위 템플릿

**6. 다음 중 URL 패턴에서 변수로 값을 전달하는 방법으로 올바른 것은?**

a) `path('user/<int:id>/', views.user_detail)`  
b) `path('user/{id}/', views.user_detail)`  
c) `url('user/<int:id>/', views.user_detail)`  
d) `get('user/:id/', views.user_detail)`

**7. Django에서 앱 별로 URL 구성을 따로 할 수 있도록 해주는 설정은?**

a) urls.py에서 include() 사용  
b) views.py에서 import  
c) models.py 연결  
d) settings.py에 form 작성

**8. Django에서 URL에 이름을 지정해 사용하는 이유는?**

a) URL을 암호화하기 위해  
b) URL을 외부로 노출하지 않기 위해  
c) 템플릿에서 링크를 쉽게 연결하기 위해  
d) URL을 길게 보이게 하기 위해

**9. Django 템플릿에서 URL 태그를 사용할 때 올바른 문법은?**

a) `{{ url 'home' }}`  
b) `[[ url 'home' ]]`  
c) `{% url 'home' %}`  
d) `<% url 'home' %>`

**10. app_name 속성을 사용하는 주요 목적은?**

a) URL 경로를 암호화하기 위해  
b) 앱 이름으로 템플릿을 렌더링하기 위해  
c) URL 이름이 중복되지 않도록 네임스페이스를 지정하기 위해  
d) settings.py에 앱을 등록하기 위해

**11. Django에서 템플릿 파일의 경로를 설정할 때 사용하는 설정 변수는?**

a) STATICFILES_DIRS  
b) MEDIA_ROOT  
c) TEMPLATES  
d) TEMPLATE_PATH

**12. Django Template Language 사용 시, 다음 중 올바르지 않은 변수 출력 방식은?**

a) `{{ title }}`  
b) `{% title %}`  
c) `{{ user.name }}`  
d) `{{ 1|add:2 }}`

## 정답 및 해설

**1.** b) HTML과 Python 코드를 분리하여 작성하기 위해 **2.** a) `{{ 변수명 }}` **3.** c) `{% extends %}` **4.** d) FETCH  
**5.** c) 현재 페이지 **6.** a) `path('user/<int:id>/', views.user_detail)` **7.** a) urls.py에서 include() 사용  
**8.** c) 템플릿에서 링크를 쉽게 연결하기 위해

**해설:**

**1.** Django 템플릿 시스템은 HTML과 Python 코드를 분리하여 보다 구조적인 웹 페이지를 작성할 수 있도록 함

**2.** 변수를 출력할 때는 `{{ 변수명 }}` 형태로 사용하며, 태그 `{% %}`와는 구분됨

**3.** 템플릿 상속 구조를 만들기 위해 `{% extends 'base.html' %}` 형태로 상위 템플릿을 지정함

**4.** HTML form에서는 기본적으로 GET과 POST 메서드를 사용하며, DELETE와 FETCH는 사용하지 않음

**5.** action 속성이 없으면 현재 페이지로 데이터를 전송함

**6.** Django에서는 path() 함수를 사용하며, 변수는 `<자료형:이름>` 형태로 지정함

**7.** 앱별 urls.py를 메인 urls.py에 include()로 포함시켜 앱 URL 관리를 가능하게 함

**8.** URL에 이름을 지정해두면 템플릿에서 `{% url '이름' %}` 문법으로 사용 가능하여 유지보수가 편리함

## 정답 및 해설

**9.** c) `{% url 'home' %}` **10.** c) URL 이름이 중복되지 않도록 네임스페이스를 지정하기 위해  
**11.** c) TEMPLATES **12.** b) `{% title %}`

**해설:**

**9.** URL 태그는 `{% url '이름' %}` 문법으로 사용하여 URL을 역으로 생성할 수 있음

**10.** 여러 앱에서 동일한 URL 이름을 사용할 수 있으므로, app_name을 통해 네임스페이스를 설정해 충돌을 방지함

**11.** 템플릿 경로는 settings.py의 TEMPLATES 설정 안의 'DIRS' 항목에 추가함

**12.** `{% %}`는 태그에 사용되고, 변수 출력에는 `{{ }}`를 사용해야 하므로 `{% title %}`는 잘못된 문법


------------------------------
















## Model

**1. Django에서 모델 클래스는 어떤 클래스의 서브클래스로 정의되어야 하는가?**

a) HttpResponse  
b) ModelForm  
c) models.Model  
d) admin.ModelAdmin

**2. 사용자의 이름을 저장하기에 가장 적절한 필드 타입은 무엇인가?**

a) IntegerField  
b) CharField  
c) BooleanField  
d) DateTimeField

**3. 필드를 필수 입력 항목으로 설정하려면 어떤 옵션을 사용해야 하는가?**

a) max_length  
b) default  
c) null=True  
d) blank=False

**4. 모델 필드에 기본값을 지정하는 옵션은 무엇인가?**

a) default  
b) unique  
c) choices  
d) max_length


**5. 날짜와 시간을 모두 저장해야 할 경우 적절한 필드 타입은 무엇인가?**

a) DateField  
b) TimeField  
c) DateTimeField  
d) DurationField

**6. 모델 변경 사항을 반영하여 migration 파일을 생성하는 명령어는 무엇인가?**

a) python manage.py runserver  
b) python manage.py makemigrations  
c) python manage.py migrate  
d) python manage.py startapp

**7. migration 파일을 실제 데이터베이스에 적용하려면 어떤 명령어를 사용해야 하는가?**

a) makemigrations  
b) startproject  
c) migrate  
d) collectstatic

**8. 다음 중 CharField를 정의할 때 입력 값 길이 제한을 위해 부여할 수 있는 옵션은 무엇인가?**

a) null  
b) max_length  
c) unique  
d) default

**9. Django의 기본 데이터베이스 엔진으로 설정된 것은?**

a) MySQL  
b) PostgreSQL  
c) Oracle  
d) SQLite

**10. Django 모델 클래스 안에서 정의된 각 필드는 어떤 의미를 가지는가?**

a) HTML 입력 필드  
b) 뷰 함수  
c) 데이터베이스 컬럼  
d) URL 라우팅

**11. Admin 사이트에 모델을 등록하려면 어떤 함수를 사용해야 하는가?**

a) include()  
b) register()  
c) admin.site.register()  
d) path()

**12. Django에서 객체가 생성된 시점을 자동으로 기록하려면 DateTimeField에 어떤 옵션을 설정해야 하는가?**

a) auto_add=True  
b) auto_now=True  
c) auto_created=True  
d) auto_now_add=True


## 정답 및 해설

**1. c) models.Model  2. b) CharField  3. d) blank=False  4. a) default  5. c) DateTimeField  6. b) python manage.py makemigrations  7. c) migrate  8. b) max_length  9. d) SQLite  10. c) 데이터베이스 컬럼  11. c) admin.site.register()  12. d) auto_now_add=True**

1. Django의 모델은 models.Model 클래스를 상속받아 정의되어야 함

2. CharField는 문자열 데이터를 저장하는 데 사용되며, 이름과 같은 짧은 텍스트에 적합

3. blank=False는 해당 필드가 빈 값을 허용하지 않음을 의미하여 폼에서 필수로 입력하도록 만듦

4. default 옵션은 객체를 생성할 때 필드에 지정된 기본값을 자동으로 설정

5. DateTimeField는 날짜와 시간을 모두 저장할 수 있는 필드 타입

6. makemigrations 명령어는 모델의 변경 사항을 기반으로 새로운 migration 파일을 생성

7. migrate 명령은 migration 파일을 바탕으로 데이터베이스를 실제로 변경

8. CharField는 문자열 길이를 제한하기 위해 max_length 옵션을 지정할 수 있음

9. Django는 기본 설정에서 SQLite를 데이터베이스 엔진으로 사용

10. 모델 클래스의 각 필드는 실제 데이터베이스 테이블의 컬럼에 해당

11. admin.site.register() 함수를 사용하여 모델을 Admin 사이트에 등록할 수 있음

12. auto_now_add=True는 객체가 처음 생성될 때만 시각을 자동으로 기록해줌

------------------------











## ORM


1. Django에서 ORM(Object Relational Mapping)의 주된 목적은 무엇인가?

a) HTML 렌더링을 단순화하기 위해  
b) SQL 쿼리를 직접 작성하지 않고 데이터베이스를 조작하기 위해  
c) 서버의 속도를 향상시키기 위해  
d) CSS 파일을 자동으로 생성하기 위해

2. 다음 중 Django ORM으로 새로운 게시글 객체를 생성하는 코드로 올바른 것은?

a) Post.new(title="New Post")  
b) Post.make(title="New Post")  
c) Post.objects.create(title="New Post")  
d) Post.objects.add(title="New Post")

3. 모든 게시글을 조회하기 위한 Django ORM 코드는?

a) Post.all()  
b) Post.objects()  
c) Post.objects.get()  
d) Post.objects.all()

4. 게시글 ID가 1인 객체의 제목을 수정하는 올바른 코드 조합은?

a) Post.objects.set(id=1, title="수정됨")  
b) Post.objects.get(id=1).update(title="수정됨")  
c) Post.update(id=1, title="수정됨")  
d) post = Post.objects.get(id=1)  
   post.title="수정됨"  
   post.save()

5. 게시글 하나를 삭제하는 가장 알맞은 방법은?

a) Post.objects.delete(id=1)  
b) Post.objects.get(id=1).delete()  
c) Post.remove(id=1)  
d) delete Post where id=1

6. 제목이 정확히 "Welcome"인 게시글만 조회하고 싶을 때 알맞은 쿼리는?

a) Post.objects.filter(title="Welcome")  
b) Post.objects.filter(title__contains="Welcome")  
c) Post.objects.get(title__startswith="Welcome")  
d) Post.objects.exclude(title="Welcome")

7. 제목에 "Django"라는 단어가 포함된 게시글을 조회하는 코드는?

a) Post.objects.filter(title__has="Django")  
b) Post.objects.filter(title_contains="Django")  
c) Post.objects.filter(title__contains="Django")  
d) Post.objects.get(title__contains="Django")

8. Django ORM을 사용하는 주요 장점 중 틀린 것은?

a) 코드의 가독성이 높아진다  
b) SQL Injection의 위험을 줄인다  
c) 모든 쿼리를 수동으로 작성해야 한다  
d) 다양한 데이터베이스에 대해 추상화된 접근이 가능하다

9. 작성자가 'anonymous'인 게시글을 모두 삭제하는 가장 적절한 방법은?

a) Post.delete(author="anonymous")  
b) Post.objects.filter(author="anonymous").delete()  
c) Post.remove(author="anonymous")  
d) Post.objects.get(author="anonymous").delete_all()

10. 다음 중 게시글 제목을 일괄 변경할 때 사용할 수 있는 QuerySet API는?

a) update()  
b) set()  
c) save_all()  
d) apply()

11. 전체 게시글을 삭제하려면 어떤 코드를 사용할까?

a) Post.delete()  
b) Post.remove_all()  
c) Post.objects.all().delete()  
d) Post.objects.clear()

12. 다음 중 Post.objects.all()과 Post.objects.get(id=1)의 리턴값에 대한 설명으로 옳은 것은?

a) 둘 다 단일 객체를 반환한다  
b) 둘 다 QuerySet을 반환한다  
c) all()은 QuerySet을 반환하고, get()은 단일 객체를 반환한다  
d) get()은 리스트를 반환하고, all()은 None을 반환한다

----


**정답 및 해설**

1. b) SQL 쿼리를 직접 작성하지 않고 데이터베이스를 조작하기 위해 2. c) Post.objects.create(title="New Post") 3. d) Post.objects.all() 4. d) post = Post.objects.get(id=1) post.title="수정됨" post.save() 5. b) Post.objects.get(id=1).delete() 6. a) Post.objects.filter(title="Welcome") 7. c) Post.objects.filter(title__contains="Django") 8. c) 모든 쿼리를 수동으로 작성해야 한다 9. b) Post.objects.filter(author="anonymous").delete() 10. a) update() 11. c) Post.objects.all().delete() 12. c) all()은 QuerySet을 반환하고, get()은 단일 객체를 반환한다

1. Django ORM은 파이썬 코드만으로 데이터베이스를 다룰 수 있게 해주며, SQL을 별도로 복잡한 데이터 조작이 가능하게 함

2. Post.objects.create()는 새 레코드를 생성하고 저장하는 데 사용됨

3. Post.objects.all()은 해당 모델의 모든 게시글을 반환함

4. 객체를 조회하고 필드를 수정한 후 .save()로 반영하는 것이 일반적인 방법

5. 객체를 get()으로 조회한 다음 .delete() 메서드를 호출해 삭제할 수 있음

6. 조건 없이 문자열과 정확히 일치할 때는 필드명만 써도 되며, title="Welcome"은 title이 정확히 "Welcome"인 값을 찾음

7. field__contains는 해당 필드에 특정 문자열이 포함된 객체를 조회할 수 있음

8. ORM을 사용하면 이전 중 하나는 쿼리를 자동으로 생성해주는 기능으로, 직접 작성할 필요가 줄어듦

9. .filter()로 조건에 맞는 객체들을 선택하고, .delete()를 호출하면 해당 객체들이 모두 삭제됨

10. update() 메서드는 필터링된 QuerySet에 대해 필드 값을 일괄적으로 수정할 때 사용함

11. Post.objects.all()은 전체 게시글을 선택하고, .delete()는 이를 삭제함

12. all()은 여러 객체가 담긴 QuerySet을 반환하고, get()은 조건에 일치하는 하나의 객체만 반환함. get() 결과는 QuerySet이 아닌 모델 인스턴스

--------------------------------------------------------

















## ORM with View


**1. GET 메서드의 특징으로 옳은 것은?**

a) 요청 본문(Body)에 데이터를 숨겨 전송
b) 서버 상태를 변경하는 작업에 주로 사용
c) 응답 결과를 브라우저가 캐시 가능
d) 브라우저 기록(History)에 남지 않음

---

**2. POST 메서드를 사용해야 하는 가장 적절한 상황은?**

a) 데이터 조회
b) 새 게시글 작성
c) 정적 파일 다운로드
d) 단순 페이지 이동

---

**3. HTTP 상태 코드 403 Forbidden이 의미하는 것은?**

a) 요청이 성공적으로 처리됨
b) 리소스를 찾을 수 없음
c) 권한 문제로 요청이 거절됨
d) 서버 오류가 발생

---

**4. Django에서 CSRF 토큰을 사용하는 주된 목적은?**

a) 데이터 압축
b) 사이트 간 요청 위조 방지
c) 정적 자원 캐싱
d) URL 라우팅 단축

**5. redirect() 함수가 render()와 다른 점으로 옳은 것은?**

a) 템플릿을 직접 렌더링
b) 클라이언트에게 다른 URL로 다시 요청하라는 응답을 줌
c) 데이터베이스 세션을 초기화
d) HTTP 404 오류를 발생

---

**6. Article.objects.create() 메서드의 특징으로 옳은 것은?**

a) 인스턴스를 생성하지만 저장하지 않음
b) 객체를 만들고 즉시 DB에 저장
c) 특정 조건에 맞는 객체를 조회
d) 기존 객체를 삭제

---

**7. URL에 데이터가 노출되는 전송 방식은?**

a) GET
b) POST
c) 둘 다
d) 둘 다 아님

---

**8. 캐시(Cache) 활용 시 기대할 수 있는 이점이 아닌 것은?**

a) 페이지 응답 속도 향상
b) 서버 부하 감소
c) 데이터 무결성 자동 보장
d) 반복 조회 시 네트워크 비용 절감


**9. URL 패턴 `<int:pk>/` 의 주된 용도는?**

a) 새 글 작성 페이지로 이동
b) 글 번호를 받아 해당 글 상세 페이지로 라우팅
c) 정적 파일 제공
d) 전체 글 목록 출력

---

**10. 모든 Article 레코드를 조회하여 QuerySet을 반환하는 메서드는?**

a) get()
b) filter()
c) all()
d) delete()

---

**11. HTTP 404 Not Found 응답을 반환해야 하는 가장 적절한 상황은?**

a) 사용자가 인증되지 않음
b) 서버 내부 로직 오류로 처리에 실패
c) 클라이언트가 요청한 URL에 해당하는 리소스가 존재하지 않음
d) 클라이언트의 요청 본문 형식이 잘못됨

---

**12. objects.get() 메서드에 대한 설명으로 옳은 것은?**

a) 조건에 맞는 모든 레코드를 QuerySet으로 반환
b) 조건과 일치하는 단 하나의 객체를 반환하며, 없으면 DoesNotExist 예외를 발생
c) 항상 새로운 객체를 생성하고 저장
d) 조건이 여러 개여도 예외 없이 첫 번째 객체만 반환








## 정답 및 해설

---

### 정답

1.  c) 응답 결과를 브라우저가 **캐시 가능**
2.  b) 새 게시글 작성
3.  c) 권한 문제로 요청이 거절됨
4.  b) 사이트 간 요청 위조 방지
5.  b) 클라이언트에게 다른 URL로 다시 요청하라는 응답을 줌
6.  b) 객체를 만들고 즉시 DB에 저장
7.  a) GET
8.  c) 데이터 무결성 자동 보장
9.  b) 글 번호를 받아 해당 글 상세 페이지로 라우팅
10. c) all()
11. c) 클라이언트가 요청한 URL에 해당하는 리소스가 존재하지 않음
12. b) 조건과 일치하는 단 하나의 객체를 반환하며, 없으면 DoesNotExist 예외를 발생

---

### 해설

1.  **GET**은 주로 조회에 사용되며, 동일 URL에 재요청 시 **브라우저 캐시**를 활용할 수 있음
2.  **POST**는 서버의 리소스를 생성·수정·삭제하는 요청에 사용되며, **게시글 작성**이 대표적
3.  **403**은 서버가 요청을 이해했으나 **권한 부족** 등으로 거부했음을 나타냄
4.  **CSRF 토큰**은 사용자가 의도하지 않은 악의적 **POST 요청을 차단**하는 보안 장치
5.  **Redirect()**는 3xx 응답을 보내어 브라우저가 지정된 URL로 GET 요청을 다시 보내도록 유도
6.  **create()**는 객체를 만들면서 **save()**까지 한 번에 수행
7.  **GET**은 **쿼리 문자열**로 데이터를 전달하므로 **URL에 보임**. POST는 HTTP Body에 담김
8.  **캐시**는 성능과 비용 측면에서 유리하지만 데이터 변경 시 **일관성 관리가 필요**
9.  `<int:pk>`는 **정수형 기본 키 값**을 캡처하여 **detail view**처럼 특정 객체 상세 조회에 사용
10. **all()**은 조건 없이 테이블의 모든 레코드를 담은 **QuerySet**을 돌려줌
11. **404**는 요청한 경로는 유효하지만, 그 경로에 매핑되는 데이터나 뷰가 존재하지 않을 때 사용
12. **get()**은 단일 객체 조회 전용이며, 결과가 없거나 2개 이상이면 **예외를 발생**시킴


-------------------------------------



















## Django Form


문제 1
다음 중 **Django Form**이 하는 일로 옳지 않은 것은?
a) 데이터 입력 화면 생성
b) 데이터 유효성 검사
c) 데이터 자동 저장 처리
d) 데이터베이스에 접속하여 직접 테이블 삭제

---

문제 2
**ModelForm**과 일반 **Form**의 차이에 대해 옳은 것은?
a) **ModelForm**은 **DB**와 연결되지 않는다.
b) 일반 **Form**은 **DB**에 데이터를 저장할 때 사용한다.
c) **ModelForm**은 데이터베이스와 직접 연결되어 있다.
d) 일반 **Form**은 자동 유효성 검사를 지원하지 않는다.

---

문제 3
다음 중 **Django Form**의 유효성 검사를 수행하는 메서드는?
a) `save()`
b) `is_valid()`
c) `redirect()`
d) `render()`

---

문제 4
**Form**의 입력 필드를 화면에 렌더링할 때 사용하는 옵션 중, 각 필드를 **`<p>`** 태그로 감싸주는 옵션은?
a) `{{ form.as_ul }}`
b) `{{ form.as_table }}`
c) `{{ form.as_p }}`
d) `{{ form.as_render }}`


문제 5
**Django**에서 사용자 입력 데이터를 저장하거나 수정할 때 사용하는 메서드는?
a) `update()`
b) `create()`
c) `save()`
d) `delete()`

---

문제 6
**Django Form** 클래스의 기본 구조에서 **HTML**의 입력 요소를 조정할 때 사용하는 것은?
a) **model**
b) **widget**
c) **validator**
d) **queryset**

---

문제 7
**Django**의 **ModelForm**에서 사용할 필드를 선택적으로 제외할 때 사용하는 **Meta** 클래스 속성은?
a) **fields**
b) **exclude**
c) **remove**
d) **drop**

---

문제 8
다음 중 **Django Form**에서 입력값이 유효하지 않을 때 발생하는 동작으로 가장 알맞은 것은?
a) 서버가 **500** 에러를 반환한다.
b) **Form** 객체가 생성되지 않는다.
c) `is_valid()`는 **False**를 반환하고 오류 메시지가 **form** 객체에 저장된다
d) 잘못된 값을 그대로 저장된다.


문제 9
**Form** 클래스에서 입력 필드에 **placeholder**나 **class** 등 추가 속성을 설정할 수 있는 곳은?
a) **fields**
b) **model**
c) **attrs**
d) **exclude**

---

문제 10
다음 중 **Django view** 함수가 **HTTP**의 **POST** 요청을 처리하는 경우로 올바른 것은?
a) 화면에 폼을 출력하여 사용자에게 보여준다.
b) 사용자가 입력한 데이터를 받아서 유효성 검사를 수행한다.
c) 데이터베이스에 있는 데이터를 화면에 표시한다.
d) **URL** 주소를 통해 직접 화면에 접근할 때 사용된다.










----------

### 정답 및 해설

1.  d) 데이터베이스에 접속하여 직접 테이블 삭제
2.  c) **ModelForm**은 데이터베이스와 직접 연결되어 있다.
3.  b) `is_valid()`
4.  c) `{{ form.as_p }}`
5.  c) `save()`
6.  b) **widget**
7.  b) **exclude**
8.  c) `is_valid()`는 **False**를 반환하고 오류 메시지가 **form** 객체에 저장된다.
9.  c) **attrs**
10. b) 사용자가 입력한 데이터를 받아서 유효성 검사를 수행한다.

----------

### 해설

1.  **Django Form**은 사용자로부터 입력받은 데이터의 화면 표시, 유효성 검사, 데이터 처리를 담당하지만, **데이터베이스의 테이블을 직접 삭제하는 기능은 제공하지 않**습니다. 테이블 삭제와 같은 작업은 **데이터베이스 관리자**의 권한으로 **Django**의 **Form 클래스**와는 관련이 없습니다.

2.  **ModelForm**은 **Django**의 **모델(Model)**과 직접 연결되어 있어 데이터베이스에 저장하거나 수정할 때 편리하게 사용 가능합니다. 일반 **Form**은 **DB**에 연결되지 않고 입력값 수집 및 유효성 검사만 처리합니다.

3.  **Django Form**의 `is_valid()` 메서드는 사용자 입력 데이터가 유효한 형식인지 검사하는 기능을 제공합니다. `save()` 메서드는 유효성 검사를 통과한 후 데이터를 저장할 때 사용되는 메서드입니다.

4.  **Django**의 **Form 클래스**에서 `{{ form.as_p }}`를 사용하면 각 입력 필드를 자동으로 **`<p>` 태그**로 감싸서 화면에 출력합니다. 이 외에 **as_ul**, **as_table** 같은 다른 옵션도 존재하지만, **`<p>` 태그**를 사용하는 것은 **as_p**입니다.

5.  **Django**의 **ModelForm**은 `save()` 메서드를 사용하여 데이터를 데이터베이스에 저장하거나 기존 데이터를 수정합니다. `create()`, `update()`, `delete()`는 **Django 모델**의 메서드로 사용될 수 있지만 **Form**에서 데이터를 처리할 때는 사용하지 않습니다.

6.  **Form 클래스**에서 **HTML** 입력 요소의 스타일이나 추가 속성 (**placeholder**, **class** 등)을 지정할 때 **Widget**을 사용합니다. **Widget**을 통해 입력 필드가 **HTML**에서 어떻게 렌더링될지 세부적으로 조정 가능합니다.

7.  **Django ModelForm**에서 **Meta 클래스**의 **exclude** 속성은 폼에서 제외하고 싶은 필드를 지정하는 데 사용됩니다. 반면 **fields** 속성은 포함할 필드를 명시적으로 정의할 때 사용합니다.

8.  **Django Form**에서 `is_valid()`는 입력값이 유효하지 않으면 **False**를 반환합니다. 이때 발생한 오류 내용은 **form** 객체의 **errors** 속성에 저장되어 사용자에게 출력될 수 있습니다. 이 과정은 자동으로 수행되며 서버 에러가 발생하지 않고, 잘못된 값도 저장되지 않습니다.

9.  입력 필드에 추가 속성 (**placeholder**, **class** 등)을 지정하려면 **Form 클래스**의 **Widget** 내부의 **attrs** 속성을 사용합니다. 이를 통해 화면에 표시되는 **HTML** 요소를 세부적으로 제어할 수 있습니다.

10. **HTTP POST** 요청은 사용자가 입력한 데이터를 서버로 전송하여 처리할 때 사용됩니다. **Django**에서 **POST** 요청은 사용자가 제출한 폼 데이터를 받아 유효성 검사를 거쳐 데이터베이스에 저장하거나 처리하는 데 활용됩니다.




## Authentication System1

**1. HTTP의 특징이 아닌 것을 고르시오.**
a) 상태 유지 (Stateful)
b) 무상태 (Stateless)
c) 웹 데이터 교환의 기초
d) 비연결 지향 (Connectionless)

---

**2. 서버가 브라우저에 보내는 작은 데이터 조각은?**
a) 캐시 (Cache)
b) 쿠키 (Cookie)
c) 세션 (Session)
d) 프로토콜 (Protocol)

---

**3. 쿠키의 주된 사용 목적이 아닌 것은?**
a) 세션 관리
b) 사용자 개인화
c) 사용자 행동 추적
d) 데이터베이스 역할

---

**4. 서버 측에서 사용자 상태를 저장하는 기술은?**
a) 캐시 (Cache)
b) 쿠키 (Cookie)
c) 세션 (Session)
d) 로컬 스토리지

**5. 세션 ID는 어디에 저장되어 전달되는가?**
a) URL 파라미터
b) 서버 데이터베이스
c) 쿠키
d) 자바스크립트 변수

---

**6. Django의 기본 User 모델에 없는 필드는?**
a) password
b) phone\_number
c) username
d) email

---

**7. 커스텀 User 모델 설정은 언제 해야 하는가?**
a) 프로젝트 중간
b) 기능 개발 완료 후
c) 데이터베이스 마이그레이션 후
d) 프로젝트 시작 시

---

**8. Django에서 사용자 인증에 사용되는 폼은?**
a) CustomForm
b) AuthenticationForm
c) ModelForm
d) UserCreationForm


**9. 로그인 성공 후 세션을 생성하는 함수는?**
a) start\_session()
b) authenticate()
c) login()
d) session\_create()

---

**10. 커스텀 User 모델을 지정하는 설정 항목은?**
a) USER\_MODEL\_AUTH
b) DJANGO\_USER\_MODEL
c) CUSTOM\_USER\_MODEL
d) AUTH\_USER\_MODEL

---

**11. HTTP의 '무상태(stateless)'란?**
a) 이전 요청 정보를 유지하지 않음
b) 서버가 클라이언트 정보를 기억함
c) 연결을 계속 유지함
d) 모든 요청은 다르게 처리됨

---

**12. 쿠키와 세션의 공통적인 목적은?**
a) 서버 부하 감소
b) 데이터 영구 저장
c) 빠른 데이터 전송
d) 상태 정보 유지 및 사용자 식별



### 정답 및 해설

---

**1. a) 상태 유지 (Stateful)** 2. **b) 쿠키 (Cookie)** 3. **d) 데이터베이스 역할** 4. **c) 세션 (Session)** 5. **c) 쿠키** 6. **b) phone\_number** 7. **d) 프로젝트 시작 시** 8. **b) AuthenticationForm** 9. **c) login()** 10. **d) AUTH\_USER\_MODEL** 11. **a) 이전 요청 정보를 유지하지 않음** 12. **d) 상태 정보 유지 및 사용자 식별**

---

1.  **HTTP**는 상태를 유지하지 않는 **무상태(Stateless)** 프로토콜입니다.
2.  **쿠키**는 서버가 사용자의 웹 브라우저에 전송하는 작은 **데이터 조각**입니다.
3.  쿠키는 간단한 데이터를 저장하며, **데이터베이스를 대체할 수 없습니다**.
4.  **세션**은 **서버 측**에서 클라이언트와의 상태를 유지하고 정보를 저장합니다.
5.  서버가 발급한 **세션 ID**는 **쿠키**에 저장되어 클라이언트와 서버 간에 전달됩니다.
6.  **전화번호**와 같은 추가 정보는 기본 User 모델에 없어 커스텀이 필요합니다.
7.  Django는 **프로젝트 시작 시** 커스텀 User 모델 설정을 강력히 권장합니다.
8.  **AuthenticationForm**은 사용자 로그인(인증)을 위해 사용되는 내장 폼입니다.
9.  `auth` 모듈의 **`login()`** 함수가 인증된 사용자의 **세션을 생성**하고 로그인 처리합니다.
10. **`settings.py`** 파일에서 **`AUTH_USER_MODEL`**에 커스텀 모델 경로를 지정합니다.
11. 연결이 끊어지면 통신이 끝나, **이전 요청의 상태 정보가 유지되지 않음**을 의미합니다.
12. 두 기술 모두 **상태가 없는 HTTP**에서 **상태를 유지하고 사용자를 구분**하기 위해 사용됩니다.

--------










## Authentication System2

### 1. 로그아웃의 역할로 가장 옳은 것은?
a) 세션 데이터만 삭제
b) 클라이언트 쿠키만 삭제
c) 세션 데이터와 쿠키 모두 처리
d) 사용자 계정 정보 삭제

---

### 2. 회원가입 기능에 사용하는 Django 내장 폼은?
a) AuthenticationForm
b) UserCreationForm
c) UserChangeForm
d) CustomUserForm

---

### 3. `get_user_model()` 함수를 사용하는 가장 큰 이유는?
a) 사용자 객체를 삭제하기 위해
b) 비밀번호를 암호화하기 위해
c) 활성화된 User 모델을 참조하기 위해
d) 모든 사용자 정보를 조회하기 위해

---

### 4. 로그인된 사용자의 회원 탈퇴를 구현하는 코드는?
a) `request.user.delete()`
b) `User.objects.delete(request.user)`
c) `delete(request.user)`
d) `request.user.remove()`


---

### 5. 템플릿에서 사용자의 로그인 여부를 확인하는 속성은?
a) `is_active`
b) `is_staff`
c) `is_loggedin`
d) `is_authenticated`

---

### 6. `@login_required` 데코레이터의 역할은 무엇인가요?
a) 로그인 페이지를 렌더링
b) 비인증 사용자의 접근을 제한
c) 모든 사용자의 접근을 허용
d) 관리자만 접근을 허용

---

### 7. 회원가입 직후 자동 로그인을 시키는 방법은?
a) `form.save()` 후 `login()` 호출
b) `login()` 호출 후 `form.save()`
c) `form.save()`만 호출
d) `login()`만 호출

---

### 8. 회원 탈퇴 시 올바른 처리 순서는?
a) 로그아웃 후 계정 삭제
b) 계정 삭제 후 로그아웃
c) 순서는 상관 없음
d) 동시에 처리해야 함


## 예상 문제
### 9. AbstractUser와 AbstractBaseUser의 주요 차이점은?
a) AbstractUser가 더 자유도가 높다
b) AbstractBaseUser는 필드가 더 많다
c) AbstractUser는 기본 필드를 포함한다
d) 둘은 기능적으로 완전히 동일하다

---

### 10. 로그아웃 요청은 어떤 방식으로 보내야 안전한가요?
a) GET
b) POST
c) PUT
d) DELETE

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>









## 정답 및 해설

### 정답 요약
1.  **c) 세션 데이터와 쿠키 모두 처리**
2.  **b) UserCreationForm**
3.  **c) 활성화된 User 모델을 참조하기 위해**
4.  **a) `request.user.delete()`**
5.  **d) `is_authenticated`**
6.  **b) 비인증 사용자의 접근을 제한**
7.  **a) `form.save()` 후 `login()` 호출**
8.  **b) 계정 삭제 후 로그아웃**
9.  **c) AbstractUser는 기본 필드를 포함한다**
10. **b) POST**

---

### 상세 해설

1.  로그아웃은 서버의 **세션 데이터**를 삭제하고, 클라이언트의 쿠키에 저장된 **세션 ID** 삭제로 연결을 완전히 끊는 과정입니다.
2.  **`UserCreationForm`**은 새로운 사용자 생성(회원가입)하기 위해 Django에서 기본으로 제공하는 **ModelForm**입니다.
3.  프로젝트의 **User 모델**이 기본이든 커스텀이든, 현재 **활성화된 모델**을 동적으로 가져와 코드의 유연성을 높입니다.
4.  `request` 객체에 담겨있는 현재 로그인된 사용자(`user`) 객체의 **`delete()`** 메서드를 호출하여 간단하게 탈퇴시킬 수 있습니다.
5.  **`is_authenticated` 속성**은 사용자가 인증(로그인)되었는지 여부를 **True/False**로 반환하는 가장 확실한 방법입니다.
6.  인증되지 않은 사용자가 해당 **view**에 접근하면, 지정된 **로그인 페이지로 리디렉션**시켜 접근을 막습니다.
7.  `form.save()`가 반환하는 **User 객체**를 **`login()` 함수**에 인자로 넘겨주면 세션이 생성되어 **자동 로그인**됩니다.
8.  **계정**을 먼저 삭제한 뒤, 남아있는 세션 정보를 **로그아웃**으로 정리해야 합니다. 반대로 하면 어떤 계정을 지워야 할지 알 수 없게 됩니다.
9.  **`AbstractUser`**는 **기본 User 모델의 모든 필드**를 포함하여 확장이 용이하고, **`AbstractBaseUser`**는 **최소한의 필드**만 제공하여 자유도가 높습니다.
10. **GET 요청**은 데이터 변경을 유발해서는 안 되므로, **서버 상태를 변경**하는 로그아웃은 **POST 방식**으로 처리해야 안전합니다.




## Aythentication System3

### 1. 회원 정보 수정 시 사용하는 Django 내장 폼은?
a) `UserCreationForm`
b) `AuthenticationForm`
c) `UserChangeForm`
d) `PasswordChangeForm`

---

### 2. `UserChangeForm`을 커스텀할 때, 불필요한 필드를 제외하는 방법은?
a) `exclude` 옵션 사용
b) `fields` 옵션에 원하는 필드만 명시
c) `Meta` 클래스를 삭제
d) 폼 템플릿에서 직접 HTML 태그 삭제

---

### 3. 비밀번호 변경 시 사용하는 Django 내장 폼은?
a) `UserChangeForm`
b) `PasswordChangeForm`
c) `SetPasswordForm`
d) `AuthenticationForm`

---

### 4. 비밀번호 변경 후 로그아웃되는 현상을 막는 함수는?
a) `login(request, user)`
b) `logout(request)`
c) `update_session_auth_hash(request, user)`
d) `save_session(request)`

---

### 5. 비밀번호를 복원이 불가능한 고정 길이의 문자열로 바꾸는 과정은?
a) 인코딩 (Encoding)
b) 디코딩 (Decoding)
c) 해싱 (Hashing)
d) 암호화 (Encryption)

---

### 6. 해시 함수의 특징이 아닌 것은?
a) 입력값이 같으면 항상 같은 결과가 나온다.
b) 해시값으로 원래 입력값을 쉽게 알 수 있다.
c) 입력값이 조금만 달라도 결과는 크게 달라진다.
d) 어떤 길이의 입력이든 고정된 길이로 출력된다.

---

### 7. '레인보우 테이블' 공격을 방어하기 위한 기법은?
a) 키 스트레칭 (Key Stretching)
b) 솔트 (Salt) 사용
c) 2단계 인증 (2FA)
d) HTTPS 사용

---

### 8. '무차별 대입 공격'의 효율을 떨어뜨리기 위한 기법은?
a) 솔트 (Salt) 사용
b) 키 스트레칭 (Key Stretching)
c) 비밀번호 복잡도 규칙 적용
d) 캡챠 (CAPTCHA) 사용

---


### 9. Django가 기본으로 사용하는 비밀번호 해싱 알고리즘은?
a) MD5
b) SHA-1
c) PBKDF2
d) bcrypt

---

### 10. Django 비밀번호 해시값에 포함되지 않는 정보는?
a) 알고리즘 (algorithm)
b) 반복 횟수 (iterations)
c) 솔트 (salt)
d) 사용자 아이디 (username)

---

### 11. 비밀번호 초기화 기능을 위해 `settings.py`에 설정해야 하는 것은?
a) `PASSWORD_RESET_TIMEOUT_DAYS`
b) `EMAIL_BACKEND`
c) `AUTH_PASSWORD_VALIDATORS`
d) `LOGIN_REDIRECT_URL`

---------










<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


----------

## 정답 및 해설


### 정답 요약
1.  c) UserChangeForm
2.  b) fields 옵션에 원하는 필드만 명시
3.  b) PasswordChangeForm
4.  c) update_session_auth_hash(request, user)
5.  c) 해싱 (Hashing)
6.  b) 해시값으로 원래 입력값을 쉽게 알 수 있다.
7.  b) 솔트 (Salt) 사용
8.  b) 키 스트레칭 (Key Stretching)
9.  c) PBKDF2
10. d) 사용자 아이디 (username)
11. b) EMAIL\_BACKEND

---

### 상세 해설

1.  **`UserChangeForm`**은 등록된 사용자의 정보를 수정하기 위해 Django에서 기본으로 제공하는 **ModelForm**입니다.
2.  커스텀 폼의 **Meta 클래스** 안에 **`fields` 튜플**에 **`'first_name'`, `'last_name'`** 등 원하는 필드 이름만 지정하여 출력 필드를 제어할 수 있습니다.
3.  **`PasswordChangeForm`**은 사용자가 기존 비밀번호를 입력하고 새 비밀번호로 변경할 수 있도록 돕는 내장 폼입니다.
4.  이 함수는 비밀번호가 변경되었을 때, **새로운 비밀번호 해시값**으로 현재 **세션 정보**를 갱신하여 **로그아웃을 방지**합니다.
5.  해싱은 임의의 데이터를 **고정된 길이**로 변환하는 **단방향 과정**으로, 비밀번호 저장에 사용됩니다.
6.  해시 함수는 **단방향 변환**이 특징이며, **결과 값(해시)**으로는 원본 데이터를 역추적하는 것은 **불가능**합니다.
7.  각 비밀번호에 **'솔트'**라는 **임의의 문자열**을 추가하여 해싱하면, 동일한 비밀번호라도 사용자마다 **다른 해시값**을 갖게 되어 **레인보우 테이블을 무력화**시킵니다.
8.  해시 연산을 의도적으로 수만 번 이상 반복하여 **한 번의 비밀번호 검증에 걸리는 시간을 늘림**으로써, 무차별 대입 공격의 속도를 극단적으로 늦춥니다.
9.  Django는 **솔트**와 **키 스트레칭**을 구현한 **PBKDF2 알고리즘**을 기본값으로 사용하여 안전하게 비밀번호를 저장합니다.
10. Django의 비밀번호 필드 값(예: `<algorithm>$<iterations>$<salt>$<hash>`)에는 **사용자 아이디**는 포함되지 않습니다.
11. 비밀번호 초기화 링크를 이메일로 보내기 때문에, Django가 이메일을 어떻게 처리할지 정의하는 **`EMAIL_BACKEND`** 설정이 필요합니다. (콘솔 테스트 포함)

