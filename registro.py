##Modulo de registro de notas y estudiantes
datos = []
def registrar_datos(datos):
    estudiante = input("Nombre de estudiante: ")
    def error():
        print("Ingrese un valor valido.")

    while True:
        try:
            nota1 = int(input("Ingrese la nota 1: "))
            if nota1 < 0 or nota1 > 100:
                error()
            else:
                break
        except ValueError:
            error()
    while True:
        try:
            nota2 = int(input("\nIngrese la nota 2: "))
            if nota2 < 0 or nota2 > 100:
                error()
            else:
                break
        except ValueError:
            error()
    while True:
        try:
            nota3 = int(input("\nIngrese la nota 3: "))
            if nota3 < 0 or nota3 > 100:
                error()
            else: 
                break
        except ValueError:
            error()

    datos.append([estudiante, [nota1, nota2, nota3]])
