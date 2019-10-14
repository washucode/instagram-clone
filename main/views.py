from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    CreateView,
    UpdateView,
)
from . import forms
from .forms import RegisterForm , ImageForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Image


def signup(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            input_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=input_password)
            login(request, user)
            messages.success(request, f'Account created for {username}')
            return redirect('home')
        

    else :
        form = RegisterForm()
    return render(request, 'auth/signup.html', {'form':form})

@login_required
def home(request):
    
    return render(request, 'index.html')


@login_required
def profile(request):
  current_user = request.user
 
  images = Image.objects.filter(uploader_profile_id = current_user.id)
  post =images.count()
  print ('---',post)
  return render(request,'profile.html',{"images":images, "post":post})

class createimage(LoginRequiredMixin, CreateView):
    
    model = Image
    fields =['image','caption'] 

    def form_valid(self,form):
        form.instance.uploader_profile = self.request.user
        return super().form_valid(form)

@login_required
def comments(request,image_id):
  Comment_form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    Comment_form = CommentForm(request.POST)
    if Comments_form.is_valid():
      comment = Comment_form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('index')


