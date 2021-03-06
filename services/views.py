from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Service


@login_required(login_url='/accounts/login')
def services(request):
    """ Display services """
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services/services.html', context)
