"""
4. Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
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

    def get_parent_data(self):
        print(self.name, self.price)


a = ItemDiscount()
b = ItemDiscountReport()
b.name, b.price = 'name', 5
b.get_parent_data()
