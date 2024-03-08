class Product:
    """Класс для представления товара."""

    name: str
    description: str
    __price: float
    quantity: int

    goods_created = []

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """
        Создаёт товар и возвращает объект, дополнительно проверяя наличие такого же товара
        """
        self = cls(name, description, price, quantity)

        for good in cls.goods_created:
            if self.name == good.name:
                self.quantity += good.quantity
                self.__price = max(self.__price, good.price)
                cls.goods_created.remove(good)
                break

        cls.goods_created.append(self)
        return self

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Устанавливает новую цену для товара, при понижении цены спрашивает подтверждение
        """
        if new_price <= 0:
            print('Введена некорректная цена')
        elif new_price <= self.__price:
            confirmation = input('Вы уверены, что хотите понизить цену? y - да, n - нет')
            if confirmation == 'y':
                self.__price = new_price
        else:
            self.__price = new_price
