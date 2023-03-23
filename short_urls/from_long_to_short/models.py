import random
from django.conf import settings
from django.db import models

class ShortURLs(models.Model):
    full_url = models.URLField(unique=True, verbose_name='Full URL')
    subpart = models.CharField(max_length=settings.LEN_SHORTS, unique=True, db_index=True, blank=True, verbose_name='Subpart')
    short_url = models.CharField(max_length=100, unique=True, db_index=True, blank=True, verbose_name='Short URL')
    request_count = models.IntegerField(default=0, verbose_name='Clicks')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')

    class Meta:
        verbose_name = 'Short URLs'
        verbose_name_plural = 'Short URLs'
        ordering = ('-created_date',) # сортировка по дате и времени добавления

    def __str__(self):
        return self.subpart
        #return f'{self.short_url} -> {self.full_url}'
