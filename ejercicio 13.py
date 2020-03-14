# De binario a entero.

binary=input("-")
total=0
for c in binary:
    total *= 2
    c = int(c)
    total += c
print(total)