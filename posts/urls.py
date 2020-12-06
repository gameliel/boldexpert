from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:id>/', views.detail_view, name='post_detail'),
    path('<category>/', views.blog_category, name='blog_category'),
]