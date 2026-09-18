import calculo, evaluacion, registro, mostrarDatos, os, time

estudiantes = []

def menu():
    print("1. Ingresar estudiante")
    print("2. Ingresar nota")
    print("3. Evaluar nota")
    print("4. Mostrar estado")
    print("5. Salir")

def error():
    print("Ingrese un valor valido.")

def separador():
    print("--------------------------------------------------")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu())

while True:
    try:
        print(menu())
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
                    ingresar_nota = int(input("Ingrese nota: "))
                    break
                except ValueError:
                    error()
                    print("Ingresar estudiante: ")
            #2 Ingresar nota

        elif opcion == 3:
            while True:
                    try:
                        cif_estudiante = int(input("Ingrese CIF del estudiante: "))
                        break
                    except ValueError:
                        error()
                    print("Entrada inválida. Debe ser un número.")

            mostrarDatos.mostrar_datos(estudiantes)


        elif opcion == 4:
           while True:
                           try:
                               cif_estudiante = int(input("Ingrese CIF del estudiante: "))
                               break
                           except ValueError:
                               error()
                           print("Entrada inválida. Debe ser un número.")
            #5 salir

        else:
            error()
    except ValueError:
        error()
        