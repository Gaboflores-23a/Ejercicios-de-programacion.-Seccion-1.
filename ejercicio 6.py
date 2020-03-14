# Convierta un numero entero positivo en un numero binario.

N=int(input("-"))
if N>0:
    print(N)
dividendo=N
cuociente=0
resto=0
valor="-"
while(dividendo != 0):
    cuociente=dividendo//2
    resto=dividendo % 2
    dividendo=cuociente
    valor += str(resto)
print(valor)