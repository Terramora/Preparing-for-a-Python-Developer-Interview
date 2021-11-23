"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
"""
import os


def get_path(file_name, folder):
    for element in os.scandir(folder):
        element: os.DirEntry
        if element.is_file():
            if element.name == file_name:
                abs_path = os.path.abspath(os.path.join(folder, file_name))
                file_name = os.path.splitext(os.path.basename(abs_path))[0]
                return file_name, abs_path
        else:
            return get_path(file_name, element.path)


print(get_path('test.py', '.'))
