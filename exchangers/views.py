from django.shortcuts import render, redirect
from product.models import Products
from .models import *
from .handler import generate_order_num
from django.contrib import messages
from sitehandlers.models import Site_handlers


# Create your views here.


def changer(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    list_of_exchangers = ExchangerList.objects.all()
    return render(request, './exchanger_temps/changer.html', {'products': products,
                                                              'list_of_exchangers': list_of_exchangers, 'kurs': kurs})


def exchanger_inner(request, exchanger_id):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    current_exchanger = ExchangerList.objects.get(pk=exchanger_id)

    if request.method == 'POST':
        try:
            method = request.POST['method']
            amount = request.POST['amount']
            order_num = generate_order_num()
            new_order = ExchangeOrders(
                user_id=request.user.id,
                number=order_num,
                name=current_exchanger.name,
                user_login=request.user.username,
                method=method,
                amount=amount,
            )
            new_order.save()
            return redirect('create_exchange', exchanger_id, order_num)
        except ValueError:
            messages.success(request, 'The amount field is required.')

    reviews = list(Review.objects.filter(exchanger=current_exchanger))
    return render(request, './exchanger_temps/exchanger_inner.html', {'products': products,
                                                                      'current_exchanger': current_exchanger,
                                                                      'kurs': kurs,
                                                                      'description': current_exchanger.description.replace(
                                                                          "\n", '<br>'),
                                                                      "reviews": reviews,
                                                                      "methods": current_exchanger.method.split(", ")})


def create_exchange(request, exchanger_id, order_num):
    products = Products.objects.all()
    kurs = Site_handlers.objects.all().first().kurs
    current_exchanger = ExchangerList.objects.get(pk=exchanger_id)
    cur_order = ExchangeOrders.objects.filter(number=order_num).first()
    comission = current_exchanger.commission
    cur_order.amount_in_BTC = round(cur_order.amount / kurs, 5)
    COMISSION = (cur_order.amount * comission) / 100
    cur_order.total = cur_order.amount + ((cur_order.amount * comission) / 100)
    cur_order.save()
    cur_order = ExchangeOrders.objects.filter(number=order_num).first()

    if request.method == 'POST':
        text = f"""
                        Создана новая заявка на пополнение.
                        ID: {cur_order.number}
                        Cумма к переводу: {cur_order.total} руб.
                        Будет зачислено: {cur_order.amount} руб. / ~{cur_order.amount_in_BTC}BTC

                        Дождитесь реквизитов от оператора
                        """
        new_dialog = DialogWithOperator(
            user_login=request.user.login,
            user_text=text,
            order_num=order_num
        )
        new_dialog.save()
        # send_message(blah, blah)
        return redirect('dialog_window', exchanger_id, order_num)

    params = {
        'products': products,
        'COMISSION': COMISSION,
        'current_exchanger': current_exchanger,
        'cur_order': cur_order,
        'exchanger_id': exchanger_id,
        'order_num': order_num,
        'kurs': kurs
    }
    return render(request, './exchanger_temps/create_exchange.html', params)


def dialog_window(request, exchanger_id, order_num):
    products = Products.objects.all()
    current_exchanger = ExchangerList.objects.get(pk=exchanger_id)
    cur_dialog = DialogWithOperator.objects.filter(user_login=request.user.login, order_num=order_num).all()
    kurs = Site_handlers.objects.all().first().kurs

    if request.method == 'POST':
        if request.POST['action'] == 'Отправить':
            if len(request.POST['message']) > 0:
                new_m = DialogWithOperator(
                    user_login=request.user.login,
                    user_text=request.POST['message'],
                    order_num=order_num
                )
                new_m.save()
                return redirect('dialog_window', exchanger_id, order_num)

            else:
                messages.error(request, 'Введите сообщение')

        if request.POST['action'] == 'Отменить':
            current_exchanger.isAvailable = False
            current_exchanger.save()
            new_m = DialogWithOperator(
                user_login=request.user.login,
                user_text='Заявка закрыта пользователем',
                order_num=order_num,
            )
            new_m.save()
            messages.error(request, 'Заявка отменена')
            return redirect('dialog_window', exchanger_id, order_num)

    params = {
        'products': products,
        'exchanger_id': exchanger_id,
        'current_exchanger': current_exchanger,
        'cur_dialog': cur_dialog,
        'order_num': order_num,
        'kurs': kurs
    }

    return render(request, './exchanger_temps/dialog_winndow.html', params)


def diialog_window(request, order_num):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    cur_order = ExchangeOrders.objects.filter(number=order_num).first()
    current_exchanger = ExchangerList.objects.get(name=cur_order.name)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        # post = dict(request.POST)
        # print(request.get('action'))
        if action == 'Отправить':
            if len(request.POST['message']) > 0:
                new_m = DialogWithOperator(
                    user_login=request.user.login,
                    user_text=request.POST['message'],
                    order_num=order_num
                )
                new_m.save()
                return redirect('diialog_window', order_num)

            else:
                messages.error(request, 'Введите сообщение')

        if action == 'Отменить':
            current_exchanger.isAvailable = False
            current_exchanger.save()
            new_m = DialogWithOperator(
                user_login=request.user.login,
                user_text='Заявка закрыта пользователем',
                order_num=order_num
            )
            new_m.save()
            messages.error(request, 'Заявка отменена')
            return redirect('diialog_window', order_num)
    cur_dialog = DialogWithOperator.objects.filter(user_login=request.user.login, order_num=order_num).all()
    params = {
        'products': products,
        'current_exchanger': current_exchanger,
        'cur_dialog': cur_dialog,
        'order_num': order_num,
        'kurs': kurs
    }
    return render(request, './exchanger_temps/diialog_window.html', params)
