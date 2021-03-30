#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    re_path('^delete/(\d+)$', views.user_delete, name='delete'),
    re_path('^edit/(\d+)$', views.profile_edit, name='edit'),
]