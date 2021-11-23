categorias = ["Hombres", "Mujeres", "Socios"]
precios = [10500, 8000, 6000]
cantidades = [0,0,0]
totalAPagar = 0

for x in range(3):
    cantidades[x] = int(input(f"Ingrese cantidad de {categorias[x]}: "))

for x in range(3):
    totalAPagar = totalAPagar + (precios[x] * cantidades[x])

print(f"{cantidades[0]} Hombres = {precios[0] * cantidades[0]}")
print(f"{cantidades[1]} Mujeres = {precios[1] * cantidades[1]}")
print(f"{cantidades[2]} Socios  = {precios[2] * cantidades[2]}")
print(f"El total a pagar es de: {totalAPagar}")
