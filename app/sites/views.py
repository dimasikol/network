from django.shortcuts import render
from .models import Category
# Create your views here.

def index(request):

    date = Category.objects.all()

    return render(request,template_name='sites/base.html',context={'context':date})