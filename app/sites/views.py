from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,template_name='sites/base.html',context={"text":"text2"})