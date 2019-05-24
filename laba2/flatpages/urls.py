# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views as core_views

app_name = 'flatpagesapp'
urlpatterns = [
    path('', core_views.home, name = 'home'),
    path('hello', core_views.home, name='hello'),
    url(r'^register/$', core_views.register, name='register'),
]