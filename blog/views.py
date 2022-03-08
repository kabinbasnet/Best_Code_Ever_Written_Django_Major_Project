from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# ::::::::Creating dummy data in list form:::::::::::::::::::::::::::
# Dummy data ==>> being information that doesnot contain any useful data, but serves to reserve space.
posts = [
    {
        'author': 'Kabin Basnet',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 1, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 2, 2022'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
