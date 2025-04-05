from django.conf import settings
from django.db import models
from django.urls import reverse
from .validators import validate_unit_of_measure
# Create your models here.
"""
- Global
    - Ingredients
    - Recipes
- User
    - Ingredients
    - Recipes
        - Ingedients
        - Directions
"""


class Recipe(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=256)
    description = models.TextField(
        blank=True,
        null=True
    )
    directions = models.TextField(
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)   
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id})
    
    def get_edit_url(self):
        return reverse("recipes:update", kwargs={"id": self.id})
    
    def get_ingredients(self):
        return self.recipeingredient_set.all()
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=256)
    description = models.TextField(
        blank=True,
        null=True
    )
    quantity = models.CharField(max_length=64)
    unit = models.CharField(
        max_length=64,
        validators=[validate_unit_of_measure]
    ) # (m, kg, lbs, pounds, gram etc ==> ) Pint comes in handy
    directions = models.TextField(
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)   
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()
    

# class RecipeImage():
#     recipe = models.ForeignKey(Recipe)