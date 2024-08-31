from django.shortcuts import render , HttpResponse , redirect



# Create your views here.
def front(request):
    return render(request,'front.html')