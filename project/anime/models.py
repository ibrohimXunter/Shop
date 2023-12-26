from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Anime(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название фильма')
    context = models.TextField(verbose_name='Описание фильма')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = models.CharField(max_length=255, verbose_name='Ссылка видио', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('anime', kwargs={'pk': self.pk})

    def get_photo_anime(self):
        try:
            return self.photo.url
        except:
            return 'https://imageproxy.ifunny.co/noop/user_photos/cb68ad6075e5a6428131ca8ca1916ea5c11f464a_0.jpg'

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Все аниме'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Коментатор')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Аниме')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата коментария')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Профиль')
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name='Фото профилья')
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Номер телефона')
    about_user = models.CharField(max_length=100, blank=True, null=True, verbose_name='О себе')
    publisher = models.BooleanField(default=True, verbose_name='Право на добавление фильма')

    def __str__(self):
        return self.user.username

    def get_photo_user(self):
        try:
            return self.photo.url
        except:
            return 'https://www.computingtech.net/wp-content/uploads/2016/08/generic.png'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'









