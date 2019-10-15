from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Comments


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
    fields = ['image','caption']   

class CommentForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.fields['comment'].widget=forms.TextInput()
    self.fields['comment'].widget.attrs['placeholder']='Add a comment...'
  class Meta:
    model = Comments
    fields = ('comment',)    