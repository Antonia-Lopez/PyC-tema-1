"""Sesión 2 — Operadores y expresiones aplicados (A.1.1)

Cálculo de porcentajes, redondeos, conversión de tipos, errores comunes.
Práctica: "Registro de un movimiento" (concepto, importe, cálculo del IVA/descuento).
Producto: 02_expresiones.py."""

IVA = 0.21                  #21 % de IVA (constante)
DESCUENTO = 0.10            #10 % de descuento
print("=== Registro de un movimiento ===")

concepto = input("Concepto de movimiento: ")
importe_bruto = float(input("Importe bruto (EUR): "))
aplica_descuento = input("¿Aplica descuento? (s/n)").lower() == "s"

importe_iva = importe_bruto * IVA
importe_total = importe_bruto + importe_iva

print(f"Importe IVA: {importe_iva:.2f} €")
print(f"Importe total: {importe_total:.2f} €")