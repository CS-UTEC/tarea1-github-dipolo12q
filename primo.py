def es_primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True
n =int(input("Ingrese un número: "))
bolean = es_primo(n)
if bolean == True:
    print("El número ingresado es primo")
else:
    print("El número ingresado no es primo")

