from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_catalog_view, name='product_catalog')
]