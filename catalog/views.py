from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class HomePageView(TemplateView):
    template_name = "catalog/home.html"


# def home(requests):
#     return render(requests, "catalog/home.html")


class ProductListView(ListView):
    model = Product

# def products_list(requests):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(requests, "product_list.html", context)


class ProductDetailView(DetailView):
    model = Product


# def product_detail(requests, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(requests, "product_detail.html", context)


class ContactsPageView(TemplateView):
    template_name = "catalog/contacts.html"


# def contacts(requests):
#     return render(requests, "catalog/contacts.html")
