from django.shortcuts import render
from django.views.generic import CreateView
from articles.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'description')
    #success_url =


