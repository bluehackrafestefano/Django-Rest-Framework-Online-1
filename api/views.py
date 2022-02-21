from django.shortcuts import render
from rest_framework import serializers
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

def home(request):
    return render(request, 'api/home.html')

def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = ArticleSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    