"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
      Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4
contar_digito(123456, 7)     → 0
"""

def contar_digito(numero, digito):
    #caso base: si el numero es 0, no quedan mas digitos por revisar.
    if numero == 0:
        return 0
    #verificar si el ultimo digito es igual al buscado
    coincidencia = 1 if numero % 10 == digito else 0

    #llamada recursiva con el numero sin el ultimo digito
    return coincidencia + contar_digito(numero // 10, digito)

numero = int(input("ingrese un numero: "))
digito = int(input("ingrese digito a buscar: "))

print(contar_digito(numero, digito))