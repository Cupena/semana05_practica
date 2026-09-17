def mostrar_datos(datos):
    if not datos:
        print("No hay estudiantes registrados.")
        return

    print("Datos de los estudiantes:")
    for alumno in datos:
        nombre = alumno[0]
        notas = alumno[1]

        promedio = sum(notas) / len(notas)