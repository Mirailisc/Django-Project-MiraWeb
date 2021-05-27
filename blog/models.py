from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Article(models.Model):
    article_name = models.CharField(max_length=250)
    articlk_info = models.CharField(max_length=250)
    article_link = models.URLField(max_length=200)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

