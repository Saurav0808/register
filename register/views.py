from django.shortcuts import render, HttpResponse
from register.models import Register_model
from django.contrib import messages

# Create your views here.
def registerU(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        password = request.POST.get('psw')
        password2 = request.POST.get('pswrepeat')
        if password == password2:
            Register = Register_model(Email=Email,Password=password,Password2=password2)
            Register.save()
            messages.success(request, "Saved")
        else:
            messages.error(request,"Please enter password correctly!")

    return render(request,"register.html")