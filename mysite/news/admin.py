from django.contrib import admin
from .models import NewsCategory, News

class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category__name')
    list_filter = ('category', 'created_at')

admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(News, NewsAdmin)