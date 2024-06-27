from django.shortcuts import render
from .models import Article

def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_articles': latest_articles}
    return render(request, 'news/index.html', context)
# Create your views here.
