from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<p>My first django app</p>")
    
def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Current date and time is: <b>" + str(dt)
    return HttpResponse(s)
