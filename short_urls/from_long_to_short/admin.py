from django.contrib import admin
from .models import *

class ShortURLsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_url', 'short_url', 'created_date')
    search_fields = ('full_url',)

admin.site.register(ShortURLs, ShortURLsAdmin)