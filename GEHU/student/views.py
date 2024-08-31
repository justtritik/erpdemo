
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.models import DetailsModel



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None and user.groups.filter(name='student').exists():
            login(request, user)
            fname = user.username
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "student.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/student/login')
    
    return render(request, "studentlogin.html")

def timetable(request):
    return render(request, "timetable.html")

def studentatt(request):
    return render(request, "studentatt.html")

def studentmarks(request):
    return render(request, "studentmarks.html")

def marks_view(request):
    details = DetailsModel.objects.get(user=request.user)
    return render(request, 'studentmarks.html', {'details': details})

def att_view(request):
    details = DetailsModel.objects.get(user=request.user)
    return render(request, 'studentatt.html', {'details': details})



