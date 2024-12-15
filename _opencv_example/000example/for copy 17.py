beverage=['사과 주스', '아메리카노', '카페라떼','밀크티','소금빵']
price=[6000,3500,4500,4000,2000]
menu = {b:p for b, p in zip(beverage, price)}
print(menu)

order = [1,2,0,1,5]
orderdic = {m:o for m, o in zip(beverage, order)}
print(orderdic)

total = 0
for i, q in orderdic.items():
    if q != 0:
        total += menu[i]*q
        print(f' {i}: {q}    {menu[i]*q}')
        
print("===Total===")
print(f' {total}')