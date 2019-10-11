from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from forms import RegisterForm


def signup(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            input_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=input_password)
            login(request, user)
            return render(request, 'index.html')
    else :
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form':form})
            
