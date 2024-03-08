class Category:
    """Класс для представления категории."""

    name: str
    description: str
    __products: list

    # Переменная на уровне класса для подсчета количества категорий
    number_of_categories = 0
    # Переменная на уровне класса для подсчета количества уникальных товаров
    number_of_products = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(self.__products)

    def add_product(self, product):
        """
        Принимает объект товара и добавляет в список товаров категории
        """
        self.__products.append(product)
