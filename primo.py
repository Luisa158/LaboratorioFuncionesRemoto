
def is_prime(a):
    contador=0
    for i in range (2,a+1):
        if a % i == 0:
            contador+=1
            print("Divider: ", i)

    if contador > 2:
        no_prime=0
        return no_prime

    else:
        prime=1
        return prime


while True:
    try:
        a = int(input("Por favor, introduca el número a evaluar: "))
        if a==0:
            break
        if a<0:
            break
        if a==1:
            print(0)

        res=is_prime(a)
        if res==0:
            print(0)
        else:
            res==1
            print(1)
    except:
        print(-1)
        print("Hay un ERROR!!")









