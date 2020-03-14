A=input("Ingrese un numero:")
B=False
resultado="0,"
for c in A:
    if B==True:
        resultado += c
    if c=="," or c==".":
        B=True
print(resultado)