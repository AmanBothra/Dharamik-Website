from django.shortcuts import render

# Create your views here.

def course(request):
    return render (request, 'pages/course.html')