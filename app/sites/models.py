from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(verbose_name='name_category',max_length=50)
    slug = models.SlugField(verbose_name='slug',max_length=60)
    image = models.ImageField(upload_to='',default='upload_media/sites/category/shablon.jpg')
class Blog(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    name = models.CharField(verbose_name='name_blog',max_length=50)
    text_area = RichTextField(blank=True,null=True)