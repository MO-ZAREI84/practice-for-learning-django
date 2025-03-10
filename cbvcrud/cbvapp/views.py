from django.shortcuts import render
from .models import Students
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class StudentsShow(ListView):
    model = Students
    template_name = 'students_list.html'
    # default pass the template_name : model_lis.html
    #  default pass the context_object_name : model_list
    #  ok if you want to change this  block you should say this sentences to change them
class students_detail(DetailView):
    model = Students
    template_name = 'student_detail.html'
    context_object_name = "student"
    # default pass the template_name : model_lis.html
    #  default pass the context_object_name : model_list
    #  ok if you want to change this  block you should say this sentences to change them
class student_create(CreateView):
    model = Students
    fields = ['firstname','lastname','score']
    template_name = "students_form.html"
class student_update(UpdateView):
    model = Students
    fields = ['score']
    template_name = "students_form.html"
class student_delete(DeleteView):
    model = Students
    success_url = reverse_lazy("student")
    template_name = "students_confirm.html"

    