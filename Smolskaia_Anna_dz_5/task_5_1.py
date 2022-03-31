"""
Task 1
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
"""


def numbers_range(n):
    for i in range(1, n + 1, 2):
        yield i
a = numbers_range(5)

print(next(a))
print(next(a))
print(next(a))


