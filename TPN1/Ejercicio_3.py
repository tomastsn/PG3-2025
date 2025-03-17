ancho = int(input("Ingrese el ancho del rectangulo: "))
alto = int(input("Ingrese el alto del rectangulo: "))
caracter = input("Ingrese el caracter: ")

print("Pedido:")
print(f"Ancho: {ancho}")
print(f"Largo: {alto}")
print(f"Caracter: {caracter}")
print("Imprime:")

for i in range(alto):
    print((caracter + " ") * ancho)

