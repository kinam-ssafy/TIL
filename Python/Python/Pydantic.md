# Pydantic 

# Pydantic: 데이터 유효성 검사 및 설정 관리 라이브러리

Pydantic은 파이썬의 **타입 힌트(type hints)**를 사용하여 데이터의 **유효성을 검사**하고 **설정을 관리**하는 라이브러리입니다.  
외부 데이터를 다룰 때 코드의 안정성과 가독성을 비약적으로 향상시켜 줍니다.  

-----

## 1\. Pydantic이란?

API 응답, JSON 파일, 환경 변수 등 외부에서 들어오는 데이터는 언제나 예상치 못한 형식이나 오류를 포함할 수 있습니다. Pydantic은 이런 데이터를 미리 정의된 데이터 구조(모델)에 맞춰 검증하고, 타입을 강제하며, 안전한 파이썬 객체로 변환해 주는 역할을 합니다.

  - **핵심 개념**: 개발자는 데이터의 '구조'와 '타입'만 클래스로 정의하면, Pydantic이 나머지 검증과 변환을 자동으로 처리합니다.

-----

## 2\. 주요 특징 및 장점

  - ✅ **강력한 유효성 검사**: `int`, `str` 같은 기본 타입은 물론 이메일, URL 등 복잡한 형식까지 자동으로 검증합니다.
  - ⚙️ **자동 타입 변환 (Coercion)**: `id="123"`처럼 문자열로 들어온 값도 `id: int`로 정의되어 있으면 자동으로 정수 `123`으로 변환합니다.
  - 🤝 **IDE 완벽 지원**: 표준 타입 힌트를 사용하므로 VS Code, PyCharm 등에서 코드 자동 완성 및 타입 체크 기능을 완벽하게 활용할 수 있습니다.
  - 🚀 **뛰어난 성능**: 핵심 로직이 Rust로 컴파일되어 있어 매우 빠릅니다.
  - 🧩 **프레임워크 통합**: **FastAPI**의 핵심 구성 요소로, API의 요청(Request) 및 응답(Response) 데이터를 처리하는 데 사용됩니다.

-----

## 3\. 기본 사용법

### 3.1. 설치

```bash
pip install pydantic
```

### 3.2. 모델 정의 및 사용

`BaseModel`을 상속받아 데이터 구조를 클래스로 정의합니다.

```python
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ValidationError

# 1. 데이터 모델 정의
class User(BaseModel):
    id: int
    name: str = 'John Doe'  # 기본값 설정
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

# 2. 데이터 파싱 및 검증
# id가 문자열 '123'이지만 int로 자동 변환됨
external_data = {
    'id': '123',
    'signup_ts': '2022-12-25 12:00',
    'friends': [1, 2, '3'] # 리스트 안의 '3'도 int로 자동 변환
}

try:
    # 딕셔너리를 모델에 주입하여 객체 생성
    user = User(**external_data)
    
    # 성공! 객체 속성으로 안전하게 접근 가능
    print(user.id)  # 출력: 123
    print(user.name) # 출력: John Doe (기본값)
    print(user.model_dump_json(indent=2)) # 검증된 데이터를 JSON으로 출력

except ValidationError as e:
    # 유효성 검증 실패 시, 명확한 에러 출력
    print(e)
```

**성공 시 JSON 출력:**

```json
{
  "id": 123,
  "name": "John Doe",
  "signup_ts": "2022-12-25T12:00:00",
  "friends": [
    1,
    2,
    3
  ]
}
```

-----

## 4\. 주요 사용 사례

### 4.1. API 데이터 검증 (FastAPI)

FastAPI는 Pydantic 모델을 사용하여 클라이언트의 요청 본문을 자동으로 검증합니다.

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.post("/items/")
async def create_item(item: Item):
    # 이 함수가 실행될 때, item은 이미 Pydantic에 의해
    # 검증되고 타입이 변환된 객체입니다.
    return {"message": "Success", "item": item}
```

### 4.2. 설정 관리 (Settings Management)

환경 변수나 `.env` 파일로부터 어플리케이션 설정을 안전하게 불러올 때 매우 유용합니다.

**설치:**

```bash
pip install pydantic-settings
```

**코드:**

```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    # .env 파일을 읽도록 설정
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # 환경 변수와 이름이 같은 속성을 정의
    DATABASE_URL: str
    API_KEY: SecretStr # SecretStr: 값이 로그에 노출되지 않도록 함

# (.env 파일 내용)
# DATABASE_URL="postgresql://user:password@host/db"
# API_KEY="my_secret_api_key"

# 설정 객체 생성
settings = Settings()
print(f"DB URL: {settings.DATABASE_URL}")
print(f"API Key: {settings.API_KEY.get_secret_value()}") # 실제 값 접근
```

-----

## 5\. 자주 사용하는 Field Types

Pydantic은 기본 타입 외에도 다양한 데이터 형식을 검증할 수 있는 타입을 제공합니다.

| 타입 | 설명 |
| :--- | :--- |
| `EmailStr` | 이메일 주소 형식 (`user@example.com`)을 검증합니다. |
| `HttpUrl` | URL 형식 (`http://` 또는 `https://`로 시작)을 검증합니다. |
| `FilePath` | 존재하는 파일의 경로인지 검증합니다. |
| `DirectoryPath` | 존재하는 디렉토리의 경로인지 검증합니다. |
| `PositiveInt` | 0보다 큰 양의 정수인지 검증합니다. |
| `NegativeFloat` | 0보다 작은 음의 실수인지 검증합니다. |
| `SecretStr` | 로그나 출력 시 값이 노출되지 않도록 마스킹 처리되는 문자열입니다. |
| `UUID` | UUID (1, 3, 4, 5) 형식을 검증합니다. |

-----

## 6\. 요약

Pydantic은 신뢰할 수 없는 외부 데이터를 **안전하고 쓰기 편한 파이썬 객체**로 변환해 주는 필수 도구입니다.   
데이터 검증 로직을 직접 작성하는 수고를 덜어주고, 타입 힌트와 결합하여 코드의 안정성과 유지보수성을 크게 향상시킵니다.  
특히 API 서버를 개발하거나 복잡한 설정을 다룰 때 강력한 힘을 발휘합니다.