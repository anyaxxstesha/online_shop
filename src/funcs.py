import json
from category_class import Category
from product_class import Product


def load_data() -> list:
    """
    Загружает список категорий и товаров из файла
    """
    with open('products.json', encoding='utf-8') as file:
        data = json.load(file)
        return data


def create_class_objects(data: list) -> None:
    """
    Создает объекты класса категория и класса продукт
    """
    categories_as_objects = []
    for category in data:
        category = Category(**category)
        products_as_objects = []
        for product in category.products:
            product = Product(**product)
            products_as_objects.append(product)
        category.products = products_as_objects
        categories_as_objects.append(category)
    return
