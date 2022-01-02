from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import ArticleForm


class view_article(ListView):
    model = Article
    template_name = 'article.html'


class view_ejournal_article_details(DetailView):
    model = Article
    template_name = 'ejournal_article_details.html'


class view_add_article(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'
