from src.category_class import Category
from src.product_class import Product
import pytest


@pytest.fixture
def product_1():
    return Product('Peach', 'Sunshine sort', 42.0, 20)


@pytest.fixture
def product_2():
    return Product('Fig', 'Resort sort', 12.0, 40)


@pytest.fixture
def category_1(product_1, product_2):
    return Category('Фрукты', 'Свежие фрукты из Краснодара',
                    [product_1, product_2])


def test_init(category_1, product_1, product_2):
    assert category_1.name == 'Фрукты'
    assert category_1.description == 'Свежие фрукты из Краснодара'
    assert category_1.products == [product_1, product_2]
    assert Category.number_of_categories == 1
    assert Category.number_of_products == 2
