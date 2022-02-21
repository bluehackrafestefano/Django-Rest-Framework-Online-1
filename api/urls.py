from django.urls import path
from .views import home, article_list, article_detail, ArticleAPIView

urlpatterns = [
    path('', home, name='home'),
    # path('article/', article_list, name='article_list'),
    path('article/', ArticleAPIView.as_view(), name='article_list'),
    path('article_detail/<int:pk>/', article_detail, name='article_detail'),
]