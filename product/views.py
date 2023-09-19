from pprint import pprint

from django.shortcuts import render

from stores.views import get_pages
from .models import Products
from sitehandlers.models import Site_handlers
from item_s.models import *
from users.models import Favourite
from loguru import logger


# Create your views here.


def products(request):
    kwargs = dict(request.GET)
    logger.info(kwargs)
    page = int(request.GET.get('page', 1))
    items = (page - 1) * 10
    kurs = Site_handlers.objects.all().first().kurs
    all_items = list(Goods.objects.all())
    max_page = (len(all_items) + 15) // 16
    pages = get_pages(page, max_page)

    products = Products.objects.all()
    if kwargs.get("subcategory") and kwargs.get("subcategory")[0]:
        try:
            category = Products.objects.get(pk=int(kwargs.get("subcategory")[0]))
            all_items = list(filter(lambda x: x.category in category.subtitle, all_items))
        except:
            pass
    data = []
    for item in all_items[items:items + 10]:
        info = {"obj": item}
        locs = list(GoodLocation.objects.filter(good=item))
        info["mass"] = min(locs, key=lambda x: x.amount).amount
        info["commets"] = len(list(Comments.objects.filter(good=item)))
        info["cities"] = ",".join(set(str(i.location.city) for i in locs))
        info["decription"] = (item.description[:325] + ("..." if len(item.description) > 325 else "")).replace("<br>",
                                                                                                               "")
        if len(info["cities"]) > 50:
            info["cities"] = info["cities"][:50] + "..."
        data.append(info)
        pprint(data)
    return render(request, './products.html', {'kurs': kurs,
                                               'all_items': data,
                                               "products": products,
                                               'pages': pages,
                                               'next_page': page + 1,
                                               'cur_page': page,
                                               'prev_page': page - 1,
                                               'max_page': max_page,
                                               'min_show': items + 1,
                                               'max_show': items + 10,
                                               'max_len': len(all_items)
                                               })


def item_from_products(request, item_id):
    kurs = Site_handlers.objects.all().first().kurs
    all_items = []
    products = Products.objects.all()

    for i in products:
        for j in eval(i.bd_name).objects.all():
            all_items.append(j)

    col = 1
    global item
    for i in all_items:
        if col == item_id:
            item = i
        col += 1

    kwargs = {
        '{0}'.format(item.__class__.__name__): item.id,
    }

    location = (GoodLocation.objects.filter(**kwargs).all())
    cities_ar = []
    amount_ar = []
    price_ar = []

    for i in location:
        cities_ar.append('{}'.format(i.city))
        price_ar.append(i.price)
        amount_ar.append(i.amount)
        logger.info(i.city)
    logger.info(location)
    loc_ar = []
    for i in location:

        b = ("{}".format(i))
        b = b.replace('(', '')
        b = b.replace(')', '')
        loc = b.split(', ')
        c = []
        for i in loc:
            c.append(i)
        loc_ar.append(c)

    logger.info(loc_ar)

    lib = {}
    for i in range(len(cities_ar)):
        lib[cities_ar[i]] = loc_ar[i]

    for i, k in lib.items():
        for j in k:
            print(i, ' -- ', j)

    am_price_lib = {}
    for i in range(len(amount_ar)):
        am_price_lib[amount_ar[i]] = int(price_ar[i])

    if request.method == 'POST':
        new_fav = Favourite(
            user_id=request.user.id,
            item=item.name
        )
        new_fav.save()
    params = {
        'products': products,
        'item': item,
        'kurs': kurs,
        'am_price_lib': am_price_lib,
        'lib': lib,

    }
    return render(request, './item_from_products.html', params)
