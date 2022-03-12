from django.urls import path
from . import views
from .views import PostListView  # Note: PostListView is class based view

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]


