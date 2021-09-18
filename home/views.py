from django.shortcuts import render


def index(request):
    print(request.session.get("cart", {}))
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def account(request):
    return render(request, 'home/account.html')