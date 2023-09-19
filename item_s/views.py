from django.shortcuts import render
from product.models import *
from loguru import logger
from users.models import *
from .models import *
from sitehandlers.models import Site_handlers

# Create your views here.
import sys


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def subcategory(request, category, category_name):
    products = Products.objects.all()
    current_product = Products.objects.get(pk=category)
    BD = current_product.bd_name
    logger.info(eval(BD))
    items = eval(BD).objects.filter(category_name=category_name).all()

    kurs = Site_handlers.objects.all().first().kurs

    params = {
        'products': products,
        'kurs': kurs,
        'current_product': current_product,
        'category': category,
        'BD': BD,
        'category_name': category_name,
        'items': items
    }
    return render(request, './subcategory.html', params)


def item(request, good_id):
    user = request.user

    if request.method == 'POST':
        try:
            favorite = Favourite.objects.all().get(item=good_id,user=user)
            favorite.delete()
            is_favorite = False
        except:
            favorite = Favourite()
            favorite.user = user
            favorite.item = good_id
            favorite.save()
            is_favorite = True
    try:
        favorite = Favourite.objects.all().get(item=good_id,user=user)
        is_favorite = True
    except:
        is_favorite = False

    kurs = Site_handlers.objects.all().first().kurs

    products = Products.objects.all()
    good = Goods.objects.get(pk=good_id)
    locs = GoodLocation.objects.filter(good=good)
    params = {
        'category': good_id,
        'BD': good.category,
        'products': products,
        'item': good,
        'kurs': kurs,
        "citys": set([str(i.location.city) for i in locs]),
        'locs': locs,
        'coms': list(Comments.objects.filter(good=good)),
        'isFavorite': is_favorite
    }

    return render(request, './item_temps/item.html', params)
