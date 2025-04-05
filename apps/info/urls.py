
from django.urls import path
from .views import (
    Info_Index,
    About
)

urlpatterns = [
    path(
        '', 
        Info_Index, 
        name='info-index'
    ),
    path(
        'about/', 
        About, 
        name='info-about'
    ),
]
