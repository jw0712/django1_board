from django.db import models

# 게시물과 관련된 클래스
class Article(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    contents=models.TextField(editable=True)
    url=models.URLField(editable=True)
    email=models.EmailField()
    cdate=models.DateTimeField(auto_now_add=True) #auto-filled
