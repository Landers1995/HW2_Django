from django.contrib import admin
from django.urls import path, include

from articles.apps import ArticlesConfig
from articles.views import ArticleCreateView, ArticleListView

app_name = ArticlesConfig.name

urlpatterns = [
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("", ArticleListView.as_view(), name="list"),
    # path("view/<int:pk>/", ..., name="view"),
    # path("edit/<int:pk>/", ..., name="edit"),
    # path("delete/<int:pk>/", ..., name="delete"),
    ]
