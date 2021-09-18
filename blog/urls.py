from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_entry_list, name='blog_entry_list'),
]
