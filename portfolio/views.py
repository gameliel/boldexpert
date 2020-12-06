from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios':portfolios}
    return render(request, 'portfolio.html', context)

def detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    photos = PortfolioImage.objects.filter(portfolio=portfolio)
    context = {'portfolio':portfolio, 'photos':photos}
    return render(request, 'detail.html', context)