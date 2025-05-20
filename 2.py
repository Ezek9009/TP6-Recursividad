"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique.
"""
def fibonacci(num1):
    #caso base
    if num1 == 0:
        return 0
    elif num1 == 1:
        return 1
    #de lo contrario devuelve la funcion con el numero -1 y el numero -2
    else:
        return fibonacci(num1 -1) + fibonacci(num1 -2)
    
#solicitamos que el usuario ingrese un numero:
num1 = int(input("ingrese un numero: "))

#se muestra en pantalla los numeros de la serie
for i in range(num1+1):
    print(f"el numero fibonacci en la posicion {i} es {fibonacci(i)}")
    print(f"{fibonacci(i)}")