from django.urls import path
from .views import home, article_list

urlpatterns = [
    path('', home, name='home'),
    path('article/', article_list, name='article_list'),
]