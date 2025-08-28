# Web
## Responsive Web

## 목차

### Bootstrap Grid system

* Grid system 구조

---

### Grid system for responsive web

* Grid system Breakpoints
* Breakpoints 실습

---

### CSS Layout 종합 정리

### UX & UI

* UX
* UI

---

### 참고

* The Grid System
* Grid cards
* UI Design Guidelines

### Bootstrap Grid system

* 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템임.
* 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움.
* Grid system에 대한 자세한 설명은 참고 자료에서 확인할 수 있음.

### 반응형 웹 디자인 (Responsive Web Design)

* 디바이스 종류나 화면 크기에 상관없이 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술임.
* 32인치 모니터, 태블릿, 스마트폰 등 화면 크기에 따라 요소의 배치를 변경하여 일관된 사용자 경험을 제공할 수 있음.

### Grid system 기본 요소 (1/4)

* **Container**: `Column`들을 담고 있는 공간.

![alt text](image/image34.png)

* **Column**: 실제 콘텐츠를 포함하는 부분

![alt text](image/image35.png)

* **Gutter**: 컬럼과 컬럼 사이의 여백 영역(상하좌우).

![alt text](image/image36.png)

  * 1개의 `row` 안에 12개의 `column` 영역이 구성됨.
  * 각 요소는 12개 중 몇 개를 차지할 것인지 지정됨.

-----

### 코드 예시

```html
<div class="container">
    <div class="row">
        <div class="col-4"></div>
        <div class="col-4"></div>
        <div class="col-4"></div>
    </div>
</div>
```

![alt text](image/image37.png)

## Grid System 실습

![alt text](image/image38.png)

- 첫 번째 줄

![alt text](image/image39.png)

### Bootstrap Grid System 예시

  * **HTML 코드**:

<!-- end list -->

```html
<div class="container">
    <div class="row">
        <div class="col">
            <div class="box">col</div>
        </div>
        <div class="col">
            <div class="box">col</div>
        </div>
        <div class="col">
            <div class="box">col</div>
        </div>
    </div>
</div>
```

  * **CSS 코드**:

<!-- end list -->

```css
.box {
    border: 1px solid black;
    background-color: lightblue;
    text-align: center;
}
```

- 두번째 줄
![alt text](image/image40.png)

### Bootstrap Grid System 예시

  * **HTML 코드**:

<!-- end list -->

```html
<div class="container">
    <div class="row">
        <div class="col-4">
            <div class="box">col-4</div>
        </div>
        <div class="col-4">
            <div class="box">col-4</div>
        </div>
        <div class="col-4">
            <div class="box">col-4</div>
        </div>
    </div>
</div>
```

  * **CSS 코드**:

<!-- end list -->

```css
.box {
    border: 1px solid black;
    background-color: lightblue;
    text-align: center;
}
```

- 세번째 줄

![alt text](image/image41.png)

### Bootstrap Grid System 예시

  * **HTML 코드**:

<!-- end list -->

```html
<div class="container">
    <div class="row">
        <div class="col-2">
            <div class="box">col-2</div>
        </div>
        <div class="col-8">
            <div class="box">col-8</div>
        </div>
        <div class="col-2">
            <div class="box">col-2</div>
        </div>
    </div>
</div>
```
### 하나의 Column에 또다른 Row 넣기

![alt text](image/image42.png)

### Bootstrap Grid System 예시

  * **HTML 코드**:

<!-- end list -->

```html
<div class="container">
    <div class="row">
        <div class="col-4 box">
            <div>col-4</div>
        </div>
        <div class="col-8 box">
            <div class="row">
                <div class="col-6">
                    <div class="box">col-6</div>
                </div>
                <div class="col-6">
                    <div class="box">col-6</div>
                </div>
                <div class="col-6">
                    <div class="box">col-6</div>
                </div>
                <div class="col-6">
                    <div class="box">col-6</div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Offset으로 Column 생략하기

![alt text](image/image43.png)

### Bootstrap Grid System `offset` 예시

  * **HTML 코드**:

<!-- end list -->

```html
<div class="container">
    <div class="row">
        <div class="col-4 offset-4">
            <div class="box">col-4 offset-4</div>
        </div>
    </div>
    <div class="row">
        <div class="col-3 offset-3">
            <div class="box">col-3 offset-3</div>
        </div>
        <div class="col-3 offset-3">
            <div class="box">col-3 offset-3</div>
        </div>
    </div>
    <div class="row">
        <div class="col-6 offset-3">
            <div class="box">col-6 offset-3</div>
        </div>
    </div>
