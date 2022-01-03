from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm
from django.urls import reverse_lazy


class view_article(ListView):
    model = Article
    template_name = 'article.html'
    ordering = ['-id']


class view_ejournal_article_details(DetailView):
    model = Article
    template_name = 'ejournal_article_details.html'


class view_add_article(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'


class view_update_article(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'update_article.html'


class view_delete_article(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('article')
