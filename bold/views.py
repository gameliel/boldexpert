from django.shortcuts import render
from posts.models import Post
from portfolio.models import Portfolio

service_url='199.192.23.44'
# Create your views here.


def home(request):
    #line 11 and 12 is to filter latest post, portfolio from DB not more than 4 
    posts = Post.objects.filter(status=1).order_by('-created_on')[:8]
    portfolios = Portfolio.objects.filter(status=1).order_by('-created_on')[:8]
    context = {'posts':posts, 'portfolios':portfolios}
    return render(request, 'pages/home.html', context,)

def expertise(request):
    portfolios = Portfolio.objects.filter(status=1).order_by('-created_on')[:6]
    context = {'portfolios':portfolios}
    return render(request, 'pages/expertise.html', context)

def approach(request):
    portfolios = Portfolio.objects.filter(status=1).order_by('-created_on')[:12]
    context = {'portfolios':portfolios}
    return render(request, 'pages/approach.html', context)

def people(request):
    return render(request, 'pages/people.html')

def publication(request):
    return render(request, 'pages/publication.html')

def contact(request):
    return render(request, 'pages/contact.html')

def contact1(request):
    return render(request, 'pages/contact1.html')

def legal(request):
    return render(request, 'pages/legal.html')
