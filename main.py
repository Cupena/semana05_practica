import calculo, evaluacion, registro, mostrarDatos

estudiantes = []

def menu():
    print("1. Ingresar estudiante")
    print("2. Ingresar nota")
    print("3. Evaluar nota")
    print("4. Mostrar estado")
    print("5. Salir")

def error():
    print("Ingrese un valor valido.")

while True:
    try:
        opcion = int(input("Ingrese accion a realizar: "))
        if opcion == 1:
            while True:
                try:
                    registro.registrar_datos(estudiantes)
                    break
                except ValueError:
                   error()
   
        elif opcion == 2:
            print("Ingresar estudiante: ")
            #2 Ingresar nota

        elif opcion == 3:
            mostrarDatos.mostrar_datos(estudiantes)

        elif opcion == 4:
            print("Ingresar estudiante: ")
            #4 Mostrar estado

        elif opcion == 5:
            print("Saliendo del programa")
            break
            #5 salir

        else:
            error()
    except ValueError:
        error()
        ola