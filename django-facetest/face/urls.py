from django.urls import path
from . import views

app_name = 'face'

urlpatterns = [
    path('', views.test, name='test'),
    path('result/', views.show, name='show'),
]