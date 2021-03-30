from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# timezone用于处理时间相关事务
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# 博客文章数据模型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)

    # 创建内部类定义数据为根据更新时间倒序排列
    class Meta:
        ordering = ('-update', )
        def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])