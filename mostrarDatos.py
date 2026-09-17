def mostrar_datos(datos):
    if not datos:
        print("No hay estudiantes registrados.")
        return

    print("Datos de los estudiantes:")
    for alumno in datos:
        nombre = alumno[0]
        notas = alumno[1]

        promedio = sum(notas) / len(notas)
        
        if promedio >= 70:
            condicion = "Aprobado"
            rendimiento = "Medio"
            recomendacion = "Buen trabajo, pero puedes mejorar."
        elif promedio >= 85:
            condicion = "Aprobado"
            rendimiento = "Alto"
            recomendacion = "Excelente trabajo"
        else:
            condicion = "Reprobado"
            rendimiento = "Bajo"
            recomendacion = "Necesitas estudiar más."
            
        print(f"\nEstudiante: {nombre}")
        print(f"Notas: {notas}")
        print(f"Promedio: {promedio:.1f}")
        print(f"Condición: {condicion} ({rendimiento})")
        print(f"Recomendación: {recomendacion}")
        print("-" * 25)