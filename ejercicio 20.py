# La palabra mas larga.

N=str(input("palabra 1:"))
S=str(input("palabra 2:"))
C1=0
C2=0
for i in N:
    if (i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U" or i=="b" or i=="B" or i=="c" or i=="C" or i=="d" or i=="D" or i=="f" or i=="F" or i=="g" or i=="G" or i=="h" or i=="H" or i=="j" or i=="J" or i=="k" or i=="K" or i=="l" or i=="L" or i=="m" or i=="M" or i=="ñ" or i=="Ñ" or i=="n" or i=="N" or i=="p" or i=="P" or i=="q" or i=="Q" or i=="r" or i=="R" or i=="s" or i=="S" or i=="t" or i=="T" or i=="v" or i=="V" or i=="w" or i=="W" or i=="x" or i=="X" or i=="y" or i=="Y" or i=="z" or i=="Z"):
        C1 += 1
for i in S:
    if (i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U" or i=="b" or i=="B" or i=="c" or i=="C" or i=="d" or i=="D" or i=="f" or i=="F" or i=="g" or i=="G" or i=="h" or i=="H" or i=="j" or i=="J" or i=="k" or i=="K" or i=="l" or i=="L" or i=="m" or i=="M" or i=="ñ" or i=="Ñ" or i=="n" or i=="N" or i=="p" or i=="P" or i=="q" or i=="Q" or i=="r" or i=="R" or i=="s" or i=="S" or i=="t" or i=="T" or i=="v" or i=="V" or i=="w" or i=="W" or i=="x" or i=="X" or i=="y" or i=="Y" or i=="z" or i=="Z"):
        C2 += 1
H=C1-C2
h=C2-C1
if (C1>C2):
    print("La palabra",N,"tiene",H,"letras mas que",S)
elif (C1<C2):
    print("La palabra",S,"tiene",h,"letras mas que",N)
if (C1==C2):
    print("Las dos palabras tienen el mismo largo")

