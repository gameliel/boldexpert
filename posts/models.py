from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class CategoryBanner(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.category.name



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', null=True)
    updated_on = models.DateTimeField(auto_now= True)
    body = RichTextUploadingField()
    categories = models.ManyToManyField('Category', default=None, related_name='posts')
    image = models.ImageField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Banner(models.Model):
    image = models.FileField(upload_to='images/')


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=90, null=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE )

    def __str__(self):
        return self.author
