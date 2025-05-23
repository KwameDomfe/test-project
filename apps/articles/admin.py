from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug', 'updated','published', 'timestamp']
    search_fields = ['title', 'contents']
    raw_id_fields = ['user']

admin.site.register(Article, ArticleAdmin)