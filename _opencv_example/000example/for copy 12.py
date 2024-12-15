original="""By dawn on June 6, thousands of paratroopers and glider
troops were already on the ground behind enemy lines, securing bridges
and exit roads. The amphibious invasions began at 6:30 a.m."""
print('===== The original sentence =====');print(original)
ciphered=''
for ch in original:
    if ch.isalpha():
        if ch.isupper():
            x = ord('z') - (ord(ch.lower()) - ord('a'))
            ch = chr(x).upper()
        else:
            x = ord('z') - (ord(ch) - ord('a'))
            ch = chr(x)
    elif ch.isdigit():
        x = ord('9') - (ord(ch) - ord('0'))
        ch = chr(x)        
    ciphered += ch

print('===== The ciphered sentence ====='); print(ciphered)

deciphered=''
for ch in ciphered:
    if ch.isalpha():
        if ch.isupper():
            x = ord('z') - (ord(ch.lower()) - ord('a'))
            ch = chr(x).upper()
        else:
            x = ord('z') - (ord(ch) - ord('a'))
            ch = chr(x)
    elif ch.isdigit():
        x = ord('9') - (ord(ch) - ord('0'))
        ch = chr(x)        
    deciphered += ch
print('===== The deciphered sentence ====='); print(deciphered)