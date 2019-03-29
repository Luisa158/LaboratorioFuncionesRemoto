
def a_power_b (a,b):
    cont=1
    for i in range (1,b+1):
        cont=cont*a
        if i > 63:
            raise ValueError('El número es muy grande')
            break
    return cont


while True:
    try:
        a=int(input("Por favor, ingrese el número base: "))

        if a ==0:
            break

        b=int(input("Por favor, ingrese el número de la potencia: "))

        res= a_power_b(a,b)
        print("El resultado es: ", res)

    except:
        print("TIENE UN ERROR!!")
    

