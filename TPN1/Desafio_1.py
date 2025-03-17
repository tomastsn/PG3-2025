def dibujar_rectangulo(ancho, alto, caracter):
    for _ in range(alto):
        print((caracter + " ") * ancho)  

def dibujar_triangulo(altura, caracter):
    for i in range(1, altura + 1):
        print((caracter + " ") * i) 


def main():
    print("Elija la figura a dibujar:")
    print("1. Rectángulo")
    print("2. Triángulo")
    
    opcion = input("Ingrese el número de la opción: ")

    caracter = input("Ingrese el carácter a utilizar: ")

    if opcion == "1":
        ancho = int(input("Ingrese el ancho del rectángulo: "))
        alto = int(input("Ingrese el alto del rectángulo: "))
        dibujar_rectangulo(ancho, alto, caracter)
    
    elif opcion == "2":
        altura = int(input("Ingrese la altura del triángulo: "))
        dibujar_triangulo(altura, caracter)
    
    else:
        print("Opción inválida. Intente nuevamente.")

main()
