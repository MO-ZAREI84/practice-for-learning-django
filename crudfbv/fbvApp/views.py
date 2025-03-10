from django.shortcuts import render,redirect
from .models import Students
from .forms import StudentsForm
from django.contrib.auth.decorators import login_required,permission_required

@login_required
def getstudent(request):
    
    students = Students.objects.all()
    return render(request,"fbvApp/index.html",{'students':students})

@login_required
def createstudent(request):
    
    form = StudentsForm()
    if request.method == "POST":
       form = StudentsForm(request.POST)
       if form.is_valid():
         form.save()
         return redirect("/")
    return render(request,"fbvApp/add.html",{'form':form})

@login_required
@permission_required('fbvApp.delete_students', raise_exception=True)
def deletstudent(request,id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect("/")

@login_required
def updatestudent(request,id):
 students =Students.objects.get(id=id)
 if request.method == "POST":
       
       form = StudentsForm(request.POST,instance=students)
       if form.is_valid():
         form.save()
         return redirect("/")
 return render(request,"fbvApp/update.html",{'students':students})

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})
def logout(request):
    return render(request,"fbvApp/logout.html")


