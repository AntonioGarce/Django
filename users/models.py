from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    is_admin = models.BooleanField(default=False)
    img = models.ImageField(verbose_name='Аватарка', upload_to='users_img/', blank=True, null=True)
    login = models.CharField(verbose_name='Имя пользователя', max_length=100)
    username = models.CharField(verbose_name='Логин', max_length=100, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=100)
    ref_code = models.CharField(verbose_name='Реф. код', max_length=100)
    secure_code = models.CharField(verbose_name='Код безопасности', max_length=100, blank=True, null=True)
    city = models.CharField(verbose_name='Город', max_length=100, blank=True, null=True)
    btc_amount = models.FloatField(verbose_name='Сумма на счету', default=0.0000, blank=True, null=True)
    agreed = models.BooleanField(verbose_name='Согласие с условиями', null=True)
    captcha = models.CharField(max_length=50, verbose_name='Каптча', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Dialogs(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    user_email = models.EmailField(verbose_name='Почта пользователя', blank=True, null=True)
    thema = models.CharField(verbose_name='Тема', max_length=200, blank=True, null=True)
    store_name = models.CharField(verbose_name='Название магазина', max_length=100, blank=True, null=True)
    action = models.CharField(verbose_name='Действия', max_length=100, blank=True, null=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)

    def __str__(self):
        return self.thema

    class Meta:
        verbose_name = 'Диалоги пользователя'
        verbose_name_plural = 'Диалоги пользователя'


class Orders(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    # good = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    num_order = models.CharField(max_length=100, verbose_name='Номер заказа', blank=True, null=True)
    item = models.CharField(max_length=100, verbose_name='Единица')
    item_img = models.ImageField(verbose_name='Изображение единицы', upload_to='orders_img/')
    amount = models.CharField(max_length=100, verbose_name='Количество')
    city = models.CharField(verbose_name='Город', max_length=100)
    location = models.CharField(verbose_name='Локация', max_length=100)
    price = models.IntegerField(verbose_name='Цена')
    store = models.CharField(verbose_name='Магазин', max_length=50)
    time = models.DateTimeField('%Y-%m-%d %H:%M', auto_now_add=True)
    actions = models.BooleanField(verbose_name='Действия', blank=True, null=True)

    def __str__(self):
        return self.num_order

    class Meta:
        verbose_name = 'Заказы пользователя'
        verbose_name_plural = 'Заказы пользователя'


class Favourite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    item = models.CharField(max_length=250, verbose_name='Товар')

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = 'Любимые товары пользователя'
        verbose_name_plural = 'Любимые товары пользователя'


class Dispute(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    dispute_num = models.CharField(max_length=100, verbose_name='Номер диспута')
    order_num = models.IntegerField(default=-1,blank=False,null=False)
    store = models.CharField(max_length=100, verbose_name='Магазин')
    item = models.CharField(max_length=250, verbose_name='Товар')
    data = models.DateTimeField('%Y-%m-%d %H:%M', auto_now_add=True)
    answer = models.BooleanField(verbose_name='Ответ', default=False)
    status = models.BooleanField(verbose_name='Статус', default=False)

    def __str__(self):
        return self.dispute_num

    class Meta:
        verbose_name = 'Диспуты пользователя'
        verbose_name_plural = 'Диспуты пользователя'


class Ticket(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    tick_order = models.CharField(max_length=100, verbose_name='Номер тикета')
    thema = models.CharField(max_length=100, verbose_name='Тема')
    status = models.BooleanField(verbose_name='Статус')
    data = models.DateTimeField('%Y-%m-%d %H:%M', auto_now_add=True)

    def __str__(self):
        return self.tick_order

    class Meta:
        verbose_name = 'Тикеты пользователя'
        verbose_name_plural = 'Тикеты пользователя'
