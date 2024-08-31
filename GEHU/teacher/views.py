
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from student.models import DetailsModel
from django.shortcuts import get_object_or_404
from student.forms import StudentDetailsForm


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None and user.groups.filter(name='teacher').exists():
            login(request, user)
            fname = user.username
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "teacher.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/teacher/login')
    
    return render(request, "teacherlogin.html")

def timetable(request):
    return render(request, "timetable.html")

def marks_view(request):
    students = DetailsModel.objects.all()
    return render(request, 'teachers_template.html', {'students': students})

def att_view(request):
    return render(request,'syllabus.html')






