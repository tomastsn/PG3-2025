def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in frase if letra in vocales)


frase = input("Ingrese una frase: ")
cantidad_vocales = contar_vocales(frase)

print(f"La cantidad de vocales en la frase es: {cantidad_vocales}")
