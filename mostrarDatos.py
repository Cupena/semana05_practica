import evaluacion, calculo
#Traslado main
def mostrar_datos(datos):
    if not datos:
        print("No hay estudiantes registrados.")
        return
    
    print("Datos de los estudiantes:")
    for alumno in datos:
        nombre = alumno[0]
        notas = alumno[1]

        promedio = calculo.averagescore(notas)
        condicion = evaluacion.evaluar_condicion(promedio)
        rendimiento = evaluacion.evaluar_Rendimiento(promedio)
        descripcion = evaluacion.describir_resultado(promedio)

            
        print(f"\nEstudiante: {nombre}")
        print(f"Notas: {notas}")
        print(f"Promedio: {promedio:.1f}")
        print(f"Condición: {condicion} ({rendimiento})")
        print(f"Descripcion: {descripcion}")
#
