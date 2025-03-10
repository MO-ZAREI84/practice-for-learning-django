from django.shortcuts import render
from empApp.models import Employee

def employeedata(request):
    employees = Employee.objects.all()
    myDict = {'employees': employees}
    return render(request, 'empApp/employees.html', context=myDict)
