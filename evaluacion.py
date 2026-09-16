# Módulo de evaluación a calificaciones

def evaluar_Nota(nota):
    if nota >= 70:
        print(f"{nota} - Aprobado")
    else:
        print(f"{nota} - Reprobado")

def evaluar_Rendimeinto(promedio):
    if promedio >= 90 and promedio <= 100:
        print("APRENDIZAJE AVANZADO" \
        "Dominio sobresaliente: evidencia manejo excepcional de las capacidades, con aplicación innnovadora y transferencia creativa del conocimiento.")
    elif promedio >= 80 and promedio <= 86:
        print("APRENDIZAJE SATISFACTORIO" \
        "Dominio adecuado: aplica habilidades y conocimientos de manera integrada en situaciones reales, cumpliendo con los criterios establecidos.")
    elif promedio >=70 and promedio <= 79:
        print("APRENDIZAJE FUNDAMENTAL" \
        "Dominio básico: demuestra comprensión fundamental de conceptos y habilidades, aunque con limitaciones en su integración y aplicación contextual.")
    elif promedio <= 69:
        print("APRENDIZAJE INICIAL" \
        "Dominio limitado o en desarrollo: evidencia habilidades y destrezas mínimas o parciales, con dificultad para aplicarlas en contextos reales.")


''' 
Ingresar los datos del estudiante.
Luis: Registrar diferentes calificaciones.
Rebeca: Calcular el promedio.
Belén: Determinar si el estudiante aprueba o reprueba - LISTO.
Belén: Identificar diferentes rangos de rendimiento.
Luis: Mostrar una recomendación según el resultado.
Rebeca: Validar que las calificaciones estén dentro del rango permitido. 
'''