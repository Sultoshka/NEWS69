"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.urls import path, include

from mysite.news.views import register, login_view, logout_view, add_favorite, remove_favorite, favorite_articles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('article/<int:article_id>/add_favorite/', add_favorite, name='add_favorite'),
    path('article/<int:article_id>/remove_favorite/', remove_favorite, name='remove_favorite'),
    path('favorites/', favorite_articles, name='favorite_articles'),
]
