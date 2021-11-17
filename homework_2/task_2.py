"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    __name = 'Test'
    __price = 100


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(self.__name, self.__price)


a = ItemDiscount()
b = ItemDiscountReport()
b.get_parent_data()
