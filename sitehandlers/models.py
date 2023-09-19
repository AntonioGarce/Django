from django.db import models
# Create your models here.


class SiteHandlers(models.Model):
    kurs = models.FloatField(verbose_name='Курс', blank=True, null=True)
    rek = models.CharField(verbose_name='Реквизиты', max_length=250, blank=True, null=True)
    forum_link1 = models.CharField(verbose_name='Ссылка на форум 1', max_length=150, blank=True, null=True)
    forum_link2 = models.CharField(verbose_name='Ссылка на форум 2', max_length=150, blank=True, null=True)
    forum_link3 = models.CharField(verbose_name='Ссылка на форум 3', max_length=150, blank=True, null=True)
    telegram_bot_link = models.CharField(verbose_name='Telegram', max_length=100, blank=True, null=True)
    lurkchat_bot_link = models.CharField(verbose_name='Lurkchat', max_length=100, blank=True, null=True)
    tor_link = models.CharField(verbose_name='Tor-ссылка', max_length=250, blank=True, null=True)
    canva = models.TextField(verbose_name='Канва на начальном экране')

    def __str__(self):
        return self.kurs

    class Meta:
        verbose_name = 'Хэндлеры сайта'
        verbose_name_plural = 'Хэндлеры сайта'


class Site_handlers(models.Model):
    kurs = models.FloatField(verbose_name='Курс', blank=True, null=True)
    rek = models.CharField(verbose_name='Реквизиты', max_length=250, blank=True, null=True)
    forum_link1 = models.CharField(verbose_name='Ссылка на форум 1', max_length=150, blank=True, null=True)
    forum_link2 = models.CharField(verbose_name='Ссылка на форум 2', max_length=150, blank=True, null=True)
    forum_link3 = models.CharField(verbose_name='Ссылка на форум 3', max_length=150, blank=True, null=True)
    telegram_bot_link = models.CharField(verbose_name='Telegram', max_length=100, blank=True, null=True)
    lurkchat_bot_link = models.CharField(verbose_name='Lurkchat', max_length=100, blank=True, null=True)
    tor_link = models.CharField(verbose_name='Tor-ссылка', max_length=250, blank=True, null=True)
    canva = models.TextField(verbose_name='Канва на начальном экране', blank=True, null=True)

    def __str__(self):
        return str(self.kurs)

    class Meta:
        verbose_name = 'Хэндлеры сайта'
        verbose_name_plural = 'Хэндлеры сайта'
        ordering = ['-id']






