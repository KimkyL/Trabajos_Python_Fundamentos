#Este código simula un sistema básico de gestión de tareas que permite a los usuarios agregar, mostrar, completar y eliminar tareas. 
tareas = []

def agregar_tarea(titulo, descripcion, fecha_limite):
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,  # Error: acento en "fecha_límite"
        "completado": False
    }
    tareas.append(tarea)  # Error: se debería agregar 'tarea', no 'tareas'

def mostrar_tareas():
    if len(tareas) == 0:  # Error: se debe usar '==', no '='
        print("No hay tareas pendientes.")
    else:
        for indice in range(len(tareas)):  # Error: el índice debería empezar en 0
            tarea = tareas[indice]  # Error: 'tarea' no está definido
            estado = "Completada" if tarea["completado"] else "Pendiente"
            print(f"{indice}. {tarea['titulo']} - {estado}")# Error: el índice ya está ajustado

def completar_tarea(indice):
    if indice < 0 or indice >= len(tareas):
        print("Índice de tarea inválido.")
    else:
        tareas[indice]["completado"] = True # Error: debería ser True, no "Sí"
        print(f"Tarea '{tareas[indice]['titulo']}' marcada como completada.")

def eliminar_tarea(indice):
    if indice < 0 or indice >= len(tareas):  # Error: debería ser >=
        print("Índice de tarea inválido.")
    else:
        tarea_eliminada = tareas.pop(indice)
        print(f"Tarea '{tarea_eliminada['titulo']}' eliminada.")

def main():
    while True:
        print("\nSistema de Gestión de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":  # Error: input devuelve un string, comparar con 1 es incorrecto
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            fecha_limite = input("Fecha límite (dd/mm/yyyy): ")
            agregar_tarea(titulo, descripcion, fecha_limite)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            try:
                indice = int(input("Número de la tarea a completar: "))  # Error: no se verifica si es un número válido
                completar_tarea(indice - 1)  # Error: si el índice es 0, se pasaría -1
            except ValueError:
                     print("Por favor, ingresa un número válido.")
        elif opcion == "4":
            try:
                indice = int(input("Número de la tarea a eliminar: "))
                eliminar_tarea(indice - 1)  
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejemplo de uso (esta parte puede generar errores si se intenta correr el código)
agregar_tarea("Estudiar Python", "Repasar conceptos básicos", "10/09/2024")
agregar_tarea("Comprar suministros", "Ir al supermercado", "11/09/2024")
mostrar_tareas()
completar_tarea(1)
mostrar_tareas()
eliminar_tarea(1)
mostrar_tareas()

main()  # Error: la función correcta es 'main'
