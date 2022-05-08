nume_1=int(input("Ingrese el primer numero: "))
nume_2=int(input("Ingrese el segundo numero: "))

if nume_1>nume_2:
    print(str(nume_1)+ " es mayor que "+ str(nume_2))
elif nume_2>nume_1:
    print(str(nume_2)+" es mayor que "+str(nume_1))
else:
    print(str(nume_1)+" y "+str(nume_2)+" son iguales")
    