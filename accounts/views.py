from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def register(request):
    if request.method == 'POST':
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password1 == password2: 
           pass
        else:
            messages.error(request,'Senhas nao sao iguais')
        return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return HttpResponse("Logout")

