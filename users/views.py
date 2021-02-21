from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        messages.error(request, 'POST register')
        return redirect('register')
    else:
        return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        messages.error(request, 'POST login')
        return redirect('login')
    else:
        return render(request, 'users/login.html')


def logout(request):
    return redirect('index')


def account(request):
    return render(request, 'users/account.html')
