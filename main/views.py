from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from . import forms
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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




