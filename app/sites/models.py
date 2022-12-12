from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(verbose_name='name_category',max_length=50,unique=True)
    slug = models.SlugField(verbose_name='slug',max_length=60,unique=True)
    image = models.ImageField(upload_to='sites/category/%Y/%m/%d/',default='upload_media/sites/category/shablon.jpg',blank=True)
    def __str__(self):
        return self.name
class Blog(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    name = models.CharField(verbose_name='name_blog',max_length=50)
    slug = models.SlugField(verbose_name='slug',max_length=60)
    image = models.ImageField(upload_to='sites/blog/%Y/%m/%d/',default='upload_media/sites/category/shablon.jpg',blank=True)
    text_area = RichTextField(blank=True,null=True)