class Product:
    """Класс для представления товара."""

    name: str
    description: str
    price: float
    quantity: int

    goods_created = []

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
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
                self.price = max(self.price, good.price)
                cls.goods_created.remove(good)
                break

        cls.goods_created.append(self)
        return self
