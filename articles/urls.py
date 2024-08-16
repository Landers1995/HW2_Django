from django.contrib import admin
from django.urls import path, include

from articles.apps import ArticlesConfig
from articles.views import ArticleCreateView, ArticleUpdateView, ArticleListView, ArticleDetailView, ArticleDeleteView, \
    article_is_publication

app_name = ArticlesConfig.name

urlpatterns = [
    path("article_create/", ArticleCreateView.as_view(), name="article_create"),
    path("", ArticleListView.as_view(), name="article_list"),
    path("article_view/<int:pk>/", ArticleDetailView.as_view(), name="article_view"),
    path("article_edit/<int:pk>/", ArticleUpdateView.as_view(), name="article_edit"),
    path("article_delete/<int:pk>/", ArticleDeleteView.as_view(), name="article_delete"),
    path("activity/<int:pk>/", article_is_publication, name="article_is_publication"),
]
