from django.db import models
from .category_name_choices import *
from stores.models import Stores
# from users.models import UserProfile

category_choice = (('apteka', 'Аптека'),
                   ('dissociatives', 'Диссоциативы'),
                   ('Marijuana', 'Марихуана'),
                   ('Opiates', 'Опиаты'),
                   ('Psychedelics', 'Психоделики'),
                   ('Stimulants', 'Стимуляторы'),
                   ('Chemical', 'Химические реактивы/Конструкторы'),
                   ('Ecstasy', 'Экстази'),
                   ('Entheogens', 'Энтеогены'),
                   ('Euphoretics', 'Эйфоретики'),
                   ('Mixtures', 'Основа курительных смесей'),
                   ('Other', 'Другoе'),
                   ('Work', 'Работа'),
                   ('Medicine', 'Медицина'),
                   ('Advert', 'Реклама'),
                   ('Earn', 'Способы заработка'),
                   ('Fake', 'Фальшивые деньги'),
                   ('Cannabinoids', 'Каннабинойды'),
                   ('Grove', 'Товары для грова'),
                   )


class City(models.Model):
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.city


class Location(models.Model):
    name = models.CharField(max_length=80)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.city.city}: {self.name}"


class Goods(models.Model):
    img = models.ImageField(verbose_name='Обложка', upload_to='goods_img/', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    min_price = models.FloatField(verbose_name='Минимальная цена', blank=False, null=False)
    rating = models.FloatField(verbose_name='Рейтинг', blank=False, null=False)
    store = models.ForeignKey(Stores, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Магазин')
    category = models.CharField(max_length=200, choices=category_choice, verbose_name='Категория товаров', blank=True,
                                null=True)
    is_popular = models.BooleanField(verbose_name="Отображать в популярных товарах?")

    def __str__(self):
        return f"({self.category}) {self.name}"

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Comments(models.Model):
    purchase = models.IntegerField(null=True)
    raiting = models.IntegerField(null=True)
    nick_name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    data = models.CharField(max_length=255,null=True)
    comment_text = models.TextField(null=True)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    # user = models.Field(UserProfile,  null=True, blank=True)


class GoodLocation(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(verbose_name='Тип', choices=type_choices, null=True, blank=True, max_length=50)
    price = models.FloatField(verbose_name='Цена', null=True, blank=True)
    amount = models.FloatField(verbose_name='Кол-во', null=True, blank=True)
