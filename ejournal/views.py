from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class view_article(ListView):
    model = Article
    template_name = 'article.html'




