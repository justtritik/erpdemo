from django.urls import path,include
from teacher import views
from django.contrib import admin

urlpatterns = [
    path('login/',views.signin,name='signin'),
    path('login/timetable/',views.timetable,name='timetable'),
    path('login/teachermarks/', views.marks_view, name='marks_view'),
    path('login/teacheratt/', views.att_view, name='att_view')

]
