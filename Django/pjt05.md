## 목차

### AbstractUser
### Model Fields 심화
  * choices 속성
  * choices 속성 실습
  * PositiveIntegerField
  * blank vs. null
### Django Form 심화
  * 다양한 Form 살펴보기
  * MultipleChoiceField
  * MultipleChoiceField 실습
  * cleaned_data
### 관통 프로젝트 안내


## AbstractUser

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

Django의 기본 User model과 동일한 모습으로 대체만 한 상황


## AbstractUser의 필드

|필드명|데이터 타입|설명|
|:---|:---|:---|
|id|INTEGER|자동 생성 기본 키|
|**password**|varchar(128)|암호화된 비밀번호|
|last\_login|datetime|날짜/시간 정보|
|is\_superuser|bool|권한 관련 필드|
|**username**|varchar(150)|유저 식별용 문자열|
|first\_name|varchar(150)|프로필 정보|
|last\_name|varchar(150)|프로필 정보|
|**email**|varchar(254)|프로필 정보|
|is\_staff|bool|권한 관련 필드|
|is\_active|bool|활성화 상태|
|date\_joined|datetime|날짜/시간 정보|

---

### 주요 필드별 역할

* **username**: 유저 식별용 문자열
* **password**: 암호화된 비밀번호
* **email**, first\_name, last\_name: 프로필 정보
* **is\_staff**, **is\_superuser**: 권한 관련 필드
* date\_joined, last\_login: 날짜/시간 정보


## AbstractUser를 사용하는 이유

* "기존 User 모델은 그대로 쓰고, 우리가 원하는 필드만 몇 개 더 추가하고 싶다."

* Django의 기본 User 모델에는 **username**, **email**, **password** 등 필수적인 필드들이 이미 포함되어 있음

* **AbstractUser**를 상속받아 커스텀 유저 모델을 만들면, 기존의 편리한 필드들은 그대로 물려받으면서, 우리가 원하는 추가적인 필드(예: 닉네임, 프로필 사진, 생년월일 등)만 손쉽게 정의하여 확장할 수 있기 때문


## AbstractUser 커스터마이징 예시

  * 우리가 원하는 필드를 추가한 models.py 예시

  * 이처럼 **AbstractUser**는 Django의 검증된 인증 시스템을 그대로 활용하면서, 프로젝트에 필요한 사용자 정보를 유연하게 추가할 수 있는 가장 표준적이고 편리한 방법

<!-- end list -->

```python
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 기존 필드들은 모두 상속받음
    
    # --- 우리가 추가하고 싶은 필드들 ---
    nickname = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
```


-----------

# Model Fields 심화

## choices 속성

  * "모델 필드에 미리 정해진 선택지를 부여하는 속성"

  * 이 속성을 사용하면, 데이터베이스에는 실제 값이 저장되지만 사용자에게는 더 이해하기 쉬운 이름(레이블)을 보여주는 드롭다운(Dropdown) 메뉴를 손쉽게 만들 수 있음





<!-- end list -->

```python
# todos/models.py
class Todo(models.Model):
    STATUS_CHOICES = [
        ('TODO', '할 일'),
        ('DOING', '진행 중'),
        ('DONE', '완료'),
    ]

    status = models.CharField(
        max_length=5,
        choices=STATUS_CHOICES,
        default='TODO',
    )
```

**choices=STATUS\_CHOICES**를 통해 드롭다운 메뉴 생성 가능

### choices 사용 방법

* (**저장될 실제 값**, **사용자에게 보여줄 이름**) 형태의 튜플을 담은 리스트 또는 튜플로 정의

### choices 동작 원리

* Django는 **choices** 속성이 지정된 필드를 발견하면, **ModelForm**이나 관리자 페이지에서 자동으로 기본 텍스트 입력 창 대신 드롭다운(**select**) 위젯으로 렌더링

* 사용자가 '**진행 중**'을 선택하고 저장하면, 데이터베이스의 **status** 필드에는 **'DOING'** 이라는 문자열이 저장됨




## choices 변수명 정의하는 법

* **STATUS\_CHOICES**처럼 전체 대문자(**UPPERCASE**)로 명명하는 것이 Django 커뮤니티의 오랜 관례(**convention**)

