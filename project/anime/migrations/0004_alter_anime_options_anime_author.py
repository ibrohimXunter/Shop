# Generated by Django 4.2.6 on 2023-10-27 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anime', '0003_anime_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'verbose_name': 'Аниме', 'verbose_name_plural': 'Все аниме'},
        ),
        migrations.AddField(
            model_name='anime',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]