from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class view_article(ListView):
    model = Article
    template_name = 'article.html'


class view_ejournal_article_details(DetailView):
    model = Article
    template_name = 'ejournal_article_details.html'