---

### 왜 대문자를 사용할까?

* 파이썬의 공식 스타일 가이드인 **PEP 8**의 '상수(**Constants**)' 명명 규칙을 따르는 것

* **choices**에 할당되는 리스트나 튜플은 한 번 정의된 후 프로그램이 실행되는 동안 **값이 변하지 않는** '상수'로 취급됨

* 코드 작성자들은 다른 개발자에게 "이 변수는 고정된 값이니, 절대 수정하지 마세요!"라는 시각적인 신호를 주기 위해 대문자로 변수명을 짓는 것을 선호

> 필수는 아니지만, '상수'임을 명확히 하여 코드의 가독성과 안정성을 높이기 위한 좋은 습관



## choices 속성 실습

### 사전 준비

1.  마이그레이션 과정 진행
      * ```bash
          python manage.py makemigrations
        ```
      * ```bash
          python manage.py migrate
        ```
2.  관리자 계정 생성
      * ```bash
          python manage.py createsuperuser
        ```


## CharField와 choices (1/3)

### 1\. STATUS\_CHOICES 리스트 정의

  * DB에는 **'TODO'**, **'DOING'**, \*\*'DONE'\*\*이 저장
  * Admin site나 Django Form에서는 **“할 일”**, **“진행 중”**, **“완료”** 라는 레이블로 표시됨

<!-- end list -->

```python
# todos/models.py
# 1) CharField + choices
STATUS_CHOICES = [
    ('TODO', '할 일'),
    ('DOING', '진행 중'),
    ('DONE', '완료'),
]
```


## CharField와 choices (2/3)

### 2\. 필드 정의

  * **choices**: 미리 정의된 값들만 선택할 수 있도록 제한
  * **default**: 사용자가 값을 입력하지 않았을 때 자동으로 할당되는 기본값
  * **help\_text**: Admin이나 Form에서 해당 필드 옆에 간단한 안내문으로 표시되는 설명
  * **verbose\_name**: Admin이나 Form에서 필드의 레이블로 표시될 텍스트

<!-- end list -->

```python
# todos/models.py
status = models.CharField(
    max_length=5,
    choices=STATUS_CHOICES,
    default='TODO',
    help_text='현재 작업 상태를 선택해주세요.',
    verbose_name='상태',
)
```

## CharField와 choices (3/3)

### 3. Admin Site 결과 확인

* 새로운 할 일 등록 시 출력되는 레이블과 **help text**를 확인 가능



## IntegerField와 choices

### 1\. PRIORITY\_CHOICES 리스트 정의

  * DB에는 정수 **1, 2, 3**이 저장
  * Admin site나 Django Form에서는 **“낮음”**, **“보통”**, **“높음”** 으로 표시됨

<!-- end list -->

```python
# todos/models.py
# 2) IntegerField + choices
PRIORITY_CHOICES = [
    (1, '낮음'),
    (2, '보통'),
    (3, '높음'),
]

priority = models.PositiveIntegerField(
    choices=PRIORITY_CHOICES,
    default=2,
    help_text='우선순위를 선택해주세요 (1=낮음, 2=보통, 3=높음).',
    verbose_name='우선순위',
)
```


## choices 속성 정리

* **choices**는 마치 자판기의 상품 코드와 같음

* 개발자(자판기 내부)
  * 상품을 관리하기 위해 간결하고 규칙적인 코드(**item\_01, item\_02** 등)를 사용

* 사용자(자판기 외부)
  * 상품을 쉽게 알아볼 수 있도록 친절한 이름(**"콜라", "사이다"** 등)을 보고 버튼을 누름

> **choices**는 이처럼, 데이터베이스에는 **정해진 값(코드)**을 저장하여 데이터의 일관성을 유지하고, 사용자 화면에는 **친절한 이름(레이블)**을 보여주어 사용성을 높이는 역할


---------------
# PositiveIntegerField
## PositiveIntegerField란

* **"0을 포함한 양의 정수만 저장할 수 있도록 강제하는 Django 모델 필드"**

* 데이터베이스에는 일반 정수(**Integer**) 타입으로 생성되지만, Django의 유효성 검사(**validation**)를 통해 음수 값이 저장되려고 하면 오류를 발생시켜 데이터의 무결성을 보장

