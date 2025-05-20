"""
4) Crear una función recursiva en Python que reciba 
un número entero positivo en base decimal y devuelva 
su representación en binario como una cadena de texto.
"""
#funcion para convertir decimal a binario y pasarlo a string
def conversor(num):
    #si el cociente es 0 , almacena "0" 
    if num == 0:
        return "0"
    #si el cociente es "1" , almacena "1" 
    elif num == 1:
        return "1"
    else:
        return conversor(num // 2) + str(num % 2)    

#solicitamos el numero decimal,se guarda en num_decimal
num_decimal = int(input("ingrese numero decimal: "))

#el resultado de la recursividad lo almacenamos en decimal_binario
decimal_binario = conversor(num_decimal)

#se muestra en pantalla el resultado de la conversion
print(decimal_binario)
