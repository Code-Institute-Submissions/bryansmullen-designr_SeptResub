from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.blog_new, name='blog_new'),
    path('edit/<blog_id>/', views.blog_edit, name='blog_edit'),
    path('delete/<blog_id>/', views.blog_delete, name='blog_delete'),
    path('<blog_id>/', views.blog_detail, name='blog_detail'),
    path('', views.blog_entry_list, name='blog_entry_list'),
]
