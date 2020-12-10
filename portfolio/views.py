from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.

def portfolio(request):
    # this line is to remove the most recents post that is been made and filter the rest
    portfolios = Portfolio.objects.all().order_by("-created_on")[1:]
    # this is to take only the most recent post from DB
    recents = Portfolio.objects.all().order_by("-created_on")[:1]
    context = {'portfolios':portfolios, 'recents':recents}
    return render(request, 'portfolio.html', context)

def detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    photos = PortfolioImage.objects.filter(portfolio=portfolio)
    context = {'portfolio':portfolio, 'photos':photos}
    return render(request, 'detail.html', context)