from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'title': 'First post',
        'content': 'This is the first post.',
        'author': 'John Doe',
        'date_posted': '2020-01-01'
    },
    {
        'title': 'Second post',
        'content': 'This is the second post.',
        'author': 'Jane Doe',
        'date_posted': '2020-01-02'
    }
]


def home(request):
    context = {'posts': posts, 'title': 'Home'}
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
