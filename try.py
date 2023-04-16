# Calculadora básica en Python

# Función para sumar dos números
def suma(num1, num2):
    return num1 + num2

# Función para restar dos números
def resta(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicacion(num1, num2):
    return num1 * num2

# Función para dividir dos números
def division(num1, num2):
    return num1 / num2

# Función principal que muestra el menú y procesa la entrada del usuario
def calculadora():
    print("Bienvenido a la calculadora básica en Python")
    print("Por favor, seleccione una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Ingrese su opción (1/2/3/4): "))

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        print(num1, "+", num2, "=", suma(num1, num2))

    elif opcion == 2:
        print(num1, "-", num2, "=", resta(num1, num2))

    elif opcion == 3:
        print(num1, "*", num2, "=", multiplicacion(num1, num2))

    elif opcion == 4:
        print(num1, "/", num2, "=", division(num1, num2))

    else:
        print("Opción inválida")

# Llamar a la función principal para iniciar la calculadora
calculadora()
