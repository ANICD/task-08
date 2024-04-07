import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    # result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int):
    """
    Функция для переноса указанной строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """
    with open(source, "r", encoding="utf-8") as source_file:
        lines = source_file.readlines()
    # Строка для переноса
    transferring_line = lines[num_row - 1]
    # Удаляем строку
    del lines[num_row - 1]
    # Записываем изменения обратно в исходный файл
    with open(source, "w", encoding="utf-8") as f_source:
        f_source.writelines(lines)
    # Запись в новый файл
    with open(dest, "a", encoding="utf-8") as f_dest:
        f_dest.write(transferring_line)
    print("Запись перенесена.")

INFO_STRING = """
Выберите ркжим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
5 - выход из программы
"""

file_s = "source.txt"
file_d = "dest.txt"

if file_s not in os.listdir():
    print("указанное имя файла отсутсвует")
    sys.exit()

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        printing_file = input("Введите имя файла для просмотра содержимого:")
        print(read_all(printing_file))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file_s)
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file_s, data))
    elif mode == 4:
        input_file = input("Введите имя файла источника:")
        with open(input_file, "r", encoding="utf-8") as s_file:
            for line in s_file:
                print(line.strip())
        n_row = int(input("Ведите номер строки для переноса в новый файл:"))
        output_file = input("Введите имя конечного файла:")
        transfer_data(input_file, output_file, n_row)
    elif mode == 5:
        print("Программа завершена.")
        break


