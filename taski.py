
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