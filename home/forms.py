from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,UserChangeForm,PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from .models import Userform
from .models import blogcomment,Blogpost


class pachange(PasswordChangeForm):
    field=['old_password','new_password1','new_password2']
    old_password=forms.CharField(label="Old password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password1=forms.CharField(label="New password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password2=forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control"}))



class Passreset(PasswordResetForm):
    
    email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))

class Passconfirm(SetPasswordForm):
    new_password1=forms.CharField(label='New Password',strip=False ,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password2=forms.CharField(label='Confirm Password',strip=False ,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    

class profilechangeform(UserChangeForm):
    password = None
    class Meta:
        model = Userform
        fields=['username', 'select_type','first_name','last_name', 'institute', 'department', 'Class', 'passout_year','phonenumber' ,'email']
        widgets={'username':forms.TextInput(attrs={"class":"form-control"}),
                 'select_type':forms.Select(attrs={"class":"form-control"}),
                  'first_name':forms.TextInput(attrs={"class":"form-control"}),
                  'last_name':forms.TextInput(attrs={"class":"form-control"}),
                   'email':forms.EmailInput(attrs={"class":"form-control"}),
                   'institute':forms.TextInput(attrs={"class":"form-control"}),
                   'department':forms.Select(attrs={"class":"form-control"}),
                    'Class':forms.Select(attrs={"class":"form-control"}),
                   'passout_year':forms.Select(attrs={"class":"form-control"}),
                   'phonenumber':forms.TextInput(attrs={"class":"form-control"})}

    
        

       


class Signupform(UserCreationForm):
    password1=forms.CharField(label='Enter Password' ,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label='Confirm Password' ,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model = Userform
        fields=['username', 'select_type','first_name','last_name', 'institute', 'department', 'Class', 'passout_year','phonenumber' ,'email']
        widgets={'username':forms.TextInput(attrs={"class":"form-control"}),
                 'select_type':forms.Select(attrs={"class":"form-control"}),
                  'first_name':forms.TextInput(attrs={"class":"form-control"}),
                  'last_name':forms.TextInput(attrs={"class":"form-control"}),
                   'email':forms.EmailInput(attrs={"class":"form-control"}),
                   'institute':forms.TextInput(attrs={"class":"form-control"}),
                   'department':forms.Select(attrs={"class":"form-control"}),
                    'Class':forms.Select(attrs={"class":"form-control"}),
                   'passout_year':forms.Select(attrs={"class":"form-control"}),
                   'phonenumber':forms.TextInput(attrs={"class":"form-control"})}

class loginform(AuthenticationForm):
    field=['username','password']
    username=UsernameField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))