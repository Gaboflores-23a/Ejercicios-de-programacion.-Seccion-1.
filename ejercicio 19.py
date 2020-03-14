# Determinar si la division es exacta o no. 

A=int(input("Dividendo:"))
B=int(input("Divisor:"))
cuociente=A//B
resto=A % B
if resto==0:
    print("la division es exacta")
else:
    print("la division no es exacta")
print("cuociente:",cuociente)
print("resto:",resto)

