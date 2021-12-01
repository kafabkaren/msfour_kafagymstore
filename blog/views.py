from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# from .forms import CommentForm


class view_blog(ListView):
    model = Post
    template_name = 'blog.html'


class view_article_details(DetailView):
    model = Post
    template_name = 'article_details.html'

# class view_add_comment(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'add_comment.html'
#     fields = '__all__'
#     success_url = reverse('home')