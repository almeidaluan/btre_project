from django.shortcuts import render,redirect
from django.http import HttpResponse

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def register(request):
    if request.method == 'POST':
        print('First Name : {} '.format(request.POST['first_name']))
        return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return HttpResponse("Logout")

