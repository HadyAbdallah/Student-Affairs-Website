from django.db import models

# Create your models here.

class Student(models.Model):
    x=[('First Level','First Level'),('Second Level','Second Level'),
    ('Third Level','Third Level'),('Fourth Level','Fourth Level')]
    y=[('General','General'),('Computer Science','Computer Science'),
    ('Information System','Information System'),('Artificial Intelligence','Artificial Intelligence')
    ,('Information Technology','Information Technology')
    ,('Decision Support','Decision Support')]
    Name=models.CharField(max_length=50)
    ID=models.CharField(max_length=8,primary_key=True)
    GPA=models.DecimalField(max_digits=4, decimal_places=3)
    Email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=11)
    Level=models.CharField(max_length=12, choices=x)
    Department=models.CharField(max_length=30, choices=y)
    DateOfBirth=models.CharField(max_length=30)
    Gender=models.CharField(max_length=20,choices=[('Male','Male'),('Female','Female')])
    Status=models.CharField(max_length=20,choices=[('Active','Active'),('Inactive','Inactive')])

    def __str__(self) :
        return self.ID