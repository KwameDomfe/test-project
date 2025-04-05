from django.urls import path
from .views import (
    article_detail,
    articles_search,
    article_create
)

app_name = 'articles'

urlpatterns = [
    # path(
    #     '', 
    #     articles_index, 
    #     name='articles-index'
    # ), 
    path(
        '', 
        articles_search, 
        name='search'
    ),
    path(
        'create/', 
        article_create, 
        name='create'
    ),
    path(
        '<slug:article_slug>/', 
        article_detail, 
        name='detail'
    ),
    
]
