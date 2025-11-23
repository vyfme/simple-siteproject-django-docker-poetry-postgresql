from django.contrib import admin

from goods.models import Category, Goods


admin.site.register((Category, Goods))