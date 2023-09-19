from django.db import models

# Create your models here.
admin_name_ch = [
    ('Модератор', 'Модератор'),
    ('Магазин', 'Магазин')
]


class DisputeDialog(models.Model):
    user_login = models.CharField(verbose_name='Юзер пользователя', max_length=100, null=True, blank=True)
    user_text = models.TextField(verbose_name='Текст пользователя')
    admin_name = models.CharField(max_length=100, choices=admin_name_ch, verbose_name='Кто отвечает юзеру')
    admin_text = models.TextField(verbose_name='Ответ админа')
    date = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True)
    admin_date = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True)
    order_num = models.CharField(max_length=100, verbose_name='Номер', blank=True, null=True)
    dispute_num = models.IntegerField( blank=True, null=True)
    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'Диалоги по поводу диспутов'
        verbose_name_plural = 'Диалоги по поводу диспутов'