---

### 주요 활용 사례

* **수량**: 재고 수량, 주문 개수
* **수치**: 나이, 조회수, 좋아요 수
* **포인트 및 금액**: 포인트, 가격, 예산

> '음수'가 될 수 없는 모든 종류의 숫자 데이터에 사용하는 것이 적합


## PositiveIntegerField의 사용 예(1/2)

  * 데이터 무결성

      * 실제 우선순위가 음수가 될 일은 없으므로, 애초에 DB에 음수가 들어가지 않도록 방지

  * 유효성 검사

      * Django가 자동으로 **0 이상** 값만 허용하므로, 음수 입력 시 **ValidationError** 발생

  * 가독성/의도 표현

      * "우선순위 = 양의 정수"라는 로직이 모델 정의에 드러나, 코드 유지보수에 유리함

<!-- end list -->

```python
# todos/models.py
priority = models.PositiveIntegerField(
    choices=PRIORITY_CHOICES,
    default=2,
    help_text='우선순위를 선택해주세요 (1=낮음, 2=보통, 3=높음).',
    verbose_name='우선순위',
)
```


## PositiveIntegerField의 사용 예(2/2)

  * 유저 관련 프로필 모델 예시

<!-- end list -->

```python
class Profile(models.Model):
    age = models.PositiveIntegerField(blank=True, null=True, default=0)
    weekly_avg_reading_time = models.PositiveIntegerField(blank=True, null=True)

    # blank, null 옵션 가능
    # default 옵션으로 0 등 지정 가능
```


# blank & null
## blank & null

모두 ‘비어 있음’과 관련된 설정처럼 보이지만

**동작 레벨이 서로 다름**


## blank vs null 비교

  * Form에서 빈 값 허용(**blank=True**)은 DB의 **NULL**과 직접 대응하지 않음
  * DB 컬럼을 **NULL** 허용(**null=True**)해도, 폼 입력에서는 여전히 필수 값이 될 수 있음

|속성|적용 레벨|역할|주 사용 대상|
|:---|:---|:---|:---|
|**blank=True**|Form validation|- Form 레벨에서 해당 필드를 \*\*"필수 입력이 아님"\*\*으로 처리<br>- Admin, ModelForm 등에서 빈 값으로 제출 가능|문자열 필드 (**CharField**, **TextField**)|
|**null=True**|DB|- DB 레벨에서 **NULL** 값 허용<br>- DB 컬럼이 **NULL**을 저장할 수 있도록 설정|문자열 외 필드 (**IntegerField**, **DateTimeField** 등)|



## blank=True의 의미

### 1\. Form 유효성 검사 차원

  * **blank=True**로 지정된 필드는 폼에서 필수 입력이 아님
  * Admin이나 **ModelForm**에서 해당 필드를 비워 제출해도 검증 에러가 발생하지 않음

### 2\. DB와는 무관

  * 단지 Django의 **Form**이나 **admin**에서 "**비워둘 수 있다**"는 의미
  * DB에는 \*\*""(빈 문자열)\*\*로 저장될 수 있지만, 실제로 DB가 **NULL** 상태가 되는 것은 아님 (기본적으로 **null=False**일 때)

<!-- end list -->

```python
# 폼 검증: 빈 값 제출 가능
# DB에 "" (빈 문자열)로 저장
title = models.CharField(max_length=100, blank=True)
```


## null=True의 의미

### 1\. DB 스키마 레벨

  * **null=True**면 해당 컬럼에 **NULL** 값을 저장 가능

### 2\. Form 검증과는 별개

  * Django Form에서 **blank=True**가 아니면 여전히 필수 입력으로 간주
  * 즉, DB에서 **NULL**을 허용하더라도, Form에서 공백 제출을 막을 수 있음

<!-- end list -->

```python
# DB 컬럼이 NULL을 허용 -> 데이터베이스에 NULL로 저장 가능
# 그러나 blank=False라면 Django 폼에서 여전히 필수 값
content = models.TextField(null=True)
```


