año_a_buscar = int(input("Ingrese cualquier año: "))

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
    
if es_bisiesto(año_a_buscar) == True:
    print(f"{año_a_buscar} es bisiesto")
else:
    print(f"{año_a_buscar} no es bisiesto")