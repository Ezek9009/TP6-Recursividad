"""
5) Implementá una función recursiva llamada es_palindromo(palabra)
que reciba una cadena de texto sin espacios ni tildes, 
y devuelva True si es un palíndromo o False si no 
lo es.Requisitos:La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed(). 
"""

def es_palindromo(palabra):
    #caso base: si la palabra tiene 0 o 1 caracteres
    #es un palíndromo

    if len(palabra) <= 1:
        return True
    #si el primer y ultimo caracter son diferentes,
    #no es un palindromo
    if palabra[0] != palabra[-1]:
        return False
    
    #llamada recursiva con la subcadena sin el primer
    #y ultimo caracter
    return es_palindromo(palabra[1:-1])

palabra = input("ingrese una palabra: ")
palindromo = es_palindromo(palabra)

if palindromo:
    print("es palindromo..")
else:
    print("no es palindromo..")