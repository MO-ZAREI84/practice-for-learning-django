from django.shortcuts import render
from django.http import HttpResponse

def displayQuote(request):
    return HttpResponse("keep calm and lean django")
