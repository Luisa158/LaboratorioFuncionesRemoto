
def perfect_number (a):
    suma=0
    for i in range (1,a):
        if a%i==0:
            d=i
            print(i)
            suma=suma+d

    if suma==a:
        print("Is a perfect number")

    else:
        print("Is NOT a perfect number")


a=int(input("Ingrese un numero: "))
perfect_number(a)