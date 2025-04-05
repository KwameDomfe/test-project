from django.contrib import admin
from django.urls import path, include
from .views import (
    Index
)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Index, name='index'),

    path('info/', include('apps.info.urls')),

    path('articles/', include('apps.articles.urls')),

    path('pantry/recipes/', include('apps.recipes.urls')),

    path('accounts/', include('apps.accounts.urls'))
]
