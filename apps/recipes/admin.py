from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Recipe, RecipeIngredient

# Register your models here.
User = get_user_model

class RecipeIngredeientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredeientInline]
    list_display = ['name' , 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)
