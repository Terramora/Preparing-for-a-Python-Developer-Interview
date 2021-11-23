"""
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def check_number(num: float) -> bool:
    split_num = str(num).split('.')
    first_num = int(split_num[0])
    second_num = int(split_num[1])
    if int(str(num).split('.')[1]) > 1:
        print('Дробное число')
        return first_num == second_num

    else:
        print('Целое число')


try:
    number = float(input('Введите число: ').replace(',', '.'))
except ValueError as er:
    print(er)
else:
    print(check_number(number))
