from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import CommentForm
# Create your views here.


def blog(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')[1:]
    recents = Post.objects.filter(status=1).order_by('-created_on')[:1]
    categories = Category.objects.all()
    context = {'posts':posts, 'categories':categories, 'recents':recents}
    return render(request, 'posts/index.html', context)


def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    recent = get_object_or_404(Post, id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment =  Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    photos = PostImage.objects.filter(post=post)
    context = {'post':post, 'recent':recent, 'photos':photos, 'comments':comments, 'form':form}
    return render(request, 'posts/detail.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
        ).order_by(
            '-created_on'
        )
    context = {'category':category, 'posts':posts}
    return render(request, 'posts/blog_category.html', context)
