n = int(input("Ingresa un número entero positivo: "))
sumpares = 0
sumimpares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sumpares += i
    else:
        sumimpares += i

print(f"Suma de pares: {sumpares}")
print(f"Suma de impares: {sumimpares}")
