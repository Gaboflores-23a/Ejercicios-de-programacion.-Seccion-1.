# Numeros enteros de 3 digitos en orden inverso.

N=int(input("ingrese un numero de 3 digitos:"))
centena=N//100
decena=(N % 100)//10
unidad=(N % 100) % 10
print("%d%d%d"%(unidad,decena,centena))

      