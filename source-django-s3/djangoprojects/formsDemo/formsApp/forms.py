from django import forms
from django.core import validators

class UserRegisterationForm(forms.Form):
    firstName = forms.CharField(validators=[validators.MinLengthValidator(5) , validators.MaxLengthValidator(10)])
    lastName = forms.CharField(max_length=20)
    email = forms.CharField()

    GENDER = [ ('male', 'MALE'),('female', 'FEMALE') ]
    gender = forms.CharField( widget=forms.Select(choices=GENDER) )
    password = forms.CharField( widget=forms.PasswordInput )

    
    '''
    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError("the max length can not be more than 20 characters")
        return inputFirstName

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find("@")==-1  :
            raise forms.ValidationError("the email format is not correct")
        return inputEmail
    '''
    
    '''
    def clean(self):
        user_cleaned_data=super().clean()
        
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError("the max length can not be more than 20 characters")
        

        
        inputEmail = user_cleaned_data['email']
        if inputEmail.find("@")==-1  :
            raise forms.ValidationError("the email format is not correct")
    
            
            
        return user_cleaned_data
    '''
    def clean(self):
        user_cleaned_data=super().clean()
        
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName) > 20:
            raise forms.ValidationError("the max length can not be more than 20 characters")
        

        
        inputEmail = user_cleaned_data['email']
        if inputEmail.find("@")==-1  :
            raise forms.ValidationError("the email format is not correct")
    
            
            
        return user_cleaned_data

        