from django.shortcuts import render

def login(request):
    loged = False
    if not loged:
        return render(request, 'login/login.html')

def forgot_password_view(request):
    return render(request, "forgot_password/forgot_password.html")

