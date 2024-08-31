from django.urls import path, include
from erp import views
from django.contrib import admin

urlpatterns = [
    path('', views.front, name='front'),
]
