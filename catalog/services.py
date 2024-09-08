from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    """Получает данные по категориям из кэша, если кэш пуст, получает данные из БД"""
    if CACHE_ENABLED:
        key = 'categories_list'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
        return categories
    return Category.objects.all()