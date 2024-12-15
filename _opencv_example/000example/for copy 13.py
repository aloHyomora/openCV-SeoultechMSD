nation = ['kr', 'En', 'Fr', 'DH', 'Kr', 'Co', 'cc', 'eu', 'to', 'cn', 'CH', 'en']
s = {w for w in nation if w.lower().startswith('c')}
print(s)

s1 = {n for n in nation if n[0] in ['c','C']}
print(s1)

tong = []
for w in nation:
    if w.lower().startswith('c'):
        tong.append(w)
print(set(tong))