from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.models import
from . models import Profile
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    
    # widgets = {
    #         'username':forms.TextInput(attrs={'class':'form-control'}),
    #         'password': forms.PasswordInput(attrs={'class':'form-control'}),
    # }

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    
    
    
    
    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("This username is taken")
        return self.cleaned_data['username']

    def validate_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)

        except ValidationError as e:
            print("bad email, details:", e)
        else:
            print("good email")
            
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Your passwords donot match")

    def validate_password(self):
        password = self.cleaned_data['password']
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match_re = re.compile(reg)
        res = re.search(match_re, password)
        if res:
            pass
        else:
             raise forms.ValidationError("Your passwords is not in rule")
            

        
class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','contact','bio']