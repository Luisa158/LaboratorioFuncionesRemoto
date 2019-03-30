
a=int(input("Por favor, introduca el número a evaluar: "))


def is_prime(a):
    contador=0
    for i in range (2,a):
        if a % i == 0:
            contador+=1
            print("Divisor: ", i)

    if contador>0:
         print("Is NOT a prime number")

    else:
         print("Is a primer number")

is_prime(a)