## 문자열 필드에 null=True를 설정하는 것은 일반적으로 **권장하지 않음**

  * 이유: **두 가지 종류의 '빈 값'**

  * 문자열 필드에 **null=True**를 허용하면, 데이터베이스에 \*\*'값이 없음'\*\*을 나타내는 상태가 두 가지가 되어 버림

      * **NULL**: 데이터베이스 수준의 값이 존재하지 않음
      * **'빈 문자열'** (`''`): 길이가 0인 문자열 값이 존재함

  * 대부분의 웹 애플리케이션에서는 이 두 상태를 굳이 구분해서 처리해야 할 이유가 없음. "**사용자가 아무것도 입력하지 않았다**"는 것을 표현하는 데에는 빈 문자열(**""**) 하나만으로도 충분

<!-- end list -->

```python
title = models.CharField(max_length=100, blank=True, null=True) # X 권장하지 않음
```


## 정리

* **blank=True**: 웹 페이지의 '**서류 양식**'에 대한 규칙
  * "**이 칸은 비워둔 채로 제출해도 괜찮습니다.**"라는 의미로, 유효성 검사(**validation**) 단계와 관련 있음

* **null=True**: 데이터가 저장되는 '**서류 보관함(DB)**'에 대한 규칙
  * "**이 칸에 해당하는 서류가 아예 없어도(**NULL**) 괜찮습니다.**"라는 의미로, 데이터베이스 스키마 단계와 관련 있음


--------
# Django Form 심화
## Django Form

다양한 모델 필드를 정의했지만, **사용자에게 입력을 받으려면 결국 HTML Form이 필요함**


## Django Form을 활용한 이점

* "**자동 검증과 편의성, 필요하다면 ModelForm을 통해 DB까지 손쉽게 연결 가능**"


<br>

-------------
# 다양한 Form 살펴보기 
## 사전 준비

  * 기본 모델 정의

<!-- end list -->

```python
# formsapp/models.py

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('BOOK', 'Books'),
        ('FASH', 'Fashion'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )
```


