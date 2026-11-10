#Sesión 4 — Estructuras de control iterativas (A.1.2)

 #   Bucles while y for, range(), break/continue.
 #   Práctica: menú repetitivo que permite introducir varios movimientos hasta salir.
 #   Producto: 04_bucles.py.


print("=== Registro de compras y ventas ===")

compras = 0.0
ventas = 0.0

continuar = True
while continuar:
    concepto = input(" Concepto (compras-ventas) (o 'fin' para terminar): ")

    if concepto.lower() == "fin" :
        break

    importe = float(input("Importe (EUR):"))
    if importe == 0:
        print("Importe 0 ignorado")
        continue

    if concepto.lower() == "ventas":
        ventas += importe

    if concepto.lower() == "compras":
            compras += importe

    print(f"Movimiento guardado; {concepto} ({importe:.2f} EUR)\n")



print("\n--- Resumen final ---")
print(f"Total compras: {compras:.2f} EUR")
print(f"Total vemtas: {ventas:.2f} EUR")
print(f"Diferencia (ventas-compras): {ventas - compras:.2f} EUR")
