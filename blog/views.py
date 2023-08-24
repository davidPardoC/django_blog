from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'title': 'Home'}
    return render(request, 'blog/home.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 


def about(request):
    return render(request, 'blog/about.html')
