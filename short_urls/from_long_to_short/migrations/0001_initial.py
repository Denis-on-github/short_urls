# Generated by Django 4.1.7 on 2023-04-17 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(db_index=True, max_length=50, verbose_name='User IP')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ('user_ip',),
            },
        ),
        migrations.CreateModel(
            name='ShortURLs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.URLField(unique=True, verbose_name='Full URL')),
                ('subpart', models.CharField(blank=True, db_index=True, max_length=5, unique=True, verbose_name='Subpart')),
                ('short_url', models.CharField(blank=True, db_index=True, max_length=100, unique=True, verbose_name='Short URL')),
                ('request_count', models.IntegerField(default=0, verbose_name='Clicks')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='from_long_to_short.users', verbose_name='User IP')),
            ],
            options={
                'verbose_name': 'Short URL',
                'verbose_name_plural': 'Short URLs',
                'ordering': ('-created_date',),
            },
        ),
    ]
