##Modulo de registro de notas y estudiantes

datos = []
def registrar_datos(datos):
    def error():
        print("Ingrese  ")
    estudiante = input("Nombre de estudiante: ")

    try:
        nota1 = int(input("Ingrese la nota 1:"))
    except ValueError:
        error()
    try:
        nota2 = int(input("Ingrese la nota 2:"))
    except ValueError:
        error()
    try:
        nota3 = int(input("Ingrese la nota 3:"))
    except ValueError:
        error()
    datos.append([estudiante, [nota1, nota2, nota3]])
