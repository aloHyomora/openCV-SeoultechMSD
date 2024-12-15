import numpy as np

menu = {'soju':3000, 'beer':4000, 'dry':10000, 'salad':6000}

print(menu['soju'])

order = input('먹고 싶은 메뉴를 입력')
total = menu.get(order, -1)
if total == -1:
    print('메뉴가 없다.')
else:
    print(total)
print(menu[order])
