from django.db import models
from users.models import UserProfile


# Create your models here.


class ExchangerList(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    directions = models.CharField(max_length=100, verbose_name='Направления')
    deposit = models.FloatField(verbose_name='Депозит')
    commission = models.FloatField(verbose_name='Комиссия')
    method = models.CharField(max_length=250, verbose_name='Методы')
    description = models.TextField(verbose_name='Описание')
    rules = models.TextField(verbose_name='Правила')
    isAvailable = models.BooleanField(default=True,blank=False,null=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обменник'
        verbose_name_plural = 'Обменники'


class Review(models.Model):
    nick = models.CharField(max_length=150, verbose_name='ник')
    date = models.CharField(max_length=150, verbose_name='дата')
    text = models.TextField(verbose_name='текст')
    buys = models.IntegerField(verbose_name='покупок')
    is_from_admin = models.BooleanField(verbose_name='от админа?')
    exchanger = models.ForeignKey(ExchangerList, on_delete=models.CASCADE, verbose_name='Обменник', blank=True, null=True)


class ExchangeOrders(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    number = models.CharField(max_length=100, verbose_name='Номер', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Название обменника', blank=True, null=True)
    method = models.CharField(max_length=100, verbose_name='Метод', blank=True, null=True)
    user_login = models.CharField(max_length=100, verbose_name='Логин юзера', blank=True, null=True)
    rek = models.BooleanField(verbose_name='Статус', default=False)
    amount = models.IntegerField(verbose_name='Размер', blank=True, null=True)
    amount_in_BTC = models.FloatField(verbose_name='Размер в BTC', blank=True, null=True)
    total = models.IntegerField(verbose_name='Тотал', blank=True, null=True)
    comission = models.IntegerField(verbose_name='Комиссия', blank=True, null=True)
    date = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True)
    committed = models.BooleanField(verbose_name='Действия', default=False)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Обмены пользователя'
        verbose_name_plural = 'Обмены пользователя'


admin_name_ch = [
    ('Модератор', 'Модератор'),
    ('Обменник', 'Обменник')
]


class DialogWithOperator(models.Model):
    user_login = models.CharField(verbose_name='Юзер пользователя', max_length=100, null=True, blank=True)
    user_text = models.TextField(verbose_name='Текст пользователя')
    admin_name = models.CharField(max_length=100, choices=admin_name_ch, verbose_name='Кто отвечает юзеру')
    admin_text = models.TextField(verbose_name='Ответ админа')
    date = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True)
    admin_date = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True)
    order_num = models.CharField(max_length=100, verbose_name='Номер', blank=True, null=True)

    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'Диалог по поводу обмена'
        verbose_name_plural = 'Диалоги по поводу обменна'
