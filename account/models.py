from django.db import models

# Create your models here.


class TicketDialog(models.Model):
    ticket_num = models.CharField(max_length=50, verbose_name='Номер тикета')
    user_login = models.CharField(max_length=50, verbose_name='Логин юзера')
    user_text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True)
    admin_text = models.TextField(verbose_name='Ответ модератора', blank=True, null=True)
    admin_date = models.DateTimeField('%Y-%m-%d %H:%M:%S', auto_now_add=True)

    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'Диалоги по тикетам'
        verbose_name_plural = 'Диалоги по тикетам'


