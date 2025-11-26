from django.shortcuts import render
from django.http import HttpResponse


from goods.models import Categories

categories = Categories.objects.all()


def index(request):
    return render(request, "shop/index.html", context={'title': 'Главная страница', 'categories': categories})


def about(request):

    return render(request, "shop/about.html", context={'title': 'О сайте', 'categories': categories})


def contact(request):
    return render(request, "shop/contact.html", context={'title': 'Контакты', 'categories': categories})


def basket(request):
    return HttpResponse("basket")