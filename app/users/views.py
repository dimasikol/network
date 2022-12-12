from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

def index(request):
    return render(request,template_name='base.html',context={'context':'printvettt'})


class Lk(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self):

        return render()
