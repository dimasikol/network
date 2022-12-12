from django.contrib import admin
from .models import Category,Blog
from django.utils.safestring import mark_safe


@admin.register(Category,Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','image_show')
    list_editable = ('name','slug',)

    def image_show(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60"/>')
    image_show.allow_tags = True