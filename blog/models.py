from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) #짧은 내용 입력
    content = models.TextField() #긴내용 입력
    #작성 시간
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'