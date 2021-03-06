from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:id>/', views.detail_view, name="detail"),
    path('cart/', views.cart, name='cart'),
    # path('signin/', views.loginPage, name='signin'),
    # path('signup/', views.register, name='signup'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name="updateitem"),
    path('process_order/', views.processOrder, name="process_order")
]