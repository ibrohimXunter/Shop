from django.urls import path
from .views import *

urlpatterns = [
    path('', AnimeListView.as_view(), name='index'),
    path('category/<int:pk>/', AnimeListByCategory.as_view(), name='category'),
    path('anime/<int:pk>/', AnimeDetailView.as_view(), name='anime'),
    path('add_anime/', NewAnime.as_view(), name='add_anime'),
    path('anime/<int:pk>/update/', AnimeUpdate.as_view(), name='update'),
    path('anime/<int:pk>/delete/', AnimeDelete.as_view(), name='delete'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register_user, name='register'),
    path('save_comment/<int:pk>/', save_comment, name='save_comment'),
    path('profile/<int:pk>/', profile_view, name='profile'),
    path('edit_account/', edit_account_view, name='edit_account'),
    path('edit_profile/', edit_profile_view, name='edit_profile'),
]