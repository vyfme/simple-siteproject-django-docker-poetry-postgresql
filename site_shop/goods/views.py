from django.shortcuts import render

from goods.models import Goods


def catalog(request):
    products = Goods.objects.all()

    return render(request, "goods/catalog.html", {"goods": products})