numero = input("Ingresa un número entero: ")
invertido = ""

i = len(numero) - 1
while i >= 0:
    invertido += numero[i]
    i -= 1

print(f"Número invertido: {invertido}")
