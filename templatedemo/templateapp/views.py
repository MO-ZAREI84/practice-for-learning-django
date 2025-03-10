from django.shortcuts import render

def templatesfunction(request):
     mydict = {'firstname':'mostasfs','salary': '13',}
     return render(request,'templateapp/secondapp.html', context= mydict)