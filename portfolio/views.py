from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.

def Explore(request):
    # this line is to remove the most recents post that is been made and filter the rest
    portfolios = Portfolio.objects.all().order_by("-created_on")[1:]
    # this is to take only the most recent post from DB
    recents = Portfolio.objects.all().order_by("-created_on")[:1]
    categories = Category.objects.all()
    banners = Banner.objects.all()
    context = {'portfolios':portfolios, 'recents':recents, 'categories':categories, 'banners':banners,}
    return render(request, 'portfolio.html', context)

def detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    photos = PortfolioImage.objects.filter(portfolio=portfolio)
    categories = Category.objects.all()
    context = {'portfolio':portfolio, 'photos':photos, 'categories':categories}
    return render(request, 'detail.html', context)


def portfolio_category(request, category):
    recents = Portfolio.objects.filter(category__name__contains=category).order_by('-created_on')[:1]
    categories = Category.objects.all()
    categorybanner = CategoryBanner.objects.all()
    banner = CategoryBanner.objects.all()
    portfolio = Portfolio.objects.filter(
        category__name__contains=category
        ).order_by(
            '-created_on'
        )
    context = {'category':category, 'categories':categories, 'categorybanner':categorybanner, 'portfolio':portfolio, 'recents':recents, 'banner':banner}
    return render(request, 'portfolio_category.html', context)
