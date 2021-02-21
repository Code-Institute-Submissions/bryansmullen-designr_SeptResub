from django.shortcuts import render


def services(request):
    return render(request, 'services/services.html')


def service(request, service_id):
    return render(request, 'services/service.html')
