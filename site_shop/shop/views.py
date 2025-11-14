from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("index")


def categories(request):
    return HttpResponse("categories")


def basket(request):
    return HttpResponse("basket")