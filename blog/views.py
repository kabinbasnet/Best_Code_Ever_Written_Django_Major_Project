from django.http import HttpResponse
from django.views.generic import ListView  # Note: LisView is class based view
from .models import Post
from django.shortcuts import render

# ::::::::Creating dummy data in list form:::::::::::::::::::::::::::
# Dummy data ==>> being information that doesnot contain any useful data, but serves to reserve space.
# posts = [
#     {
#         'author': 'Kabin Basnet',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'March 1, 2022'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'March 2, 2022'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post

    # <app ==>> blog >/<model ==>> Post >_<viewtype =>> blog/home.html >.html
    template_name = 'blog/home.html'

    context_object_name = 'posts'
    # -date_posted ==> gives recent to oldest date time views
    ordering = ['-date_posted']


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
