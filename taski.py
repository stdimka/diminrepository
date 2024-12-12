# list1 = ["Alice", "Bob", "Charlie"]
# list2 = [25, 30, 35]
#
# # Объединение двух списков в список кортежей с использованием zip()
# zipped_list = list(zip(list1, list2))
# print("Объединенный список кортежей:", zipped_list)
#
# # Список чисел
# numbers = [10, 20, 5, 15, 30]
#
# # Наименьший элемент в списке чисел
# min_number = min(numbers)
# print("Наименьший элемент в списке чисел:", min_number)
#
# # Наибольший элемент в списке чисел
# max_number = max(numbers)
# print("Наибольший элемент в списке чисел:", max_number)
#
# # Сумма всех элементов в списке чисел
# sum_numbers = sum(numbers)
# print("Сумма всех элементов в списке чисел:", sum_numbers)

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# spisok = ['first', 'zalupa', 'spathochu']
# dlina = list(sorted(spisok, key=lambda x: len(x)))
# print(dlina)

# def outer_function(x):
#     def inner_function(y):
#         return x + y
#
#     return inner_function
#
# closure = outer_function(10)
# print(closure(5))


# def счетчик():
#     число = 0  # Секретное хранилище
#
#     def увеличить():
#         nonlocal число
#         число += 1
#         return число
#
#     return увеличить
# мой_счётчик = счетчик()
# print(мой_счётчик())  # 1
# print(мой_счётчик())  # 2
# print(мой_счётчик())  # 3

# def make_counter():
#     null = 0
#     def counter():
#         nonlocal null
#         null += 1
#         return null
#     return counter
# odin = make_counter()
# dva = make_counter()
# print(odin())
# print(odin())
# print(dva())
# print(dva())


# def large_range(n):
#     for i in range(n):
#         yield i
#
# for value in large_range(1000000):
#     # Обрабатываем значения по одному
#     print(value)


# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacci()
# for _ in range(10):
#     print(next(fib))

#
# for i in range(10):
#     print(i)

# def my_decorator(func):
#     def wrapper():
#         print("Перед вызовом функции")
#         func()
#         print("После вызова функции")
#
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello!")
# say_hello()

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator_repeat
# @repeat(num_times=5)
# def say_hello(name):
#     print(f"Hello, {name}!")
# say_hello("Alice")


# def my_decorator(func):
#     def wrapper():
#         print("Перед вызовом функции")
#         func()
#         print("После вызова функции")
#
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()

# class MyClass:
#     def __init__(self, value):
#         self.hidden_value = value
#
#     @property
#     def value(self):
#         return self.hidden_value
#
#     @value.setter
#     def value(self, new_value):
#         self.hidden_value = new_value
#
# obj = MyClass(10)
# print(obj.value)  # Вывод: 10
# obj.value = 20
# print(obj.value)  # Вывод: 20

# import platform
#
# os_name = platform.system()
# print("Operating System:", os_name)
#
# architecture = platform.architecture()
# print("Architecture:", architecture)
# processor = platform.processor()
# print("Processor:", processor)
#
# import sys
#
# # Список загруженных модулей
# print("Загруженные модули:")
# for module in sys.modules:
#     print(module)

import os

# import os
#
# # Создаем директорию
# os.mkdir("test_directory")
#
# # Переходим в созданную директорию
# os.chdir("test_directory")
#
# # Создаем файл и записываем текст
# with open("test_file.txt", "w") as file:
#     file.write("Hello, World!")
#
# # Читаем содержимое файла
# with open("test_file.txt", "r") as file:
#     content = file.read()
#     print("Содержимое файла:", content)
#
# # Удаляем файл
# os.remove("test_file.txt")
#
# # Переходим на уровень выше и удаляем директорию
# os.chdir("..")
# os.rmdir("test_directory")

# from datetime import date
#
# # Запросить у пользователя год, месяц и день его рождения
# year = int(input("Введите год рождения: "))
# month = int(input("Введите месяц рождения (1-12): "))
# day = int(input("Введите день рождения (1-31): "))
#
# # Создать объект даты рождения
# birth_date = date(year, month, day)
#
# # Получить текущую дату
# current_date = date.today()
#
# # Вычислить разницу между текущей датой и датой рождения
# days_difference = (current_date - birth_date).days
#
# # Вывести количество дней, прошедших с даты рождения
# print(f"С даты вашего рождения прошло {days_difference} дней.")