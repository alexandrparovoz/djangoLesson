# Generated by Django 4.1.7 on 2023-03-24 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0004_rename_cat_id_barber_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barber',
            options={'ordering': ['time_create', 'title']},
        ),
    ]
