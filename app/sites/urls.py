from .views import CategoryView,NewsView,NewsViewItem
from django.urls import path

urlpatterns = [
    path('',CategoryView.as_view(),name='category'),
    path('<slug:category>',NewsView.as_view(),name='news_category'),
    path('<slug:category>/<slug:item>',NewsViewItem.as_view(),name='news_item')
]