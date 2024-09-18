# 
주문 = '마른안주'
메뉴 = {'소주':3000, '맥주':4000, '마른안주':10000, '샐러드':6000}
total = 메뉴.get(주문, 999999)
if total == 999999:
    print('주문 오류!')
else:
    print(total)

# 허리 둘레를 인치로 입력받아 그 값이 27인치 미만은 "small", 27에서 30인치 미만은 "medium", 그리고 30 인치 이상은 "large"라고 출력하는 프로그램을 작성하자.
n = float(input('허리 둘레를 입력하세요.:'))
if n < 27:
    print("small")
elif n < 30:
    print("medium")
elif n >= 30:
    print("large")

# 어떤 주점의 메뉴에서 소주는 3000원, 맥주는 4000원, 마른안주는 10000원, 그리고 샐러드는 6000원일 때 임의의 주문에 대하여 가격을 출력하는 프로그램을 if 문으로 작성하라.
numberOfSoju = int(input('소주 구매 개수: '))
numberOfBeer = int(input('맥주 구매 개수: '))
numberOfSnack = int(input('안주 구매 개수: '))
numberOfSalad = int(input('샐러드 구매 개수: '))

totalPrice = numberOfSoju * 3000 + numberOfBeer * 4000 + numberOfSnack * 10000 + numberOfSalad * 6000
print(f'총 금액은 {totalPrice}입니다.')