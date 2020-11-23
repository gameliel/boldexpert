from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

CATEGORY = (Category)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', null=True)
    updated_on = models.DateTimeField(auto_now= True)
    body = models.TextField()
    Category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title
