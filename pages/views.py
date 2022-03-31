from django.shortcuts import render

def home(request):
    return render (request, 'pages/home.html')

def about(request):
    return render (request, 'pages/about.html')

def course(request):
    return render (request, 'pages/course.html')

def blog(request):
    return render (request, 'pages/blog.html')

def contact(request):
    return render (request, 'pages/contatc.html')

def login(request):
    return render (request, 'pages/login.html')