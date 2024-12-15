data = "Hello World"
bcc = 0
for c in data:
    bcc ^= ord(c)

print(hex(bcc)[2:])
print(hex(bcc)[2:].zfill(2))
bcc_s = hex(bcc)[2:].zfill(2)

print(data+bcc_s)