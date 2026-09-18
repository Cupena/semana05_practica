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
            while True:
                    try:
                        cif_estudiante = int(input("Ingrese CIF del estudiante: "))
                        break
                    except ValueError:
                        error()
                    print("Entrada inválida. Debe ser un número.")

            mostrarDatos.mostrar_datos(estudiantes)

        elif opcion == 3:
             separador()
             break

        else:
            error()
    except ValueError:
        error()
        