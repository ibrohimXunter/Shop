# Generated by Django 4.2.6 on 2023-10-30 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anime', '0004_alter_anime_options_anime_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время коммента')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime', verbose_name='Аниме')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Коментатор')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
