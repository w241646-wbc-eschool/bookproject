from django.db import models

# Create your models here.

# class SampleModel(models.Model): #コード追記
#     title = models.CharField(max_length = 100) #コード追記
#     number = models.IntegerField() #コード追記

CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他')) #コード追記

from .consts import MAX_RATE #コード追記（5-7（P.215））
RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)] #コード追記（5-7（P.215））


class Book(models.Model): #コード追記
  title = models.CharField(max_length = 100) #コード追記
  text = models.TextField() #コード追記
  thumbnail = models.ImageField(null=True, blank=True) #コード追記（5-8（P.232、P.234））
  category = models.CharField(
    max_length = 100,
    choices = CATEGORY
    ) #コード追記
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE) #コード追記（5-11（P.251））

# ↓ 管理画面の「Book」にタイトルを表示させるために記述
  def __str__(self): #コード追記
    return self.title #コード追記


#コード追記（5-7（P.215））
class Review(models.Model):
  book = models.ForeignKey(Book, on_delete = models.CASCADE)
  title = models.CharField(max_length = 100)
  text = models.TextField()
  rate = models.IntegerField(choices = RATE_CHOICES)
  user = models.ForeignKey('auth.User', on_delete = models.CASCADE)

  def __str__(self):
    return self.title

