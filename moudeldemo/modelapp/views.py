from django.shortcuts import render
from .models import *

def Student(request):
    information = student.objects.all()
    Dict = {'students':information}
    return render(request,'moudeldemo/student.html',Dict)

