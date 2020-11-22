# Generated by Django 3.1.3 on 2020-11-22 07:00

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20201122_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'breakfast'), (2, 'lunch'), (3, 'dinner')], max_length=5, null=True),
        ),
    ]
