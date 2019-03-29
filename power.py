
def a_power_b (a,b):
    cont=1
    for i in range (1,b+1):
        cont=cont*a
        if i > 63:
            raise ValueError('El número es muy grande')
            break
    return cont


error = 0
poten = 0
par = 0
impar = 0

while True:
    try:
        a=int(input("Por favor, ingrese el número base: "))

        if a ==0:
            break

        b=int(input("Por favor, ingrese el número de la potencia: "))
        poten=poten+1

        res= a_power_b(a,b)
        print("El resultado es: ", res)
        if res%2==0:
            par=par+1
        else:
            impar=impar+1

    except:
        print("TIENE UN ERROR!!")
        error=error+1


print("El número de potencias calculadas es: ", poten)
print("El número de erroes es: ", error)
print("El número de resultados pares fue: ", par)
print("El número de resultados impares fue: ", impar)



