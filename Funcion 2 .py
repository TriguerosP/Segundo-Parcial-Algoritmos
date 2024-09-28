def calcular_superficie(lado1, lado2):
    return lado1 * lado2

# Bloque principal
lado1_rect1 = float(input("Ingrese el lado 1 del primer rectángulo: "))
lado2_rect1 = float(input("Ingrese el lado 2 del primer rectángulo: "))
lado1_rect2 = float(input("Ingrese el lado 1 del segundo rectángulo: "))
lado2_rect2 = float(input("Ingrese el lado 2 del segundo rectángulo: "))

superficie_rect1 = calcular_superficie(lado1_rect1, lado2_rect1)
superficie_rect2 = calcular_superficie(lado1_rect2, lado2_rect2)

if superficie_rect1 > superficie_rect2:
    print("El primer rectángulo tiene mayor superficie.")
elif superficie_rect1 < superficie_rect2:
    print("El segundo rectángulo tiene mayor superficie.")
else:
    print("Ambos rectángulos tienen la misma superficie.")
