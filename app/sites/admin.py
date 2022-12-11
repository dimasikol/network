from django.contrib import admin
from .models import Category,Blog
# Register your models here.

@admin.register(Category, Blog)
class CategoryAdmin(admin.ModelAdmin):
    pass