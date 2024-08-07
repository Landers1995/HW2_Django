from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from articles.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'description',)
    success_url = reverse_lazy('articles:list')


class ArticleListView(ListView):
    model = Article
