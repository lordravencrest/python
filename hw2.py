#задание №1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 3))

#задание №2
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem [1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_list.append(elem)
out_info = ' '.join(new_list)
print(out_info)

symbol_idxs = []
for idx, letter in enumerate(out_info):
    if letter == '"':
        symbol_idxs.append(idx)

for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] = 1

for del_idx in reversed(symbol_idxs):
    out_info = out_info[:del_idx] + out_info[del_idx+1:]

#задание №4
bad_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй'
            'директор аэлита']
for position in bad_list:
    print('Привет', position.split()[-1].title())

#задание №5
goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.05, 50.98, 9077, 1]
for good in goods:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп ')
goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.05, 50.98, 9077, 1]
print(id(goods))
goods.sort()
print(id(goods))
for good in goods:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп ')
goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.05, 50.98, 9077, 1, 23.7]
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп ')

