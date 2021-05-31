from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import fields, models, widgets
from django.utils.translation import gettext,gettext_lazy as a_
from .models import Customer
from django.contrib.auth import password_validation


########### registration form #########
class customerregistration(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email',}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}


########### login form #########
class loginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
    attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=("Password"),strip=False,
    widget=forms.PasswordInput(attrs={
    'autocomplete':'current-password','class':'form-control'
    }))
    class Meta:
        model=User


####This is Section for Customer Address form Table###########
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','zipcode','upazila']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control'})}


####This is Section for password change Table###########
class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=('Old Password'),
    strip=False,widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','autofocus':True,
    'class':'form-control'}))
    new_password1=forms.CharField(label=('New Password'),
    strip=False,widget=forms.PasswordInput(attrs=
    {'autocomplete':'new-password','class':'form-control'}),
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2=forms.CharField(label=('Confirm New Password'),
    strip=False,widget=forms.PasswordInput(attrs=
    {'autocomplete':'new-password','class':'form-control'}))
