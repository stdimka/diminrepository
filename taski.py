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

# class Car:
#     make = "атрибут мейк "
#     model = 'атрибут модель'
#     year = 'атрибут ер'
#     def display_info(self):
#         print(self.make, self.model, self.year)
#
# my_object = Car()
# my_object.display_info()

# class Library:
#     books = ["золушка", "война миров"]  # Атрибут класса
#     def add_book(self, book):
#         self.books.append(book)  # Добавляем книгу в общий список
#     def display_books(self):
#         print(self.books)  # Печатаем список книг
#
# # Создаем объект класса Library
# my_object = Library()
# my_object.add_book("колобок")
# my_object.display_books()


# class Cat:
#     pass
# # Создание объекта Cat
# barsik = Cat()
# # Инициализация атрибутов после создания объекта
# barsik.name = "Barsik"
# barsik.age = 5
# print(f"Имя кота: {barsik.name}, возраст: {barsik.age}")  # Вывод: Имя кота: Barsik, возраст: 5


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # Создание объекта Cat с именем и возрастом
# barsik = Cat("Barsik", 5)
# print(f"Имя кота: {barsik.name}, возраст: {barsik.age}")  # Вывод: Имя кота: Barsik, возраст: 5

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         print(self.width * self.height)  # Используем атрибуты объекта
# # Создаем объект класса Rectangle
# square = Rectangle(6, 5)
# # Вызываем метод area
# square.area()

# class BankAccount:
#     def __init__(self, account_number, initial_balance):
#         self.account_number = account_number
#         self.balance = initial_balance  # Устанавливаем начальный баланс
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"На счет {self.account_number} внесено {amount}. Текущий баланс: {self.balance}.")
#         else:
#             print("Сумма для пополнения должна быть больше нуля.")
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f"Недостаточно средств на счете {self.account_number}. Доступно: {self.balance}.")
#         elif amount > 0:
#             self.balance -= amount
#             print(f"Со счета {self.account_number} снято {amount}. Текущий баланс: {self.balance}.")
#         else:
#             print("Сумма для снятия должна быть больше нуля.")
# # Создание объекта BankAccount
# my_account = BankAccount("123456789", 1000)
# # Выполнение операций пополнения и снятия средств
# my_account.deposit(500)      # Пополнение на 500
# my_account.withdraw(200)     # Снятие 200
# my_account.withdraw(1500)    # Попытка снять больше, чем есть на счете
# my_account.deposit(-100)     # Попытка внести отрицательную сумму
# my_account.withdraw(0)       # Попытка снять ноль

# class MyClass:
#     def __init__(self):
#         self.__private_attribute = "I am private"
# obj = MyClass()
# print(dir(obj))

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand      # Публичный атрибут
#         self._model = model     # Защищенный атрибут
#     # Метод для получения значения защищенного атрибута _model_
#     def get_model(self):
#         return self._model
#     # Метод для установки значения защищенного атрибута _model_
#     def set_model(self, model):
#         if isinstance(model, str) and model.strip():  # Проверка, что значение является непустой строкой
#             self._model = model
#         else:
#             print("Ошибка: Модель должна быть непустой строкой.")
# # Создание объекта класса Car
# my_car = Car("Toyota", "Corolla")
# # Установка значений атрибутов
# my_car.brand = "Honda"  # Изменение публичного атрибута brand
# my_car.set_model("Civic")  # Установка нового значения для защищенного атрибута _model_
# # Вывод значений атрибутов
# print(f"Марка автомобиля: {my_car.brand}")  # Доступ к публичному атрибуту
# print(f"Модель автомобиля: {my_car.get_model()}")  # Получение значения защищенного атрибута через метод


# class Library:
#     def __init__(self):
#         self.books = []
#     def add_book(self, book):
#         if isinstance(book, str) and book.strip():
#             self.books.append(book)
#         else:
#             print("Ошибка: Название книги должно быть непустой строкой.")
#     def __str__(self):
#         if self.books:
#             books_list = "\n".join(self.books)
#             return f"Библиотека содержит следующие книги:\n{books_list}"
#         else:
#             return "Библиотека пуста."
#     def __len__(self):
#         return len(self.books)
# # Создаем объект библиотеки
# library = Library()
# # Добавляем книги в библиотеку
# library.add_book("Harry Potter and the Philosopher's Stone")
# library.add_book("The Great Gatsby")
# library.add_book("1984")
# # Выводим информацию о библиотеке с перечнем книг и количество книг
# print(library)
# print(f"Number of books in library: {len(library)}")


# class Animal:
#     def speak(self):
#         return "Some generic animal sound"
##
# class Dog(Animal):
#     def speak(self):
#         parent_speech = super().speak()  # Вызов метода родительского класса
#         return f"{parent_speech} And the dog barks!"
# dog = Dog()
# print(dog.speak())
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
##
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return f"Withdrew {amount}. New balance: {self.balance}"
#         return "Insufficient funds"
##
# class SavingsAccount(BankAccount):
#     def withdraw(self, amount):
#         if amount > 1000:
#             return "Withdrawal limit exceeded"
#         return super().withdraw(amount)  # Вызов метода родительского класса
##
# savings = SavingsAccount(1500)
# print(savings.withdraw(500))  # Выведет: Withdrew 500. New balance: 1000
# print(savings.withdraw(1500))  # Выведет: Withdrawal limit exceeded


# class Employee:
#     def get_salary(self):
#         return 1000
# class FullTimeEmployee(Employee):
#     def get_salary(self):
#         return 5000
# class PartTimeEmployee(Employee):
#     def get_salary(self):
#         return 3000
# class Intern(Employee):
#     pass
# def print_salary(employee):
#     print(employee.get_salary())
# employees = [FullTimeEmployee(), PartTimeEmployee(), Intern()]
# for employee in employees:
#     print_salary(employee)

# import math
# # Базовый класс Shape
# class Shape:
#     def area(self):
#         """Метод для расчета площади. Должен быть переопределен в дочерних классах."""
#         raise NotImplementedError("Метод area() должен быть переопределен в дочерних классах")
# # Дочерний класс Circle
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         """Переопределение метода для расчета площади круга."""
#         return math.pi * self.radius ** 2
# # Дочерний класс Rectangle
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         """Переопределение метода для расчета площади прямоугольника."""
#         return self.width * self.height
# # Использование полиморфизма для работы с объектами разных классов
# shapes = [
#     Circle(5),        # Создание круга с радиусом 5
#     Rectangle(4, 6),  # Создание прямоугольника со сторонами 4 и 6
#     Circle(3),        # Создание круга с радиусом 3
#     Rectangle(2, 7)   # Создание прямоугольника со сторонами 2 и 7
# ]
# # Вычисление и вывод площадей всех фигур
# for shape in shapes:
#     print(f"Площадь {shape.__class__.__name__}: {shape.area():.2f}")

#
# # Определяем первый декоратор
# def decorator1(func):
#     def wrapper(*args, **kwargs):
#         print("Вызов decorator1: перед выполнением функции.")
#         result = func(*args, **kwargs)
#         print("Вызов decorator1: после выполнения функции.")
#         return result
#     return wrapper
# # Определяем второй декоратор
# def decorator2(func):
#     def wrapper(*args, **kwargs):
#         print("Вызов decorator2: перед выполнением функции.")
#         result = func(*args, **kwargs)
#         print("Вызов decorator2: после выполнения функции.")
#         return result
#     return wrapper
# # Применяем декораторы к функции
# @decorator1
# @decorator2
# def say_hello():
#     print("Привет! Я функция say_hello.")
# # Вызов функции
# say_hello()
