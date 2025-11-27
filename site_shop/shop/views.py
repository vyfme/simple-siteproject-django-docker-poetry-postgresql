from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "shop/index.html", context={'title': 'Главная страница'})


def about(request):
    return render(request, "shop/about.html", context={'title': 'О сайте'})


def contact(request):
    return render(request, "shop/contact.html", context={'title': 'Контакты'})


def basket(request):
    return HttpResponse("basket")