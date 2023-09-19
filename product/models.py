from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    subtitle = models.TextField(verbose_name='Категории')
    bd_name = models.CharField(max_length=100, verbose_name='Название бд')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
