from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def register(request):
    return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return HttpResponse("Logout")

