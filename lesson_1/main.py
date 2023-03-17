# Подсчет символов в строке

s = input('Введите строку: ')
dct = {}
anscnt = 0
ans = ''
for sym in s:
    if sym not in dct:
        dct[sym] = 0
    dct[sym] += 1

    if dct[sym] > anscnt:
        anscnt = dct[sym]
        ans = sym

print('Чаще всего встречалась буква {letter}.\nКол-во вхождений: {count}'.format(
    letter=ans, count=anscnt
))
