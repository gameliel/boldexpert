from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = RichTextUploadingField()
    image = models.FileField(blank=True)
    status = models.BooleanField(default=None, null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete = models.CASCADE, null=True)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.portfolio.title