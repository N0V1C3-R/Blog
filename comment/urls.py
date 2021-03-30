#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('post_comment/<int:article_id>/', views.post_comment, name='post_comment')
]