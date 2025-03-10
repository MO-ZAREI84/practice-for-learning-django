from django.shortcuts import render
from .models import project
from .forms import projectform

def index(request):
    return render(request, "index.html")

def listproject(request):
    FormShow = project.objects.all()
    return render(request,"list.html",{'forms':FormShow})

def addProject(request):   
    form = projectform()
   
    if request.method == "POST":
        form = projectform(request.POST)
    if form.is_valid():
        form.save()
        return index(request)

    return render(request,"add.html",{'form':form})

