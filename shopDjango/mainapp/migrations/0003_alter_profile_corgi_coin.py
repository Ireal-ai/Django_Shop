# Generated by Django 4.0.1 on 2022-05-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_profile_corgi_coin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='corgi_coin',
            field=models.PositiveIntegerField(default=0, verbose_name='Corgi coin'),
        ),
    ]
