from django.shortcuts import render, redirect
from product.models import Products
from stores.models import Stores
from .handler import generate_number_order
from users.models import Orders, Dispute
from .models import DisputeDialog
from django.contrib import messages
from sitehandlers.models import Site_handlers
from item_s.models import *
from loguru import logger
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
# Create your views here.


def checkout(request, loc_id):
    products = Products.objects.all()
    loc = GoodLocation.objects.get(pk=loc_id)
    logger.info(loc.__dict__)
    item = Goods.objects.get(pk=loc.good.pk)
    kurs = Site_handlers.objects.all().first().kurs
    store_rules = Stores.objects.filter(name=item.store).first().rules
    
    if request.method == 'POST':
        order_num = generate_number_order()
        new_order = Orders(
            user=request.user,
            num_order=order_num,
            item=item.name,
            item_img=item.img.url,
            city=str(loc.location),
            amount=loc.amount,
            price=loc.price / kurs,
            store=item.store,
        )
        new_order.save()
        cur_order_id = Orders.objects.filter(num_order=order_num).first().num_order
        return redirect('order_further', cur_order_id)
    params = {
        'products': products,
        'item': item,
        'store_rules': store_rules,
        'category': item.category,
        'kurs': kurs,
        'city': str(loc.location),
        'loc': loc,
        'amount': loc.amount,
        'price': loc.price,
    }
    return render(request, './checkout/checkout.html', params)


def order_further(request, cur_order):
    print(cur_order)
    products = Products.objects.all()
    order = Orders.objects.filter(num_order=int(cur_order)).first()
    kurs = Site_handlers.objects.all().first().kurs
    good = Goods.objects.filter(name=order.item).first()
    user = request.user
    comment = Comments.objects.filter(good=good, nick_name=user).first()

    if(comment):
        commentExist = True
    else:
        commentExist = False
    if request.method == 'POST':
        if request.POST['action'] == 'Открыть диспут':
            return redirect("open_dispute", cur_order=cur_order)
    rating = 0
    if commentExist:
        rating = comment.raiting
    params = {
        'products': products,
        'order': order,
        'cur_order': cur_order,
        'kurs': kurs,
        'comment': comment,
        'rating': rating,
        'commentExist': commentExist
    }
    print('*****************')
    if(commentExist):
        print(comment.comment_text)
    else:
        print('not exist')

    # print(user)
    # print(order.item_img)
    return render(request, './checkout/order_further.html', params)

def remain_review(request, cur_order):
    order = Orders.objects.filter(num_order=int(cur_order)).first()
    good = Goods.objects.filter(name=order.item).first()
    user = order.user
    
    comment = Comments.objects.filter(good=good, nick_name=user)
    if comment:
        print('comment already exist.')
    else:
        current_time = timezone.now()
        # current_time_integer = int(current_time.timestamp())
        print(order.amount)
        amount = []
        for i in order.amount.split():
            if i.isdigit():
                amount.append(int(i))
        print(amount)
        print('----------------------')
        rating = int(request.POST.get('rating')) * 20
        print(rating)
        new_comment = Comments(
            purchase = amount[0],
            raiting = rating,
            nick_name = user,
            city='',
            data=current_time,
            comment_text = request.POST['message'],
            good = good
        )
        new_comment.save()
    return redirect('order_further', cur_order)    
    # if request.method == 'POST':
    #     if request.POST['action'] == 'Открыть диспут':
    #         return redirect("open_dispute", cur_order=cur_order)
    # params = {
    #     'products': products,
    #     'order': order,
    #     'cur_order': cur_order,
    #     'kurs': kurs,
    # }
    # # # # print(order.item_img)
    # return render(request, './checkout/order_further.html', params)

def open_dispute(request, cur_order):
    products = Products.objects.all()
    curr_order = Orders.objects.filter(num_order=int(cur_order)).first()
    kurs = Site_handlers.objects.all().first().kurs
    if request.method == 'POST':
        dispute_num = generate_number_order()

        new_dispute = Dispute(
            order_num = cur_order,
            dispute_num=dispute_num,
            user_id=request.user.id,
            item=curr_order.item,
            store=curr_order.store,
            answer=False,
            status=True,
        )
        new_dispute.save()
        cur_dispute_id = Dispute.objects.filter(dispute_num=dispute_num).first().id
        return redirect("dispute_window", cur_order, dispute_num)

    params = {
        'products': products,
        'cur_order': cur_order,
        'kurs': kurs,
    }

    return render(request, './checkout/open_dispute.html', params)


def dispute_window(request, cur_order, dispute_num):
    products = Products.objects.all()
    curr_order = Orders.objects.filter(num_order=int(cur_order)).first()
    logger.info(curr_order)
    kurs = Site_handlers.objects.all().first().kurs
    dispute_dialogs = DisputeDialog.objects.filter(user_login=request.user.login, dispute_num=dispute_num).all()
    if request.method == 'POST':

        if request.POST['action'] == 'Закрыть диспут':
            return redirect("close_dispute", dispute_num=dispute_num)

        elif request.POST['action'] == 'Отправить':
            if len(request.POST['message']) > 0:
                new_m = DisputeDialog(
                    user_login=request.user.login,
                    user_text=request.POST['message'],
                    dispute_num=dispute_num,
                    order_num = cur_order
                    )
                new_m.save()
                return redirect('dispute_window', cur_order, dispute_num)
            else:
                messages.error(request, 'Введите сообщение')
    params = {
        'products': products,
        'cur_order': curr_order,
        'dispute_num': dispute_num,
        'dispute_dialogs': dispute_dialogs,
        'kurs': kurs,
        'num': cur_order
    }
    return render(request, './checkout/dispute_window.html', params)


def close_dispute(request, dispute_num):
    products = Products.objects.all()
    kurs = Site_handlers.objects.all().first().kurs
    if request.method == 'POST':
        if request.POST['action'] == 'Закрыть диспут':
            cur_dispute = Dispute.objects.filter(pk=dispute_num).first()
            if cur_dispute:
                cur_dispute.status = False
                cur_dispute.save()
            return redirect('dispute')
    params = {
        'products': products,
        'dispute_num': dispute_num,
        'kurs': kurs

    }
    return render(request, './checkout/close_dispute.html', params)

