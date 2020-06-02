from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=500) #No such colums 에러.. 모델 변수이름 바꾸면 꼭 migrate해주자

    def __str__(self):
        return self.title