from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def blog(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    categories = Category.objects.all()
    context = {'posts':posts, 'categories':categories}
    return render(request, 'posts/index.html', context)


def detail_view(request, id):
	post = get_object_or_404(Post, id=id)
	photos = PostImage.objects.filter(id=id)
	context = {'post':post, 'photos':photos}
	return render(request, 'posts/detail.html', context)
