##Modulo de registro de notas y estudiantes

datos = []
def registrar_datos(datos):
    def error():
        print("Ingrese  ")
    estudiante = input("Nombre de estudiante: ")
    try:
        nota1 = int(input("Ingrese la nota 1:"))
    except ValueError:

    nota2 = int(input("Ingrese la nota 2:"))
    nota3 = int(input("Ingrese la nota 3:"))
    datos.append([estudiante, [nota1, nota2, nota3]])

registrar_datos(datos)

