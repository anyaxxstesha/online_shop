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

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.__products})'

    def __len__(self):
        return len(self.__products)

    def add_product(self, product):
        """
        Принимает объект товара и добавляет в список товаров категории
        """
        self.__products.append(product)

    @property
    def products(self):
        """
        Выводит список товаров в формате: Продукт, 80 руб. Остаток: 15 шт.
        """
        for product in self.__products:
            print(product)
        return self.__products
