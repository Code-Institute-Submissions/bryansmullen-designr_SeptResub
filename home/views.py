from django.shortcuts import render


def index(request):
    """ Display Index Page """
    return render(request, 'home/index.html')


def about(request):
    """ Display About Page """
    return render(request, 'home/about.html')


def account(request):
    """ Display Account Page """
    return render(request, 'home/account.html')
