lista_numeros = [8, 12, 9, 45, 42, 99, 1045]

def buscar_elemento(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)  
    else:
        return -1  


numero_buscado = int(input("Ingrese el número a buscar: "))

indice = buscar_elemento(lista_numeros, numero_buscado)

if indice != -1:
    print(f"El número {numero_buscado} se encuentra en la posición {indice}.")
else:
    print(f"El número {numero_buscado} no está en la lista.")
