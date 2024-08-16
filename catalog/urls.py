from django.contrib import admin
from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, HomePageView, ContactsPageView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_edit/<int:pk>/", ProductUpdateView.as_view(), name="product_edit"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
