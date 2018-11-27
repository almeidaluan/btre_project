from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def register(request):
    return HttpResponse("Register")

def login(request):
    return HttpResponse("Login")

def logout(request):
    return HttpResponse("Logout")

