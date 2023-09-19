from django.shortcuts import render
from loguru import logger

from .models import Stores
from product.models import Products
from sitehandlers.models import Site_handlers
from item_s.models import *


# Create your views here.

def get_pages(page, max_page):
    if page < 8:
        pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "...", max_page - 1, max_page]
    elif page + 7 > max_page:
        pages = [1, 2, "..."]
        for i in range(max_page - 10, max_page + 1):
            pages.append(i)
    else:
        pages = [1, 2, "..."]

        for i in range(page - 3, page + 4):
            pages.append(i)
        pages += ['...', max_page - 1, max_page]
    return pages


def stores(request):
    page = int(request.GET.get('page', 1))
    items = (page - 1) * 16
    kurs = Site_handlers.objects.all().first().kurs

    stores = list(filter(lambda x: request.GET.get('name', '').lower() in x.name.lower(),
                         sorted(Stores.objects.all(), key=lambda x: x.sold, reverse=True)))
    products = Products.objects.all()
    max_page = (len(stores) + 15) // 16
    pages = get_pages(page, max_page)

    data = {'stores': stores[items:items + 16],
            'products': products,
            'kurs': kurs,
            'pages': pages,
            'next_page': page + 1,
            'cur_page': page,
            'prev_page': page - 1,
            'max_page': max_page,
            'min_show': items + 1,
            'max_show': items + 16,
            'max_len': len(stores)}
    logger.debug([s.store_type for s in data['stores']])
    return render(request, './store_temp/stores.html', data)


def store_page(request, store_id):
    kurs = Site_handlers.objects.all().first().kurs
    referer = request.META.get("HTTP_REFERER")
    print('******************')
    print(referer)
    alertShow = False
    
    if referer and ('/products/' in referer):
        alertShow = True

    store = Stores.objects.get(pk=store_id)
    store_items = list(Goods.objects.filter(store_id=store_id))
    data = {'store': store,
            'kurs': kurs, 'store_items': store_items, 'alert_show': alertShow}
    logger.info(data)
    return render(request, './store_temp/store_page.html', data)


def store_work(request, store_id):
    kurs = Site_handlers.objects.all().first().kurs

    store = Stores.objects.get(pk=store_id)
    logger.debug(store.__dict__)
    return render(request, './store_temp/store_work.html', {'store': store,
                                                            'kurs': kurs})


def store_rules(request, store_id):
    kurs = Site_handlers.objects.all().first().kurs

    store = Stores.objects.get(pk=store_id)

    return render(request, './store_temp/store_rules.html', {'store': store,
                                                             'kurs': kurs})


def store_sales(request, store_id):
    products = Products.objects.all()
    store = Stores.objects.filter(pk=store_id).first()
    kurs = Site_handlers.objects.all().first().kurs

    params = {
        'products': products,
        'store': store,
        'kurs': kurs,
    }

    # return JsonResponse({"ping": "pong"})
    return render(request, 'main/top_store/top_store_sales.html', params)


def store_reviews(request, store_id):
    products = Products.objects.all()
    store = Stores.objects.get(pk=store_id)
    kurs = Site_handlers.objects.all().first().kurs
    params = {
        'products': products,
        'store': store,
        'kurs': kurs,
    }

    return render(request, 'main/top_store/top_store_reviews.html', params)
