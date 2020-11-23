from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('expertise/', views.expertise, name="expertise"),
    path('approach/', views.approach, name="approach"),
    path('people/', views.people, name="people"),
    path('publication/', views.publication, name="publication"),
    path('contact/', views.contact, name="contact"),
    path('contact1/', views.contact1, name="contact1")
]

