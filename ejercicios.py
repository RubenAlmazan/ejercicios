#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

"""def max(uno, dos):
    if(uno > dos):
        return uno
    elif(dos > uno):
        return dos
    elif(uno == dos):
        return 'Los numeros son iguales'
    else:
        return 'Ocurrio un error, Intentelo de nuevo'
    
print(max(1, 2))"""

#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

"""def max_de_tres(uno, dos, tres):
    lista = (uno, dos, tres)
    valor = max(lista)
    
    elemento = lista.count(valor)
    if(elemento > 1):
        return f"Hay más de un elemento máximo con el valor {valor}."
    else:
        return valor
    
print(max_de_tres(1022, 102, 102))"""

#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

"""def vocal(elemento):
    valores = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    
    for i in valores:
        if(i == elemento):
            return f"El valor {elemento} es vocal."
            break
    
    return f"El valor {elemento} NO es vocal."
        
print(vocal('A'))"""
    
#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

"""def sum(lista):
    
    valor = 0
    for i in lista:
        valor += i
    
    return valor

def multi(lista):
    valor = 1
    for i in lista:
        valor *= i
    
    return valor

lista = [1, 2, 3, 4]
print(sum(lista))
print(multi(lista))"""

#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

"""def inversa(texto):
    texto = texto[::-1]
    return texto

print(inversa('estoy probando'))"""

#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

"""def es_palindromo(texto):
    inverso = texto[::-1]
    if(inverso == texto):
        return 'Es palindromo'
    else:
        return 'No es palindromo, es un texto normal'

print(es_palindromo('ommo'))"""

#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

"""def superposicion(lista1, lista2):
    for i in lista1:
        if i in lista2:
            return True
        
    return False
    
lista1 = [1, 2, 3, 22]
lista2 = [11, 22, 32]
print(superposicion(lista1, lista2))"""

#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

"""def generar_n_caracteres(entero, letra):
    
    orden = letra
    for i in range(0, entero):
        orden += letra
    
    return orden

print(generar_n_caracteres(14, 'R'))"""

#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

"""def procedimiento(lista):
    
    for i in lista:
        
        a = 0
        while a < i:
            print('*', end='')
            a += 1
            
        print('\n')

lista = [15, 14, 27]
procedimiento(lista)"""

# Ejercicio de idea Turing 

"""palabra = 'ru-ben-alma-zan'
lista = palabra[::-1].replace('-', '')

print(palabra)
print('->')

base = []
a=0

for i in palabra:
    if(i != '-'):
        base.append(lista[a])
        a+=1
    else:
        base.append(i)

result = ''.join(base)
print(result)"""

