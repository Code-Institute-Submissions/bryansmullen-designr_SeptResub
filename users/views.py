from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        # pull data from request
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check passwords match
        if password == password2:
            # check user model
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name, password=password)
                print(user)
                # login user
                auth.login(request, user)
                return redirect('account')
        else:
            messages.error(request, 'Passwords do not match')
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
