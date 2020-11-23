from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'pages/home.html')

def expertise(request):
    return render(request, 'pages/expertise.html')

def approach(request):
    return render(request, 'pages/approach.html')

def people(request):
    return render(request, 'pages/people.html')

def publication(request):
    return render(request, 'pages/publication.html')

def contact(request):
    return render(request, 'pages/contact.html')

def contact1(request):
    return render(request, 'pages/contact1.html')