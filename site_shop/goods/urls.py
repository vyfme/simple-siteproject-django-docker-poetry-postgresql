from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path("catalog/<slug:category_slug>/", views.catalog, name="catalog"),
    path("catalog/<slug:category_slug>/<int:page>/", views.catalog, name="catalog"),
    path("catalog/product/<slug:product_name>/", views.product, name="product")
]