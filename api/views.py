from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
# from django.http import JsonResponse, HttpResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

def home(request):
    return render(request, 'api/home.html')

# @csrf_exempt
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # data = JSONParser.parse(request)  # No need to pars data, since we are using api_view decorator
        # serializer = ArticleSerializer(data=data)
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        article.delete()
        # return HttpResponse(status=204)
        return Response(status=HTTP_204_NO_CONTENT)
        