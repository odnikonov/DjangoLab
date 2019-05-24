from django.urls import path, include
from django.conf.urls import url

from . import views as core_views

app_name = 'archive'

urlpatterns = [
    path('', core_views.archive, name='archive'),
    url(r'^(?P<pk>[-\w]+)/$', core_views.get_article.as_view(), name='get_article'),
    path('add', core_views.create_post.as_view(), name='create_post')
]
