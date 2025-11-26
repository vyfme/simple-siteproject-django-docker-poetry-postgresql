from django.shortcuts import render

from goods.models import Goods


def catalog(request):
    products = Goods.objects.all()
    context = {"data": [
        {
        "name": "Эко-кружка BambooCup",
        "description": "Многоразовая кружка из бамбукового волокна, лёгкая и прочная.",
        "price": "590 ₽"
        },
        {
        "name": "Смарт-лампа Lumina",
        "description": "Умная LED-лампа с регулировкой яркости и цвета через приложение.",
        "price": "1 290 ₽"
        },
        {
        "name": "Наушники AeroSound Lite",
        "description": "Беспроводные наушники с шумоподавлением и автономностью до 20 часов.",
        "price": "3 490 ₽"
        },
        {
        "name": "Термобутылка FrostKeep",
        "description": "Стальная бутылка, сохраняющая температуру напитков до 12 часов.",
        "price": "890 ₽"
        },
        {
        "name": "Блокнот SoftNote A5",
        "description": "Стильный блокнот в мягкой обложке, 120 страниц.",
        "price": "350 ₽"
        },
        {
        "name": "Фитнес-браслет FitTrack Mini",
        "description": "Отслеживает шаги, пульс и сон, защита IP67.",
        "price": "1 990 ₽"
        },
        {
        "name": "Портативная колонка BeatBox Go",
        "description": "Компактная Bluetooth-колонка с глубоким басом.",
        "price": "2 490 ₽"
        },
        {
        "name": "Аромасвеча Cozy Home",
        "description": "Натуральный соевый воск, аромат ванили и корицы.",
        "price": "450 ₽"
        },
        {
        "name": "Рюкзак UrbanPack 20L",
        "description": "Городской рюкзак с отделением для ноутбука 15.",
        "price": "2 790 ₽"
        },
        {
        "name": "Игровая мышь Falcon Pro",
        "description": "RGB-подсветка, настраиваемые кнопки, сенсор 12 000 DPI.",
        "price": "1 590 ₽"
        },
        {
        "name": "Плед FluffyWarm",
        "description": "Мягкий флисовый плед 150×200 см, не электризуется.",
        "price": "740 ₽"
        },
        {
        "name": "Кухонный набор ChefEasy",
        "description": "Комплект из 5 ножей из нержавеющей стали с подставкой.",
        "price": "1 850 ₽"
        }
    ]
    }

    return render(request, "goods/catalog.html", {"goods": products})