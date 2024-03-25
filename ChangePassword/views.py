from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def ChangePassword(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        NewPassword = request.POST['NewPassword']
        ReEnterPassword = request.POST['ReEnterPassword']
        user = authenticate(request, username=Email, password=Password)
        if user is not None and NewPassword == ReEnterPassword:
            user.set_password(NewPassword)
            user.save()
            messages.success(request, "Password Changed!")
            return redirect('Login')
        else:
            messages.error(request, "Invalid credentials or passwords don't match.")
    
    return render(request, 'ChangePassword/ChangePassword.html')