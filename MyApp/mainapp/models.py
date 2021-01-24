from django.db import models


# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title')
    MainText = models.TextField(null=True, verbose_name='Text', )
    Email = models.EmailField(null=True, verbose_name='Email')
    Price = models.IntegerField(null=True, verbose_name='Price')
    DataPublish = models.DateTimeField((auto_now_add=True, verbose_name='Date')
