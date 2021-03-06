from dataclasses import fields
from django.http import HttpResponse
# Note: LisView and DetailView are class based view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.shortcuts import render, get_object_or_404
#  :::::::LoginRequiredMixin Same as login_required decorator::::::::
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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

    # ::::::::::paginate_by means give pagination(a process used to divide a large data into smaller discrete pages) after 2 posts::::::::::::::
    paginate_by = 5


class UserPostListView(ListView):
    # :::::::::For User who can see their post only:::::::::::::::::
    model = Post

    # <app ==>> blog >/<model ==>> Post >_<viewtype =>> blog/home.html >.html
    template_name = 'blog/user_posts.html'

    context_object_name = 'posts'

    ordering = ['-date_posted']

    # ::::::::::paginate_by means give pagination(a process used to divide a large data into smaller discrete pages) after 2 posts::::::::::::::
    paginate_by = 5

    # ::::::Pass this query in url:::::::::::
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # Note: '-date_posted' ==> gives recent to oldest date time views
        return Post.objects.filter(author=user).order_by('-date_posted')


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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # ::::::::::::::After deleting the post it'll takes us to home page:::::::::::::::
    success_url = '/'

    # ::::::Each user can only delete their post but not the other users post:::::::::::
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
