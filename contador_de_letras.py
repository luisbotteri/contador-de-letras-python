# Paso 1: solicitar la entrada al usuario.
print("¡Bienvenido/a al contador de letras!")
nombre = input("Por favor, primeramente ingrese su nombre: ")
print(f"Hola, {nombre}! :D")

# Paso 2: contar la cantidad de letras de la palabra ingresada.
while True:
    palabra_ingresada = input("Por favor, ingrese la palabra deseada: ").strip()
    if not palabra_ingresada:
        print("Debes ingresar una palabra.")
        continue

# Paso 3: mostrar el resultado al usuario.
    cantidad_de_letras = len(palabra_ingresada)
    print(f"La palabra '{palabra_ingresada}' contiene {cantidad_de_letras} letras.")

# Paso 4: preguntar al usuario si desea utilizar nuevamente la herramienta.
    continuar = input("¿Deseas ingresar una nueva palabra? Sí/No: ").strip().lower()
    if continuar != "sí":
        print("Gracias por utilizar esta herramienta. ¡Te deseo lo mejor!")
        break