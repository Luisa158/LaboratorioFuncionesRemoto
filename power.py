
a=int(input("Por favor, ingrese el número base: "))
b=int(input("Por favor, ingrese el número de la potencia: "))

def a_power_b (a,b):
    cont=0
    for i in range (1,b+1):
      cont=a*i
    print("El resultado es: ", cont)

a_power_b(a,b)
