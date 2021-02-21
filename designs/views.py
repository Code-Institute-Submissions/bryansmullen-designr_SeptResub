from django.shortcuts import render


def my_designs(request):
    return render(request, 'designs/my_designs.html')
