from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contact, get_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contact, name='contact'),
    path('product/<pk>/', get_product),
]
