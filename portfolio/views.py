from django.shortcuts import render
from .models import PortfolioEntry


def portfolio(request):
    """ Display portfolio page """
    portfolio_entries = PortfolioEntry.objects.all()
    context = {
        'portfolio_entries': portfolio_entries
    }
    return render(request, 'portfolio/portfolio.html', context)
