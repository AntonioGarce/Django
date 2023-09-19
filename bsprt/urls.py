from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from stores import views as stores_url
from product import views as products_url
from users import views as auth_url
from account import views as ac_url
from exchangers import views as exc_url
from item_s import views as item_url
from checkout import views as checkout_url
from mainpage import views as mainpage_url

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('captcha/', include('captcha.urls')),
                  path("dynamic-admin-form/", include("dynamic_admin_forms.urls")),
                  path('home', index, name='index'),
                  path('stores', stores_url.stores, name='stores'),
                  path('stores/<int:store_id>', stores_url.store_page, name='store_page'),
                  path('stores/<int:store_id>/work', stores_url.store_work, name='store_work'),
                  path('stores/<int:store_id>/rules', stores_url.store_rules, name='store_rules'),
                  path('stores/<int:store_id>/promotions', stores_url.store_sales, name='store_sales'),
                  path('reviews/<int:cur_order>/store', checkout_url.remain_review, name='remain_review'),
                  path('stores/<int:store_id>/reviews', stores_url.store_reviews, name='store_reviews'),
                  path('products', products_url.products, name='products'),
                  path('register', auth_url.register, name='register'),
                  path('login', auth_url.log_in, name='login'),
                  path('logout', auth_url.log_out, name='logout'),
                  path('', auth_url.first_captcha, name='first_captcha'),
                  path('secure_code', auth_url.secure_code, name='secure_code'),
                  path('choose_city', auth_url.choose_city, name='choose_city'),
                  path('account', ac_url.account, name='account'),
                  path('messages', ac_url.messagess, name='messages'),
                  path('messages/stores/<int:store_id>',ac_url.messages, name='messages_store'),
                  path('dispute', ac_url.dispute, name='dispute'),
                  path('exchanges', ac_url.exchanges, name='exchanges'),
                  path('orders', ac_url.orders, name='orders'),
                  path('favorites', ac_url.favorites, name='favorites'),
                  path('settings', ac_url.settings, name='settings'),
                  path('tickets', ac_url.tickets, name='tickets'),
                  path('sessions', ac_url.sessions, name='sessions'),
                  path('create_ticket', ac_url.create_ticket, name='create_ticket'),
                  path('ticket_window_<int:ticket_id>', ac_url.ticket_window, name='ticket_window'),
                  path('changer', exc_url.changer, name='changer'),
                  path('exchanger_inner_<int:exchanger_id>', exc_url.exchanger_inner, name='exchanger_inner'),
                  path('create_exchange_<int:exchanger_id>_<str:order_num>', exc_url.create_exchange,
                       name='create_exchange'),
                  path('dialog_window_<int:exchanger_id>_<str:order_num>', exc_url.dialog_window, name='dialog_window'),
                  path('diialog_window_<str:order_num>', exc_url.diialog_window, name='diialog_window'),
                  path('contacts', contacts, name='contacts'),
                  path('rules', rules, name='rules'),
                  path('how_create', how_create, name='how_create'),
                  path('payment_info', payment_info, name='payment_info'),
                  path('guarantee', guarantee, name='guarantee'),
                  path('advert', advert, name='advert'),
                  path('agency', agency, name='agency'),
                  path('products/<int:good_id>', item_url.item, name='item'),
                  path('checkout/<int:loc_id>',
                       checkout_url.checkout, name='checkout'),
                  path('order_further_<int:cur_order>', checkout_url.order_further, name='order_further'),
                  path('open_dispute_<int:cur_order>', checkout_url.open_dispute, name='open_dispute'),
                  path('dispute_window_<int:cur_order>_<int:dispute_num>', checkout_url.dispute_window,
                       name='dispute_window'),
                  path('close_dispute_<int:dispute_num>', checkout_url.close_dispute, name='close_dispute'),
                  path('account/deposits/card/create', ac_url.pay, name="pay")
              ] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

