from django.contrib import admin
# 将ArticlePost数据表添加到后台进行管理
from .models import ArticlePost

# Register your models here.

# 注册ArticlePost到admin
admin.site.register(ArticlePost)