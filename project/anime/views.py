from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Category, Anime, Comment, Profile
from .forms import AnimeForm, LoginForm, RegisterForm, CommentForm, EditAccountForm, EditProfileForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.


class AnimeListView(ListView):
    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'animas'
    extra_context = {
        'title': 'Главная страница: АниМагия'
    }



class AnimeListByCategory(AnimeListView):
    def get_queryset(self):
        animas = Anime.objects.filter(category_id=self.kwargs['pk'])
        return animas

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Аниме: {category.title}'
        return context



class AnimeDetailView(DetailView):
    model = Anime
    context_object_name = 'anime'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        anime = Anime.objects.get(pk=self.kwargs['pk'])
        anime.views += 1
        anime.save()
        animas = Anime.objects.all()[::-1][:3]
        context['title'] = f'Аниме: {anime.title}'
        context['animas'] = animas
        context['comments'] = Comment.objects.filter(anime=anime)

        if self.request.user.is_authenticated:
            context['form'] = CommentForm()
        return context



class NewAnime(CreateView):
    form_class = AnimeForm
    template_name = 'anime/add_anime.html'
    extra_context = {
        'title': 'Добавить аниме'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnimeUpdate(UpdateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'anime/add_anime.html'
    extra_context = {
        'title': 'Изменить аниме'
    }



class AnimeDelete(DeleteView):
    model = Anime
    context_object_name = 'anime'
    success_url = reverse_lazy('index')



# Функция для входа в Аккаунт
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            if user:
                login(request, user)
                messages.success(request, 'Успешный вход в Аккаунт')
                return redirect('index')
            else:
                messages.error(request, 'Не верный логин или пароль')
                return redirect('login')
        else:
            messages.error(request, 'Не верный логин или пароль')
            return redirect('login')

    else:
        login_form = LoginForm()

    context = {
        'title': 'Войти в Аккаунт',
        'login_form': login_form
    }
    if not request.user.is_authenticated:
        return render(request, 'anime/login.html', context)
    else:
        return redirect('index')


def user_logout(request):
    logout(request)
    messages.warning(request, 'Вы вышли из Аккаунта')
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            profile = Profile.objects.create(user=user)
            profile.save()

            messages.success(request, 'Регистрация прошла успешно')
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('register')

    else:
        form = RegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }

    if not request.user.is_authenticated:
        return render(request, 'anime/register.html', context)
    else:
        return redirect('index')


# Функция для сохранения комментария
def save_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.anime = Anime.objects.get(pk=pk)
        comment.user = request.user
        comment.save()
        messages.success(request, 'Ваш комментарий оставлен')
        return redirect('anime', pk)



def profile_view(request, pk):
    profile = Profile.objects.get(user_id=pk)
    animas = Anime.objects.filter(author_id=pk)
    most_viewed = animas.order_by('-views')[:1][0]
    recent_anime = animas.order_by('-created_at')[:1][0]


    context = {
        'title': f'Профиль: {request.user.username}',
        'profile': profile,
        'most_viewed': most_viewed,
        'recent_anime': recent_anime
    }

    return render(request, 'anime/profile.html', context)



def edit_account_view(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные Аккаунта изменены')
            return redirect('profile', request.user.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('change')

    else:
        form = EditAccountForm(instance=request.user)

    context = {
        'title': f'Изменение Аккаунта: {request.user.username}',
        'form': form
    }

    return render(request, 'anime/change.html', context)



def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные Профилья изменены')
            return redirect('profile', request.user.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('change')

    else:
        form = EditProfileForm(instance=request.user.profile)

    context = {
        'title': f'Изменение Профилья: {request.user.username}',
        'form': form
    }

    return render(request, 'anime/change.html', context)












