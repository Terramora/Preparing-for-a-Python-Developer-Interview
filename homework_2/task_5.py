"""
5. Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    __name = 'Test'
    __price = 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount):
        self.discount = discount

    def __str__(self):
        return f'Цена "{self.name}" без скидки {self.price}, скидка {self.discount}%, итог:{self.price - self.price * self.discount / 100}'

    def get_parent_data(self):
        print(self.name, self.price)


a = ItemDiscount()
b = ItemDiscountReport(10)
b.name, b.price = 'name', 5000
print(b)
