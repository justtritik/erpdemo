from django.urls import path,include
from student import views
from django.contrib import admin

urlpatterns = [
    path('login/',views.signin,name='signin'),
    path('login/timetable/',views.timetable,name='timetable'),
    path('login/studentatt/',views.att_view,name='att_view'),
    #path('login/studentmarks/',views.studentmarks,name='studentmarks')
    path('login/studentmarks/', views.marks_view, name='marks_view')
]

