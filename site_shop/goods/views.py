from django.shortcuts import render

from goods.models import Goods


def catalog(request, category_slug):
    products = Goods.objects.filter(category__slug=category_slug)

    return render(request, "goods/catalog.html", {"goods": products})


def product(request, product_id):
    product = Goods.objects.get(id=product_id)

    return render(request, "goods/product.html", {"product": product})