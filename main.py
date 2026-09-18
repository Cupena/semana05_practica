import calculo, evaluacion, registro, mostrarDatos, os, time

estudiantes = []

def menu():
    print("1. Ingresar informacion del estudiante")
    print("2. Mostrar estado")
    print("3. Salir")

def error():
    print("Ingrese un valor valido.")

def separador():
    print("--------------------------------------------------")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:
        menu()
        opcion = int(input("Ingrese accion a realizar: "))

        if opcion == 1:
            while True:
                try:
                    registro.registrar_datos(estudiantes)
                    separador()
                    break
                except ValueError:
                   error()

        elif opcion == 2:
            mostrarDatos.mostrar_datos(estudiantes)
            input("\nPresione Enter para continuar...")
            separador()
            break

        elif opcion == 3:
             separador()
             break

        else:
            error()
            separador()

    except ValueError:
        error()
        