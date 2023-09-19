from django.shortcuts import render, redirect
from product.models import Products
from .forms import UpdatePhotoForm, ChangePasswordForm
from users.models import *
from django.contrib import messages
from .handler import generate_number_order
from .models import TicketDialog
from exchangers.models import ExchangeOrders
from sitehandlers.models import Site_handlers
from loguru import logger
from item_s.models import Goods, Comments

# Create your views here.


def account(request):
    kurs = Site_handlers.objects.all().first().kurs
    user_exc = ExchangeOrders.objects.filter(user=request.user).all()
    products = Products.objects.all()
    return render(request, './account_temps/account.html', {'products': products,
                                                            'user_exc': user_exc,
                                                            'kurs': kurs})


def messagess(request):
    kurs = Site_handlers.objects.all().first().kurs
    user_dialogs = Dialogs.objects.filter(user=request.user).all()
    products = Products.objects.all()
    return render(request, './account_temps/messages.html', {'products': products,
                                                             'user_dialogs': user_dialogs,
                                                             'kurs': kurs})

def messages(request, store_id):
    user = request.user
    comments = Comments.objects.filter(nick_name=user, purchase__gt=2000)
    isAvaiableMessage = False
    for comment in comments:
        if comment.good.store.id == store_id:
            isAvaiableMessage = True
            print(comment)
            break
    if isAvaiableMessage:
        return redirect('messages')
    else:
        return redirect('store_page', store_id)
    

def dispute(request):
    kurs = Site_handlers.objects.all().first().kurs
    user_disputes = Dispute.objects.filter(user=request.user).all()
    products = Products.objects.all()
    return render(request, './account_temps/dispute.html', {'products': products,
                                                            'user_disputes': user_disputes,
                                                            'kurs': kurs})


def pay(request):
    kurs = Site_handlers.objects.all().first().kurs
    user_disputes = Dispute.objects.filter(user=request.user).all()
    products = Products.objects.all()
    return render(request, './account_temps/pay.html', {'products': products,
                                                            'user_disputes': user_disputes,
                                                            'kurs': kurs})

def exchanges(request):
    kurs = Site_handlers.objects.all().first().kurs
    user_exc = ExchangeOrders.objects.filter(user=request.user).all()
    products = Products.objects.all()
    return render(request, './account_temps/exchanges.html', {'products': products,
                                                              'user_exc': user_exc,
                                                              'kurs': kurs})


def orders(request):
    kurs = Site_handlers.objects.all().first().kurs
    user_orders = Orders.objects.filter(user=request.user).all()
    products = Products.objects.all()
    return render(request, './account_temps/orders.html', {'products': products,
                                                           'user_orders': user_orders,
                                                            'kurs': kurs})


def favorites(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    user = request.user
    favorites = Favourite.objects.filter(user=user)
    favorite_products =  []
    for fav in favorites:
        product = Goods.objects.get(pk=fav.item)
        favorite_products.append(product)

    return render(request, './account_temps/favorites.html', { 'favorites':favorite_products, 'products': products, 'kurs': kurs})


def settings(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    photo_form = UpdatePhotoForm()
    password_form = ChangePasswordForm()
    if request.method == 'POST':
        if request.POST['action'] == 'Загрузить аватарку':
            form = UpdatePhotoForm(request.FILES)

            if form.is_valid():
                user = UserProfile.objects.get(username=request.user)
                user.img = form.cleaned_data['img']
                user.save()
                messages.success(request, 'Аватар загружен')

        elif request.POST['action'] == 'Обновить пароль':
            form = ChangePasswordForm(request.POST)

            if form.is_valid():
                user = UserProfile.objects.get(username=request.user)
                if form.cleaned_data('password') == user.password:
                    user.password = form.cleaned_data('new_password')
                    user.save()
                    messages.success(request, 'Пароль успешно изменен.')

                else:
                    messages.error(request, 'Неверный пароль, попробуйте еще.')

        elif request.POST['action'] == 'Обновить город':
            user = UserProfile.objects.get(username=request.user)
            user.city = request.POST['city_id']
            user.save()
            messages.success(request, 'Город успешно изменен.')

    return render(request, './account_temps/settings.html', {'products': products,
                                                             'photo_form': photo_form,
                                                             'password_form': password_form, 'kurs': kurs})


def tickets(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    user_tickets = Ticket.objects.filter(user_id=request.user.id).all()
    return render(request, './account_temps/tickets.html', {'products': products,
                                                            'user_tickets': user_tickets, 'kurs': kurs})


def create_ticket(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        ticket_num = generate_number_order()
        new_ticket = Ticket(
            user=request.user,
            tick_order=ticket_num,
            thema=subject,
            status=False,
        )

        new_ticket.save()
        new_m = TicketDialog(
            ticket_num=ticket_num,
            user_login=request.user.login,
            user_text=message
        )
        new_m.save()
        messages.success(request, 'Тикет успешно создан, ожидайте ответа')
        return redirect('tickets')
    return render(request, './account_temps/create_ticket.html', {'products': products, 'kurs': kurs})


def sessions(request):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    if request.method == 'POST':
        if request.user.password == request.POST['password']:
            return redirect('logout')
    return render(request, './account_temps/sessions.html', {'products': products})


def ticket_window(request, ticket_id):
    kurs = Site_handlers.objects.all().first().kurs
    products = Products.objects.all()
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket_dialogs = TicketDialog.objects.filter(ticket_num=ticket.tick_order).all()
    if request.method == 'POST':
        if request.POST['action'] == 'Закрыть':
            new_m = TicketDialog(
                ticket_num=ticket.tick_order,
                user_login=request.user.login,
                user_text='Тикет закрыт пользователем'
            )
            ticket = Ticket.objects.get(pk=ticket_id)
            ticket.status = True
            new_m.save()
        elif request.POST['action'] == 'Отправить':
            new_m = TicketDialog(
                ticket_num=ticket.tick_order,
                user_login=request.user.login,
                user_text=request.POST['message'])
            new_m.save()
            return redirect('ticket_window', ticket_id)
    return render(request, './account_temps/dialog_window/ticket_window.html', {'products': products,
                                                                                'ticket_dialogs': ticket_dialogs,
                                                                                'ticket': ticket, 'kurs': kurs})



