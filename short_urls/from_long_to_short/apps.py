from django.apps import AppConfig


class FromLongToShortConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'from_long_to_short'
    verbose_name = 'Short URLs'
