# Generated by Django 3.1.3 on 2020-11-22 06:56

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20201122_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('BR', 'завтрак'), ('LN', 'обед'), ('DN', 'ужин')], max_length=8, null=True),
        ),
    ]