from django import forms

def validate_env(value):
    if value%2 ==0:
        raise forms.ValidationError("is a zoj ")
    
       
class numform(forms.Form):
    num = forms.IntegerField(validators=[validate_env])