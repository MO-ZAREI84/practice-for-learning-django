from django.shortcuts import render

from . import forms

def userRegisterationView(request):
    form = forms.UserRegisterationForm()
    
    if request.method == 'POST':
        form = forms.UserRegisterationForm(request.POST)
        if form.is_valid():
            print('form is valid')
            print('first name is: ' , form.cleaned_data['firstName'])
            print('last name is: ' , form.cleaned_data['lastName'])
            print('email is: ' , form.cleaned_data['email'])
        
    
    return render(request, 'formsApp/userRegisteration.html', {'form': form})
