from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator

from goods.models import Goods


def catalog(request, category_slug):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'vse-tovary':
        products = Goods.objects.all()
    else:
        products = get_list_or_404(Goods.objects.filter(category__slug=category_slug))
        
    if on_sale:
        products = products.filter(discount__gt=0)
        
    if order_by and order_by != 'default':
        products = products.order_by(order_by)

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    return render(request, "goods/catalog.html", {"goods": current_page, "slug_url": category_slug})


def product(request, product_name):
    product = Goods.objects.get(slug=product_name)

    return render(request, "goods/product.html", {"product": product})