"""  Sesión 5 — Práctica integradora "mini-retos"

 Retos progresivos que combinan condicionales y bucles (validación de datos, menús).
 Producto: 05_retos.py. """

# 1ºer reto: Comprobar si alguien es mayor de edad (Validación de datos)

edad = int(input("Introduce tu edad: "))

while edad < 0:
    print("Edad no válida.")
    edad = int(input("Introduce tu edad de nuevo: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


#2º reto: Hacer el menú de una calculadora (Menú)
print("------Calculadora-------")

while True:
   opcion = input("Elige una opción (1-sumar, 2-restar, 3-multiplicar, 4-dividir) o 'fin' para salir: ").lower() 
   if opcion == "fin":
        break
   
   opcion = int(opcion)

   if opcion == 1:
    print("Has elegido sumar.")
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    resultado = numero1 + numero2
    print(f"El resultado es {resultado}")

   elif opcion == 2:
    print("Has elegido restar.")
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    resultado = numero1 - numero2
    print(f"El resultado es {resultado}")

   elif opcion == 3:
    print("Has elegido multiplicar.")
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    resultado = numero1 * numero2
    print(f"El resultado es {resultado}")

   elif opcion == 4:
    print("Has elegido dividir.")
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    if numero2 == 0:
       print("No se puede dividir entre 0")
    else:
        resultado = numero1 / numero2
        print(f"El resultado es {resultado}")
   
   else:
    print("Opción no válida.")


