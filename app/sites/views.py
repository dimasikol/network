from django.shortcuts import render
from .models import Category,Blog
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.


class CategoryView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        self.data = Category.objects.all()
        return render(request,template_name='sites/show/category.html',context={'context':self.data})

class NewsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,category):
        self.data = Blog.objects.filter(category__slug=category)
        return render(request,template_name='sites/show/news_category.html',context={'context':self.data})

class NewsViewItem(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,category,item):
        self.data = Blog.objects.get(slug=item)
        return render(request,template_name='sites/show/item.html',context={'context':self.data})
