from django.shortcuts import render
from .forms import *

def NumView(request):
     form = numform()
     if request.method == "POST":
        form = numform(request.POST)
        if form.is_valid:
            return render(request,"result.html",{'form':form})
        else:
            print(form.errors)  # نمایش خطاها در کنسول

     else:
        form = numform()
     return render(request,"result.html",{'form':form})
