from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class view_blog(ListView):
    model = Post
    template_name = 'blog.html'


class view_article_details(DetailView):
    model = Post
    template_name = 'article_details.html'

