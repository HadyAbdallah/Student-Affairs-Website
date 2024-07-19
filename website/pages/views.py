from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'pages/home.html')

def HomePage(request):
    return render(request,'pages/Home_page.html') 

def login(request):
    return render(request,'pages/login.html')



def dep(request):
    return render(request,'pages/dep.html')

def search(request):
    return render(request,'pages/search.html')



