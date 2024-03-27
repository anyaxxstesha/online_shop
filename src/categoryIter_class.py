from category_class import Category


class CategoryIter:
    """Класс, принимающий на вход объект категория и дающий возможность использовать цикл for для прохода
    по всем товарам данной категории"""

    category: Category

    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value < len(self.category):
            self.current_value += 1
            return self.category.products[self.current_value]
        else:
            raise StopIteration
