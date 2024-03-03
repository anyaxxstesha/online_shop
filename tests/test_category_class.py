from src.category_class import Category
import pytest


@pytest.fixture
def category_1():
    return Category('Фрукты', 'Свежие фрукты из Краснодара', ['peaches', 'figs', 'figs'])


def test_init(category_1):
    assert category_1.name == 'Фрукты'
    assert category_1.description == 'Свежие фрукты из Краснодара'
    assert category_1.products == ['peaches', 'figs', 'figs']
    assert Category.number_of_categories == 1
    assert Category.number_of_products == {'peaches', 'figs'}
