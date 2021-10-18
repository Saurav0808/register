from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")


def loginUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('psw')

        user = authenticate(request,username=name, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, ' User found!')
            return redirect('index')
        else:
            messages.error(request, ' User not found!')
            return redirect('login')
    return render(request,"login.html")

def first(request):
    if request.user.is_anonymous:
        messages.success(request,"You must Log in First!")
        return redirect('login')

    return render(request, "first.html")