## 1\. 기본 Form

  * [http://127.0.0.1:8000/formsapp/form-1/](https://www.google.com/search?q=http://127.0.0.1:8000/formsapp/form-1/)

<!-- end list -->

```python
# formsapp/forms.py

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
```


## 2\. ModelForm

  * [http://127.0.0.1:8000/formsapp/form-2/](https://www.google.com/search?q=http://127.0.0.1:8000/formsapp/form-2/)

<!-- end list -->

```python
# formsapp/forms.py

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']
```


## 3\. Form 상속 (부모 Form)

  * [http://127.0.0.1:8000/formsapp/form-3/](https://www.google.com/search?q=http://127.0.0.1:8000/formsapp/form-3/)

<!-- end list -->

```python
# formsapp/forms.py

class BaseForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
```


## 5\. Widget을 활용한 Form

  * [http://127.0.0.1:8000/formsapp/form-5/](https://www.google.com/search?q=http://127.0.0.1:8000/formsapp/form-5/)

<!-- end list -->

```python
# formsapp/forms.py

class WidgetForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'cols': 50,
                'class': 'form-control',
            }
        ),
        required=False,
    )
```



---------------
# MultipleChoiceField
## MultipleChoiceField

Form에서 여러 개의 선택지를 동시에 선택할 수 있도록 해주는 필드

> 사용자가 제출하면, 선택된 값들은 파이썬 리스트(**list**) 형태로 처리


## 핵심 특징 및 사용법

### HTML 렌더링

  * 기본적으로 여러 줄 선택이 가능한 `<select multiple>` 태그로 렌더링되지만, **widget** 옵션을 통해 체크박스(**Checkbox**) 형태로 더 편리하게 바꿀 수 있음

<!-- end list -->

```python
class MyForm(forms.Form):
    FAVORITE_COLORS = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ]

    colors = forms.MultipleChoiceField(
        choices=FAVORITE_COLORS,
        widget=forms.CheckboxSelectMultiple,
    )
```

※ 사용자가 “Red”, “Blue” 등을 체크하면, 백(서버)으로 넘어오는 폼 데이터는 **['red', 'blue']** 같은 리스트 형태로 전달


## MultipleChoiceField 실습

### 여러 값 입력 받기 - Product 모델 수정 (1/6)

  * **formsapp/models.py**의 **Product** 모델 수정
  * 수정 후 **makemigrations** 및 **migrate** 진행

#### 기존 코드 주석 처리

```python
# 기존 코드 주석 처리
class Product(models.Model):
    ...
    # CATEGORY_CHOICES = [
    #     ('ELEC', 'Electronics'),
    #     ('BOOK', 'Books'),
    #     ('FASH', 'Fashion'),
    # ]
    #
    # category = models.CharField(
    #     max_length=20,
    #     choices=CATEGORY_CHOICES,
    # )
```

#### 새로운 코드 주석 해제

```python
# 새로운 코드 주석 해제
class Product(models.Model):
    ...
    category = models.CharField(
        max_length=500,
        help_text='콤마로 구분된 카테고리 코드',
        blank=True,
        verbose_name='카테고리',
    )
```

## 여러 값 입력 받기 - Product 모델 수정 (2/6)

  * **formsapp/forms.py**의 **ProductForm** 수정
  * **CATEGORY\_CHOICES** 및 **category** 주석 해제

<!-- end list -->

```python
class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('BOOK', 'Books'),
        ('FASH', 'Fashion'),
    ]

    category = forms.MultipleChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
        help_text='하나 이상의 카테고리를 선택하세요',
        # widget=forms.CheckboxSelectMultiple, # 체크박스 형태로 렌더링
    )
```


## 여러 값 입력 받기 - save 로직 확인 (3/6)

  * **formsapp/views.py**의 **form2** view 함수 확인

<!-- end list -->

```python
def form2(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False) # 저장하지 않고 인스턴스 반환
            print(f'cleaned_data: {form.cleaned_data}') # cleaned_data 확인
            print(f'cleaned_data 타입: {type(form.cleaned_data)}') # cleaned_data 타입 확인
            category_values = form.cleaned_data.get('category', [])
            category_string = ','.join(category_values) # 카테고리 데이터를 콤마로 구분된 문자열로 변환
            product.category = category_string
            product.save()
            messages.success(
                request,
                f"제품 '{product.name}'이(가) 성공적으로 저장되었습니다!"
            )
    return redirect('formsapp:form2')
```


## 여러 값 입력 받기 - Widget 변경 (5/6)

```python
# formsapp/forms.py
class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('BOOK', 'Books'),
        ('FASH', 'Fashion'),
    ]

    category = forms.MultipleChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
        help_text='하나 이상의 카테고리를 선택하세요',
        widget=forms.CheckboxSelectMultiple,
    )
```

**Category** 필드는 **CheckboxSelectMultiple** 위젯을 사용하여 체크박스 형태로 렌더링

-----

# cleaned_data
## cleaned\_data란

* "Django 폼에서 유효성 검사를 성공적으로 통과한 **"깨끗한"** 데이터를 담고 있는 파이썬 딕셔너리"
* 사용자가 폼에 입력한 데이터는 마치 공항에 들어오는 승객들의 짐과 같음
* **cleaned\_data**는 보안 검색대(**is\_valid()**)를 통과하여 안전하다고 확인된 짐들만 모아놓은 곳

---

* **request.POST**: 승객들이 들고 온 모든 종류의 짐 (**검증되지 않음**, 문자열 형태)
* **form.is\_valid()**: 보안 검색대 (**유효성 검사 과정**)
* **form.cleaned\_data**: 검색대를 통과한 안전한 짐 (**검증 완료**, 올바른 파이썬 타입으로 변환됨)



## cleaned\_data 주요 특징

### 접근 시점

* 반드시 **form.is\_valid()**가 **True**를 반환한 이후에만 접근 가능

### 데이터 타입

* **request.POST**에 담긴 데이터는 모두 문자열(**str**)이지만, **cleaned\_data**에 담긴 데이터는 각 필드에 맞는 올바른 파이썬 타입(예: **IntegerField** -> **int**, **DateField** -> **datetime.date**)으로 자동 변환됨

### 활용

* 데이터베이스에 저장하기 직전에, 검증된 데이터를 가지고 추가적인 로직(예: 특정 단어 필터링)을 수행하고 싶을 때 유용하게 사용 가능


