# Años bisiestos.

N=int(input("Ingrese un año:"))
if (N>1582 and (N % 100)==0):
    if (N % 400)==0:
        print(N,"es bisiesto")
    else:
        print(N,"no es bisiesto")
elif (N<=1582 and (N % 4)==0):
    print(N,"es bisiesto")
else:
    print(N,"no es bisiesto")

    