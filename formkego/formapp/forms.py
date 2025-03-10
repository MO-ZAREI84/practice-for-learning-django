from django import forms

class UserRegistriation(forms.Form):
    FirstName=forms.CharField(max_length=50,required=False)
    LastName = forms.CharField(max_length=50)
    email = forms.EmailField()
    gender=[('m','male'),('f','female')]
    gender = forms.CharField(widget=forms.Select(choices=gender))
    passw = forms.CharField(widget = forms.PasswordInput)