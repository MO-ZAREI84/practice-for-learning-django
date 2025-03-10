from django.shortcuts import render
from .forms import *

def sessionapi(request):
    count = request.session.get('count',1)
    count += 1
    request.session['count'] = count
    return render (request,"sessionapp/count.html",{'count':count})
def index(request):
    raise Exception("woooooooookkk")
    return render(request,"sessionapp/index.html")
def DisplayItem(request):
    return render(request,"sessionapp/displayItems.html")
def AddItem(request):
    form = AddForm()
    if request.method == 'POST':
        
        if form.is_valid:
            name = request.POST['name']
            quntity = request.POST['quntity']
            request.session[name] = quntity
    return render(request,"sessionapp/addItem.html",{'form':form})