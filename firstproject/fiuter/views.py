from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("hooo")
def displaydatetime (request):
    dt = datetime.datetime.now()
    s = "your time is" + str(dt)
    return HttpResponse(s)