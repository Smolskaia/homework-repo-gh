"""
Генерация карточек для игры ЛОТО
"""


import random


# Класс карточки игрока
class Cart:
    # Задаем длину списка при создании карточки (по умолчанию = 90)
    def __init__(self, length=90):
        self.lst = [x for x in range(1, length + 1)]
        self.fifteen = []
        self.health = 15  # Длина списка билетов
        self._get_fifteen_items()
        self.original_line = [x for x in range(9)]
        self.lines = self._sort_random(self.original_line.copy())



    # Метод создания списка из случайных 15 элементов
    def _get_fifteen_items(self):
        try:
            five = []
            copy_list = self.lst.copy()
            for x in range(1, 4):
                for y in range(1, 6):
                    idx = random.randrange(0, len(copy_list))
                    five.append(copy_list[idx])
                    copy_list.pop(idx)
                five.sort()
                self.fifteen.append(five.copy())
                five.clear()
            return self.fifteen
        except ValueError:
            return "Список меньше чем вы думаете. Не мучайте его."

    # Метод рандомной сортировки для строки
    def _sort_random(self, lst):
        lines = []
        for x in range(3):
            for _ in range(10):
                x1 = random.randint(0, 8)
                x2 = random.randint(0, 8)
                if x1 != x2:
                    lst[x1], lst[x2] = lst[x2], lst[x1]
            lines.append(lst.copy())
        return lines

 # Метод вывода принадлежности карточки игрока
    def _print_name_cart(self):
        print('---------- Ваша карточка ----------')

    # Метод вывода карточки игрока
    def print_cart(self):
        self._print_name_cart()
        # прогоняем на печать три строки карточки
        for x in range(3):
            line = ''
            y = 0
            for j, el in enumerate(self.lines[x]):
                if el == 5 or el == 6 or el == 7 or el == 8:
                    line += ''.rjust(2)
                else:
                    line += str(self.fifteen[x][y]).rjust(2)
                    y += 1
                if j < len(self.lines[x]) - 1:
                    line += ''.rjust(2)
            print(line)
        print('-----------------------------------')


# Класс карточки компьютера с уникальным методом
class CartComp(Cart):
    # Переопределяем метод вывода принадлежности карточки компьютера
    def _print_name_cart(self):
        print('------- Карточка компьютера--------')

# Класс запуска Игры, печать карточек игрока и компьютера
class Game:
    def __init__(self, human, comp):
        self.human = human
        self.comp = comp

    def print_game(self):
        self.human.print_cart()
        self.comp.print_cart()

# Определяем экземпляры классов
my_cart = Cart()
cart_comp = CartComp()
game = Game(my_cart, cart_comp)

# Запускаем Игру
game.print_game()






