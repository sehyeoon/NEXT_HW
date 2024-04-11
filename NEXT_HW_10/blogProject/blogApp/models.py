from django.db import models

# Create your models here.
class Article(models.Model):
    category_choices = [
        ('option1', '취미'),
        ('option2', '음식'),
        ('option3', '프로그래밍'),]
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=category_choices, default='option1')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    def __str__(self):
        return self.content[:20]
    
