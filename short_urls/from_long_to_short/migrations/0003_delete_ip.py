# Generated by Django 4.1.7 on 2023-04-12 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('from_long_to_short', '0002_ip'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IP',
        ),
    ]
