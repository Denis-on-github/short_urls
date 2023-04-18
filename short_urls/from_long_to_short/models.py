from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars

class ShortURLs(models.Model):
    full_url = models.URLField(unique=True, verbose_name='Full URL')
    subpart = models.CharField(max_length=settings.LEN_SHORTS, unique=True, db_index=True, blank=True, verbose_name='Subpart')
    short_url = models.CharField(max_length=100, unique=True, db_index=True, blank=True, verbose_name='Short URL')
    request_count = models.IntegerField(default=0, verbose_name='Clicks')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    user = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name='User IP')

    class Meta:
        verbose_name = 'Short URL' # для админки
        verbose_name_plural = 'Short URLs' # для админки
        ordering = ('-created_date',) # сортировка по дате и времени добавления

    def __str__(self):
        return self.full_url
        #return f'{self.short_url} -> {self.full_url}'

    def url(self):
        return truncatechars(self.full_url, 40) # сокращаем отображение ссылки в админке

class Users(models.Model):
    user_ip = models.CharField(max_length=50, db_index=True, verbose_name='User IP')

    class Meta:
        verbose_name = 'User'  # для админки
        verbose_name_plural = 'Users'  # для админки
        ordering = ('user_ip',)  # сортировка по ip

    def  __str__(self):
        return self.user_ip