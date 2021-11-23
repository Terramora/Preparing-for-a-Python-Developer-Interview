"""
6. Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemDiscountReport1(ItemDiscount):

    def __init__(self, discount):
        self.discount = discount

    def __str__(self):
        return f'Цена "{self.name}" без скидки {self.price}, скидка {self.discount}%, итог:{self.price - self.price * self.discount / 100}'

    def get_parent_data(self):
        print(self.name, self.price)

    def get_info(self):
        print(self.name)


class ItemDiscountReport2(ItemDiscount):

    def __init__(self, discount):
        self.discount = discount

    def __str__(self):
        return f'Цена "{self.name}" без скидки {self.price}, скидка {self.discount}%, итог:{self.price - self.price * self.discount / 100}'

    def get_parent_data(self):
        print(self.name, self.price)

    def get_info(self):
        print(self.price)


a = ItemDiscount()
b = ItemDiscountReport1(1000)
c = ItemDiscountReport2(1000)

for obj in (b, c):
    obj.get_info()
    func = getattr(obj, 'get_info')
    func()
    eval('obj.get_info()')
