from re import X
from django.shortcuts import render
from .models import Student
# Create your views here.

def StudentUpdate(request):
    if request.method == "GET" :
        id = request.GET['searchID']
        studentInfo = Student.objects.get(ID=id)
    return render(request, 'pages/Update.html',{'Student':studentInfo})

def Delete(request,id):
    student=Student.objects.get(ID=id)
    student.delete()
    return render(request, 'pages/SerchUpdate.html')

def Update(request,id):
    student=Student.objects.get(ID=id)
    student.Name=request.POST.get('Student name')
    student.ID=request.POST.get('Student ID')
    student.GBA=request.POST.get('Student GPA')
    student.Email =request.POST.get('Student Email')
    student.Phone =request.POST.get('Student Mobilenum')
    student.Level =request.POST.get('Level')
    student.DateOfBirth =request.POST.get('birthday')
    student.Gender =request.POST.get('Sex')
    student.Status=request.POST.get('Status')
    student.save()
    return render(request, 'pages/SerchUpdate.html')

def SerchUpdate(request):
    return render(request, 'pages/SerchUpdate.html',)

def add(request):
    if request.method=='POST':
        Name = request.POST.get('Student name')
        ID =request.POST.get('Student ID')
        GPA =request.POST.get('Student GPA')
        Email =request.POST.get('Student Email')
        Phone =request.POST.get('Student Mobilenum')
        Level =request.POST.get('Level')
        Department =request.POST.get('Department')
        DateOfBirth =request.POST.get('birthday')
        Gender =request.POST.get('Sex')
        Status =request.POST.get('Status')

        data = Student(Name=Name ,ID=ID ,GPA=GPA ,Email=Email ,Phone=Phone ,
        Level=Level ,Department=Department ,DateOfBirth=DateOfBirth ,
        Gender=Gender ,Status=Status )
        data.save()

    return render(request,'pages/add.html')


def status(request):
    return render(request,'pages/status.html',{'student':Student.objects.all()})

