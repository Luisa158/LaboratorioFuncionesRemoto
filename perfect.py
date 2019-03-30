
def perfect_number (a):
    suma=0
    for i in range (1,a):
        if a%i==0:
            d=i
            print(i)
            suma=suma+d
            res=suma-a

    if res<=a:
        print(a, "Is a almost-perfect number")

    else:
        print("Is NOT a almost-perfect number")


a=int(input("Ingrese un numero: "))
perfect_number(a)