</div>
```

### Gutters

* Grid system에서 `column` 사이의 여백 영역.
* x축은 `padding`, y축은 `margin`으로 여백을 생성함.
* 실제 컬럼 간의 좌우 간격(x축)은 변하지 않으며, `padding`으로 인해 컬럼 안의 콘텐츠(`contents`) 너비가 변함.

![alt text](image/image44.png)

### Grid System 실습 - gutters (1/3)

  * `Gutter`를 이용해 간격을 조정함.
      * `gx-0`: 좌우 여백 제거
      * `col` 사이 여백 제거

-----

### 코드 및 결과

  * **HTML 코드**:

<!-- end list -->

```html
<div class="container">
    <div class="row gx-0">
        <div class="col-6">
            <div class="box">col</div>
        </div>
        <div class="col-6">
            <div class="box">col</div>
        </div>
    </div>
</div>
```

![alt text](image/image45.png)

  * **결과**: `gx-0` 클래스 적용으로 `col` 사이의 가로 여백이 제거됨.


  ### Grid System 실습 - gutters (2/3)

  * `Gutter`를 이용해 간격을 조정함.
      * `gy-5`: `row` 사이의 여백 증가

-----

### 코드 및 결과

  * **HTML 코드**:

<!-- end list -->

```html
<div class="container">
    <div class="row gy-5">
        <div class="col-6">
            <div class="box">col</div>
        </div>
        <div class="col-6">
            <div class="box">col</div>
        </div>
        <div class="col-6">
            <div class="box">col</div>
        </div>
        <div class="col-6">
            <div class="box">col</div>
        </div>
    </div>
</div>
```

![alt text](image/image46.png)

  * **결과**: `gy-5` 클래스 적용으로 두 번째 줄의 `row`에 세로 여백이 증가함.


### Grid System 실습 - gutters (3/3)

  * `Gutter`를 이용해 간격을 조정함.
      * `g-5`: 가로/세로 여백 모두 증가

-----

### 코드 및 결과

  * **HTML 코드**:

<!-- end list -->

```html
<div class="container">
    <div class="row g-5">
        <div class="col-6">
            <div class="box">col</div>
        </div>
        <div class="col-6">
            <div class="box">col</div>
        </div>
        <div class="col-6">
            <div class="box">col</div>
        </div>
        <div class="col-6">
            <div class="box">col</div>
        </div>
    </div>
</div>
```

![alt text](image/image47.png)

  * **결과**: `g-5` 클래스 적용으로 `row` 안의 `col` 사이의 가로 및 세로 여백이 모두 증가함.



## Responsive Web Design

* 디바이스 종류나 화면 크기에 상관없이 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술.
* Bootstrap grid system에서는 12개의 `column`과 6개의 `breakpoints`를 사용하여 반응형 웹 디자인을 구현함.  

### Grid system breakpoints

* 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점임.
* 화면 너비에 따라 6개의 분기점을 제공함(`xs, sm, md, lg, xl, xxl`).

---

### Breakpoints 정보

| | **xs** | **sm** | **md** | **lg** | **xl** | **xxl** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| | <576px | ≥576px | ≥768px | ≥992px | ≥1200px | ≥1400px |
| **Container** `max-width` | None(auto) | 540px | 720px | 960px | 1140px | 1320px |
| **Class prefix** | `.col-` | `.col-sm-` | `.col-md-` | `.col-lg-` | `.col-xl-` | `.col-xxl-` |

---

* 각 `breakpoints`마다 설정된 최대 너비 값 "이상"으로 화면이 커지면 `grid system` 동작이 변경됨.

