matriz = []

# Procedimiento para capturar datos por consola y agregarlos a la matriz
def registrar(matriz_destino):
    nombre = input("Nombre: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    matriz_destino.append([nombre, [n1, n2, n3]])

# Procedimiento para imprimir
def mostrar(estudiante):
    nombre = estudiante[0]
    notas = estudiante[1]
    promedio = sum(notas) / len(notas)
    print(f"Estudiante: {nombre} | Notas: {notas} | Promedio: {promedio:.2f}")

# Registro de 2 estudiantes en bruto (sin while ni if)
print("--- Registro 1 ---")
registrar(matriz)

print("--- Registro 2 ---")
registrar(matriz)

# Mostrar resultados
print("\n--- Resultados ---")
mostrar(matriz[0])
mostrar(matriz[1])