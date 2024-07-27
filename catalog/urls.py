from django.contrib import admin
from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import home, products_list, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("products_list/", products_list, name="products_list"),
    path("catalog/<int:pk>/", product_detail, name="product_detail"),
    path("contacts/", contacts, name="contacts"),
]
