"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
algoritmo general.
"""

#funcion de potencia con recursividad.
def potencia(b,e):
    #condicion base todo numero elevado a 0 es igual a 1
    if e == 0:
        return 1
    #en caso contrario multiplica la base por base, restando un exponente
    else:
        return b * potencia(b, e-1)
    
#solicitamos al usuario que ingrese base y exponente
base = int(input("ingrese base: "))
exp = int(input("ingrese exponente: "))

#guardamos el resultado de la funcion potencia en la variable resultado
resultado = potencia(base, exp)

#se muestra en pantalla el resultado
print(f"{resultado}")
    
