# task_1_3
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# ...
# 100 процентов

percent = int(input('Введите число процента: '))
if percent == 1:
    word = 'процент'
elif percent == 21:
        word = 'процент'
elif percent == 31:
        word = 'процент'
elif percent == 41:
        word = 'процент'
elif percent == 51:
        word = 'процент'
elif percent == 61:
        word = 'процент'
elif percent == 71:
        word = 'процент'
elif percent == 81:
        word = 'процент'
elif percent == 91:
        word = 'процент'
elif 2 <= percent <= 4:
    word = 'процента'
elif 22 <= percent <= 24:
    word = 'процента'
elif 32 <= percent <= 34:
    word = 'процента'
elif 42 <= percent <= 44:
    word = 'процента'
elif 52 <= percent <= 54:
    word = 'процента'
elif 62 <= percent <= 64:
    word = 'процента'
elif 72 <= percent <= 74:
    word = 'процента'
elif 82 <= percent <= 84:
    word = 'процента'
elif 92 <= percent <= 94:
    word = 'процента'
else:
    word = 'процентов'
print(percent, word)

