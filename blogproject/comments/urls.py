"""
    date:       2020/8/17 2:14 下午
    written by: neonleexiang
"""
from django.urls import path
from .views import comment

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', comment, name='comment'),
]
