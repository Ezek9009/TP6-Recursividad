"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario
"""

def factorial_num(num1):
    
    if num1 == 1:
        return 1
    else:        
        return  num1 * factorial_num(num1 -1)

num1 = int(input("ingrese un numero: "))

for i in range(1, num1 + 1):
    print(f"factorial de {i}: {factorial_num(i)}")