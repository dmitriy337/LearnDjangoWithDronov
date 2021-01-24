from django.db import models


# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title')
    MainText = models.TextField(null=True, verbose_name='Text', )
    Price = models.IntegerField(null=True, verbose_name='Price')
    DataPublish = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-DataPublish', 'Title']

class LearnModels(models.Model):
    class Kinds(models.IntegerChoices):
        BUY = 1, 'Куплю'
        SELL = 2, 'Продам'
        EXCHANGE = 3, 'Обменяю'

    Kind = models.SmallIntegerField(choices=Kinds.choices, default=Kinds.SELL)

    Email = models.EmailField(null=True, verbose_name='Email')
     