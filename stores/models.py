from django.db import models

# Create your models here.

store_type_choice = (
    ('Производитель', 'Производитель'),
    ('Оптовик', 'Оптовик'),
    ('Миниопт', 'Миниопт'),
    ('Непроверенный', 'Непроверенный')
)


class Stores(models.Model):
    img = models.ImageField(verbose_name='Обложка', upload_to='topstores_img/')
    name = models.CharField(max_length=100, verbose_name='Название магазина')
    rating = models.FloatField(verbose_name='Рейтинг', blank=True, null=True)
    sold = models.IntegerField(verbose_name='Продано', blank=True, null=True)
    deposit = models.FloatField(verbose_name='Депозит', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    works = models.TextField(verbose_name='Работа', blank=True, null=True)
    rules = models.TextField(verbose_name='Правила магазина', blank=True, null=True)
    sales = models.TextField(verbose_name='Акции', blank=True, null=True)
    forum = models.CharField(verbose_name='Ссылка на форум', blank=True, null=True, max_length=255)
    # category = models.CharField(max_length=200, choices=category_choice, verbose_name='Категория товаров', blank=True,
    #                             null=True)
    store_type = models.CharField(max_length=80, choices=store_type_choice, verbose_name='Категория', blank=True,
                                  null=True)
    telegram_bot = models.URLField(verbose_name='Телеграм-бот', blank=True, null=True)
    cover = models.ImageField(verbose_name='Шапка магазина', upload_to='topstores_img/', blank=True, null=True)
    is_crown = models.BooleanField(verbose_name='Корона', default=False)
    is_top = models.BooleanField(verbose_name='Отображать в топ магазинах', default=False)
    is_new = models.BooleanField(verbose_name='Отображать в топ оптовиках', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
