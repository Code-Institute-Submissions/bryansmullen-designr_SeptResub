from django.urls import path
from . import views

urlpatterns = [
    path('my-designs', views.my_designs, name='my_designs'),
]
