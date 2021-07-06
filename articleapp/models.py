from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from projectapp.models import Project

class Article(models.Model):
    writer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,   # User 삭제(회원탈퇴) 시, article이 사라지지 않고 계정 정보를 Null로 변경
        related_name='article',      # User 객체에서 Article에 접근하기 위한 이름
        null=True,
    )
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)         # static/article에 이미지 저장
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)         # 자동 생성 시간 입력. auto_now_add 최초 한번만 입력 됨