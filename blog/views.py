from django.shortcuts import render
from.models import *
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
        
    return render(request, 'blog/blog.html',{
        'posts': posts,
        'comments': comments
    })