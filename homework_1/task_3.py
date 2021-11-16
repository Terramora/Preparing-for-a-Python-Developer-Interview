"""
Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""
import time

COUNT_NUMS = 3


def simple_random(start: int, end: int) -> (dict, list):
    dt = {}
    ls = []
    if end > start > 0 and end > 0:
        count_of_characters = len(list(str(end)))
        success_iter = 0
        while success_iter < COUNT_NUMS:
            for num in range(1, count_of_characters + 1):
                now = str(time.time()).split('.')[1]
                random_number = int(now[-num:])
                if start <= random_number <= end:
                    success_iter += 1
                    ls.append(random_number)
                    dt[f'elem_{success_iter}'] = random_number
                    time.sleep(1)

        return dt, ls


print(simple_random(1000, 9999))
