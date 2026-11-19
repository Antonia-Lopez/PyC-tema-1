""" Estructuras de datos I (A.1.2)

    Listas y tuplas: creación, indexación, métodos, mutabilidad.
    Práctica: almacenar una lista de importes y calcular total, media, máximo y mínimo.
    Producto: 06_listas.py.
 """

importes = []

while True:
    entrada = input("Introduce un importe o 'fin' para terminar: ")
    if entrada.lower() == "fin":
        break
    importe = float(entrada)

    importes.append(importe)

if not importes:
    print("No se han introducido importes.")

else:
    total = sum(importes)
    media = total / len(importes)
    maximo = max(importes)
    minimo = min(importes)

    print(f"El total es {total}")
    print(f"La media es {media}")
    print(f"El máximo es {maximo}")
    print(f"El mínimo es {minimo}")
