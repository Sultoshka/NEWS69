from django.shortcuts import render
from .models import Article
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article

@login_required
def add_favorite(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article not in request.user.favorite_articles.all():
        request.user.favorite_articles.add(article)
    return redirect('article_detail', article_id=article.id)

@login_required
def remove_favorite(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article in request.user.favorite_articles.all():
        request.user.favorite_articles.remove(article)
    return redirect('article_detail', article_id=article.id)


def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_articles': latest_articles}
    return render(request, 'news/index.html', context)


def index(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles})


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

def favorite_articles(request):
    articles = request.user.favorite_articles.all()
    return render(request, 'favorite_articles.html', {'articles': articles})