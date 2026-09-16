##Modulo de registro de notas y estudiantes

datos = []
def registrar_datos(datos):
    estudiante = input("Nombre de estudiante: ")
    def error():
        print("Ingrese un valor valido")

    while True:
        try:
            nota1 = int(input("Ingrese la nota 1:"))
            break
        except ValueError:
            error()
    while True:
        try:
            nota2 = int(input("Ingrese la nota 2:"))
            break
        except ValueError:
            error()
    while True:
        try:
            nota3 = int(input("Ingrese la nota 3:"))
            break
        except ValueError:
            error()

    datos.append([estudiante, [nota1, nota2, nota3]])
