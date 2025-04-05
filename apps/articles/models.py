from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import (
    pre_save, post_save
)
from django.urls import reverse
from django.utils import timezone
from .utils import slugify_instance_title

# Create your models here.

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(contents__icontains=query)
        return self.filter(lookups)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query) 
class Article (models.Model):
    user = models.ForeignKey(
        User,
        blank=True, 
        null=True,
        on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, null=True, unique=True)
    contents = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    published = models.DateField(
        auto_now = False, 
        auto_now_add=False, 
        null=True, 
        blank=True, 
        default=timezone.now
    )
    objects = ArticleManager()

    def get_absolute_url(self):
        # return f"/articles/{self.slug}/"
        return reverse("articles:detail", kwargs={'article_slug': self.slug})
    
    def save(self, *args, **kwargs):

        # if self.slug is None:
        #     self.slug = slugify(self.title)
          
        # if self.slug is None:
        #     slugify_instance_title = (self, save=False)
        
        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    print('pre-save')
    
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    print('post-save')
    
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)

