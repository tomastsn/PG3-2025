def es_palindromo(palabra):
    return palabra == palabra[::-1] 


palabra_elegida = input("Ingrese una palabra: ").lower()  
if es_palindromo(palabra_elegida):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")






