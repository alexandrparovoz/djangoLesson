# Generated by Django 4.1.7 on 2023-03-21 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0002_category_barber_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barber',
            old_name='cat',
            new_name='cat_id',
        ),
    ]
