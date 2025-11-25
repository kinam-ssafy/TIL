DRF 실습 코드.

articles는 app
drf는 pjt name

```python
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# DRF의 모든 뷰 함수는 반드시 api_view 데코레이터가 필수.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 데이터 조회
        articles = Article.objects.all()
        # Serialization 진행
        serializer = ArticleListSerializer(articles, many=True)
        # serializer 덩어리에서 데이터 추출 (.data 속성)한 것을 응답
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # 예전 코드
        # form = ArticleForm(request.POST)
        # 1. 사용자가 보낸 입력 데이터를 직렬화
        serializer = ArticleSerializer(data=request.data)
        # 2. 직렬화된 데이터를 유효성 검사
        if serializer.is_valid():
            # 3. 저장
            serializer.save()
            # 4. 저장이 성공했다는 응답 (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 5. 저장이 실패했다는 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PATCH'])
def article_detail(request, article_pk):
    # 단일 게시글 조회
    # article = Article.objects.get(pk=article_pk)

    # 단일 게시글 조회 + 이 게시글에 작성된 댓글의 개수 데이터
    article = Article.objects.annotate(num_of_comments=Count('comment')).get(pk=article_pk)

    if request.method == 'GET':
        # 조회 한 결과를 직렬화
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        # 과거 코드
        # form = ArticleForm(request.POST, instance=article)
        # 1. 사용자로부터 새로운 입력 데이터를 받아 직렬화 진행(+ 기존 데이터)
        # serializer = ArticleSerializer(article, data=request.data)
        # 데이터 일부만 수정하려면 partial=True를 설정해야 함
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # serializer = ArticleSerializer(instance=article, data=request.data)
        # 2. 직렬화 결과를 유효성 검사
        if serializer.is_valid():
            serializer.save()
            # 3. 수정이 성공했다는 응답
            return Response(serializer.data)
        # 4. 수정이 실패했다는 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request):
    # 1. 전체 댓글 조회
    comments = Comment.objects.all()
    # 2. 전체 댓글 쿼리셋 데이터를 직렬화
    serializer = CommentSerializer(comments, many=True)
    # 3. 가공된 데이터 덩어리에서 json 데이터를 추출
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    # 1. 단일 댓글 조회
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        # 2. 단일 댓글 데이터를 직렬화
        serializer = CommentSerializer(comment)
        # 3. 가공된 데이터 덩어리에서 json 데이터를 추출
        return Response(serializer.data)

    elif request.method == 'PUT':
        # 1. 사용자 입력 데이터 + 기존 댓글 데이터를 함께 직렬화
        serializer = CommentSerializer(comment, data=request.data)
        # 2. 유효성 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request, article_pk):
    # 1. 단일 게시글 조회
    article = Article.objects.get(pk=article_pk)
    # 2. 사용자 입력 데이터를 받아서 직렬화
    serializer = CommentSerializer(data=request.data)
    # 3. 유효성 검사
    if serializer.is_valid(raise_exception=True):
        # 4. 외래키 데이터 추가
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


```

```python
# articles/urls.py

from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]

```

```python
# articles/serializers.py


from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    # 역참조 매니저 이름으로 응답에 제공할 필드를 재정의
    # (주의! 역참조 매니저 이름이 아니면 동작하지 않음)

    # 만약 comment_set이 아닌 다른 이름으로 사용하고 싶다면
    # models.py에서 외래키 필드에서 related_name 설정으로 변경하고,
    # 여기서도 related_name의 값으로 변경해야 한다.
    comment_set = CommentDetailSerializer(many=True, read_only=True)

    # 댓글 개수를 제공할 새로운 읽기 전용 필드를 정의
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_num_of_comments(self, obj):
        # 왜 이런 함수를 호출하는 구조로 되었을까?
            # gpt의 응답 결과를 받아서 반환
            # 여러가지
            # 코드들이
            # 작성 됨
            # 그 결과를 새로운 필드에 반환 하는 구조...
        return obj.num_of_comments



class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):

    # 게시글의 제목만 직렬화 해주는 도구
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title',)

    # article 필드에 대한 데이터 재정의(덮어쓰기)
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)

```

```python
# articles/models.py

from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

```python
# drf/urls.py

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('articles.urls')),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


```

## api 응답 받아서 json을 python에서 사용하



```python
# 프로젝트 폴더와 같은 위치에 다음과 같은 코드 작성

import requests
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/articles/')

# json을 python 타입으로 변환
result = response.json()

print(type(result))
# pprint(result)
pprint(result[0])
# pprint(result[0].get('title'))

```

```python
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


# @api_view(['GET'])
@api_view()
def article_json(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

```python 
#my_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```