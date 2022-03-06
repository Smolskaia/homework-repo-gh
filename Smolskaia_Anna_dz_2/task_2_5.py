# task_2_5

goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.05, 50.98, 9077, 1]
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой



goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.5, 50.98, 9077, 1]
print(id(goods))
goods.sort()
print(id(goods))
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой


goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.5, 50.98, 9077, 1, 23.7]
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой

# one line
print([f'{int(good)} руб {(good - int(good)) * 100:02.0f} коп' for good in sorted(goods)[::-1][:5]])

