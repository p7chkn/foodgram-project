# Generated by Django 3.1.3 on 2020-11-23 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_auto_20201123_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorites',
            options={'verbose_name': 'Избранное'},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'Подкиски'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='purchases',
            options={'verbose_name': 'Покупки'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Рецепты'},
        ),
    ]
