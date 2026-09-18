aprobado = "Aprobado"
reprobado = "Reprobado"

def evaluar_Rendimiento(promedio):
    if promedio >= 90:
        return "APRENDIZAJE AVANZADO"
    elif promedio >= 80:
        return "APRENDIZAJE SATISFACTORIO" 
    elif promedio >= 70:
        return "APRENDIZAJE FUNDAMENTAL" 
    else:
        return "APRENDIZAJE INICIAL" 

def evaluar_condicion(promedio):
    if promedio >= 70:
        return aprobado
    else:
        return reprobado
    
def describir_resultado(promedio):
    if promedio >= 90:
        descripcion = "Dominio sobresaliente: evidencia manejo excepcional de las capacidades, con aplicación innovadora y transferencia creativa del conocimiento."
    elif promedio >= 80:
        descripcion = "Dominio adecuado: aplica habilidades y conocimientos de manera integrada en situaciones reales, cumpliendo con los criterios establecidos."
    elif promedio >= 70:
        descripcion = "Dominio básico: demuestra comprensión fundamental de conceptos y habilidades, aunque con limitaciones en su integración y aplicación contextual."
    else:
        descripcion = "Dominio limitado o en desarrollo: evidencia habilidades y destrezas mínimas o parciales, con dificultad para aplicarlas en contextos reales."
    return descripcion