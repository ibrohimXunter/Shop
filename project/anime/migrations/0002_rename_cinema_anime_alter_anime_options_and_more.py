# Generated by Django 4.2.6 on 2023-10-21 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cinema',
            new_name='Anime',
        ),
        migrations.AlterModelOptions(
            name='anime',
            options={'verbose_name': 'Кинофилм', 'verbose_name_plural': 'Кинофилмы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
