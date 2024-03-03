from src.product_class import Product
import pytest


@pytest.fixture
def product_1():
    return Product('Яблоко', 'Свежее из Краснодара', 9.50, 100)


def test_init(product_1):
    assert product_1.name == 'Яблоко'
    assert product_1.description == 'Свежее из Краснодара'
    assert product_1.price == 9.50
    assert product_1.quantity == 100
