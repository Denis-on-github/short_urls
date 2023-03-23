# Generated by Django 4.1.7 on 2023-03-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.URLField(unique=True, verbose_name='Full URL')),
                ('subpart', models.CharField(blank=True, db_index=True, max_length=5, unique=True, verbose_name='Subpart')),
                ('short_url', models.CharField(blank=True, db_index=True, max_length=100, unique=True, verbose_name='Short URL')),
                ('request_count', models.IntegerField(default=0, verbose_name='Clicks')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
            options={
                'verbose_name': 'Short URLs',
                'verbose_name_plural': 'Short URLs',
                'ordering': ('-created_date',),
            },
        ),
    ]