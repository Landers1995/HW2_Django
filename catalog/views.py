from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(requests):
    return render(requests, "home.html")


def products_list(requests):
    products = Product.objects.all()
    context = {'products': products}
    return render(requests, "products_list.html", context)


def product_detail(requests, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(requests, "product_detail.html", context)


def contacts(requests):
    return render(requests, "contacts.html")
