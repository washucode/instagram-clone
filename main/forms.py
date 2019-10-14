from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=30,required=False,help_text='Optional.')
    surname = forms.CharField(max_length=30,required=False,help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta :
        model = User
        fields =('username','firstname','surname','email','password1','password2')


class ImageForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['image','name','caption','likes','date']       