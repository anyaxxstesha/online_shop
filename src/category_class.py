class Category:
    """Класс для представления категории."""

    name: str
    description: str
    products: list

    # Переменная на уровне класса для подсчета количества категорий
    number_of_categories = 0
    # Переменная на уровне класса для подсчета количества уникальных товаров
    number_of_products = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(self.products)
