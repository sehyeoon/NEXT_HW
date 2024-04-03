from django.db import models
from django.utils import timezone 

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    CATEGORY_CHOICES = [
        ('취미', '취미'),
        ('음식', '음식'),
        ('프로그래밍', '프로그래밍'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)  # 카테고리 선택 필드
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title