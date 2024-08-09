from django.contrib import admin
from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, HomePageView, ContactsPageView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("products_list/", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
]
