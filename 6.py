"""
Escribí una función recursiva en Python llamada suma_digitos(n)
 que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
     Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5)
"""

def suma_digitos(n):
    #caso base: si n es menor que 10
    if n < 10:
        return n
    #obtener el ultimo digito con el operador modulo (%) y sumarlo a la recursion
    return n % 10 + suma_digitos(n // 10)

n = int(input("ingrese un numero: "))
print(suma_digitos(n))
    

