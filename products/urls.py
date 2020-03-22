from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard.html'),
    path('product/', views.vv_product, name='vv_product.html'),
]