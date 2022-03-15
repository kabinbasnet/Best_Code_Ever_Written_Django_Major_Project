from dataclasses import fields
from django.http import HttpResponse
# Note: LisView and DetailView are class based view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post
from django.shortcuts import render
#  :::::::LoginRequiredMixin Same as login_required decorator::::::::
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # ::::::::::When form is post then we need to valid it and save in our database:::::::::::::::
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # ::::::::::When form is post then we need to valid it and save in our database:::::::::::::::
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # ::::::Each user can only update their post but not the other users:::::::::::
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
