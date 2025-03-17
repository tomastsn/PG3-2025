l = []
e = 0

elementos_lista = int(input("Ingresa la cantidad de elementos de la lista: "))

for i in range(elementos_lista):
    e += 1
    n = int(input(f"Ingrese el numero {e}: "))
    l.append(n)


def ordenar_lista(lista):
    return sorted(lista, reverse=True)


lista_ordenada = ordenar_lista(l)
print("Lista original:", l)
print("Lista ordenada de mayor a menor:", lista_ordenada)