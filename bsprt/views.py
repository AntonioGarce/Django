from django.http import HttpResponse
from django.shortcuts import render
from loguru import logger

from item_s.models import Goods
from product.models import Products
from sitehandlers.models import Site_handlers
from mainpage.models import *
from stores.models import Stores


def index(request):
    kurs = Site_handlers.objects.all().first().kurs

    top_stores = Stores.objects.filter(is_top=True)
    popular_items = Goods.objects.filter(is_popular=True)
    new_stores = Stores.objects.filter(is_new=True)
    canva = Site_handlers.objects.all().first().canva

    products = Products.objects.all()
    logger.info([i.__dict__ for i in products])
    params = {
        'products': products,
        'kurs': kurs,
        'top_stores': sorted(top_stores, key=lambda x: x.sold, reverse=True),
        'popular_items': popular_items,
        'new_stores': new_stores,
        'canva': canva,
    }
    
    logger.debug([s.store_type for s in top_stores])
    return render(request, './index.html', params)


def contacts(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    return render(request, './junk/actual_contact.html', {'products': products,
                                                            'kurs': kurs})


def rules(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    return render(request, './junk/rules.html', {'products': products,
                                                            'kurs': kurs})


def how_create(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    return render(request, './junk/create_store.html', {'products': products,
                                                            'kurs': kurs})


def payment_info(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    return render(request, './junk/payment.html', {'products': products,
                                                            'kurs': kurs})


def guarantee(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    return render(request, './junk/guarantee.html', {'products': products,
                                                            'kurs': kurs})


def advert(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    return render(request, './junk/advert.html', {'products': products,
                                                            'kurs': kurs})


def agency(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    return render(request, './junk/agency.html', {'products': products,
                                                            'kurs': kurs})









