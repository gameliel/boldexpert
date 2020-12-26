from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:id>', views.detail, name='detailed'),
    path('<category>/', views.portfolio_category, name='portfolio_category')
]

