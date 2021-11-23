"""
3. Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""
import random

keys = [i for i in range(random.randint(1, 10))]
values = [i for i in range(random.randint(1, 10))]

print(keys, values)


# print(dict(zip(ls1, ls2)))

def create_dict(ls1: list, ls2: list) -> dict:
    result = {}
    for i, val in enumerate(ls1):
        try:
            value = ls2[i]
        except IndexError:
            value = None

        result[val] = value

    return result


print(create_dict(keys, values))
