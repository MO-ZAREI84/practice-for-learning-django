from django import forms

class AddForm(forms.Form):
    name = forms.CharField(max_length=50)
    quntity = forms.CharField(max_length=50)
