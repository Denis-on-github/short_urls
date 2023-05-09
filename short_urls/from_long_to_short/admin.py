from django.contrib import admin
from .models import *


class ShortURLsAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'short_url', 'user', 'created_date')
    search_fields = ('full_url', 'user',)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_ip',)
    search_fields = ('user_ip',)

admin.site.register(ShortURLs, ShortURLsAdmin)
admin.site.register(Users, UsersAdmin)