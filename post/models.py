from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    #image = models.ImageField()
    image_url = models.URLField(default='https://assets.asaxiy.uz/product/main_image/desktop//61165331d95f7.jpg')
