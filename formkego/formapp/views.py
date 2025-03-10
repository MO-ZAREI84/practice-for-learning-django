from django.shortcuts import render
from formapp import forms

def registerf(request):

    Form = forms.UserRegistriation()
    if request.method == 'POST':
        Form=forms.UserRegistriation(request.post)
    return render(request,'login.html',{'form' : Form })
