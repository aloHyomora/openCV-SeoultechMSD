desserts= ['요거트','아이샌드', '컵케이크', '생강빵']
contents=['칼로리', '지방', '탄수화물', '단백질']
numbers=[[159.,6.,24.,4.], [237.,9.,37.,4.3],
	 [305.,3.7,67.,3.9], [356.,16.,49.,0.0]]

print("디저트\t\t", end="")
for c in contents:
    print(f"{c}\t\t", end="")
print()
for i,d in enumerate(desserts):
    print(f"{d}\t\t",end="")
    for j,c in enumerate(contents):
        print(f"{numbers[i][j]}\t\t",end="")
    print()
        
#dic ={ d: { c:numbers[i][j] for j, c in enumerate(contents)}  for i, d in enumerate(desserts)}
# print(dic)
dic2 = {(d,c):numbers[i][j] for j,c in enumerate(contents) for i, d in enumerate(desserts)}
print(dic2)