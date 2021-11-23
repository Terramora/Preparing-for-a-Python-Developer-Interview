"""Дополнить следующую функцию недостающим кодом:

def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах
"""
from os import path, DirEntry, scandir


def print_directory_contents(path_: str, result: dict = None):
    if not result:
        result = {}

    if path.isdir(path_):
        for obj in scandir(path_):
            obj: DirEntry
            if obj.is_file():
                print(f'path: "{obj.path}", file: "{obj.name}"')
            else:
                print_directory_contents(obj.path, result)

    else:
        print(f'{path_} is not directory')


print_directory_contents(r"""../""")
