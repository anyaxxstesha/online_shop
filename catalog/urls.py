from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, product_info

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product_info, name='product_info'),
]
