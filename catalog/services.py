from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст, получает данные из БД"""
    if CACHE_ENABLED:
        key = 'products_list'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all()
            cache.set(key, products)
        return products
    return Product.objects.all()
