from django.urls.base import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from articles.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'description', 'photo', 'created_at', 'is_publication')
    success_url = reverse_lazy('articles:list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'description', 'photo', 'created_at', 'is_publication')
    success_url = reverse_lazy('articles:list')

    def get_success_url(self):
        return reverse('articles:view', args=[self.kwargs.get('pk')])


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:list')


def article_is_publication(request, pk):
    article_item = get_object_or_404(Article, pk=pk)
    if article_item.is_publication:
        article_item.is_publication = False
    else:
        article_item.is_publication = True

    article_item.save()

    return redirect(reverse('articles:list'))


