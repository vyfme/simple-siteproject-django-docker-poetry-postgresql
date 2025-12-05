from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path("search/", views.catalog, name="search"),
    path("<slug:category_slug>/", views.catalog, name="catalog"),
    path("<slug:category_slug>/<int:page>/", views.catalog, name="catalog"),
    path("product/<slug:product_name>/", views.product, name="product")
]