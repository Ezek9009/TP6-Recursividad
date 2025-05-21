"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide. 
 
      Ejemplos: 
contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1)
"""

def contar_bloques(n):
    #caso base
    if n == 1:
        return n
    else:
    #retorna el valor de n sumado al numero -1
        return n + (contar_bloques(n-1))

#se ingresa un numero por teclado1    
n = int(input("ingrese un numero: "))

#se muestra en pantalla el resultado de la piramide
print(contar_bloques(n))