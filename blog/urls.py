from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_entry_list, name='blog_entry_list'),
    path('new/', views.blog_new, name='blog_new'),
    path('<blog_id>/', views.blog_detail, name='blog_detail'),
    path('edit/<blog_id>/', views.blog_edit, name='blog_edit')
]