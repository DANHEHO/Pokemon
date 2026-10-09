import sys
from clases.pokemon import Pokemon

# Variable global para almacenar los objetos Pokémon capturados
lista_pokemons = []


def buscar_pokemon(nombre: str):
    """Función auxiliar con ámbito local que busca un Pokémon en la lista global."""
    for p in lista_pokemons:
        if p.nombre.strip().lower() == nombre.strip().lower():
            return p
    return None


def menu_capturar():
    print("\n--- Capturar Nuevo Pokémon ---")
    nombre = input("Ingresa el nombre del Pokémon: ").strip()
    if not nombre:
        print(" El nombre no puede estar vacío.")
        return

    if buscar_pokemon(nombre):
        print(" Ya tienes un Pokémon con ese nombre.")
        return

    tipo = input("Ingresa el tipo (ej. Fuego, Agua, Planta, Eléctrico): ").strip()
    
    try:
        ataque = int(input("Ataque base [por defecto 10]: ") or 10)
        defensa = int(input("Defensa base [por defecto 10]: ") or 10)
        salud = int(input("Salud base [por defecto 50]: ") or 50)
    except ValueError:
        print("Entrada inválida. Se asignarán valores por defecto.")
        ataque, defensa, salud = 10, 10, 50

    # Crear la instancia del Pokémon
    nuevo_pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)
    lista_pokemons.append(nuevo_pokemon)


def menu_entrenar():
    if not lista_pokemons:
        print("\n❌ No tienes Pokémon para entrenar.")
        return

    print("\n---  Entrenar Pokémon ---")
    nombre = input("¿A qué Pokémon quieres entrenar?: ").strip()
    p = buscar_pokemon(nombre)

    if p:
        print("¿Qué estadísticas deseas enfocar? (Opciones: ataque, defensa, salud)")
        print("Escribe las opciones separadas por coma (o presiona ENTER para un entrenamiento general):")
        eleccion = input("> ").strip()

        if eleccion:
            stats = [s.strip() for s in eleccion.split(",")]
            p.entrenar(*stats)
        else:
            p.entrenar()
    else:
        print(f" No se encontró ningún Pokémon llamado '{nombre}'.")


def menu_ver_pokemons():
    if not lista_pokemons:
        print("\n No hay Pokémon capturados en el registro.")
        return

    print("\n================  POKÉMON CAPTURADOS ================")
    for idx, p in enumerate(lista_pokemons, start=1):
        print(f"\[Pokémon #{idx}]")
        p.mostrar_info()


def menu_liberar():
    if not lista_pokemons:
        print("\n No tienes Pokémon para liberar.")
        return

    print("\n---  Liberar Pokémon ---")
    nombre = input("Ingresa el nombre del Pokémon que deseas liberar: ").strip()
    p = buscar_pokemon(nombre)

    if p:
        # Se remueve de la lista global, eliminando la referencia
        lista_pokemons.remove(p)
        del p  # Fuerza la llamada al destructor __del__
    else:
        print(f" No se encontró ningún Pokémon llamado '{nombre}'.")


def menu_combate_demo():
    """Demuestra el paso de parámetros por referencia modificando la salud del objetivo."""
    if len(lista_pokemons) < 2:
        print("\n Necesitas al menos 2 Pokémon registrados para simular un combate.")
        return

    print("\n---  Simulación de Combate ---")
    atacante_nombre = input("Nombre del Pokémon atacante: ").strip()
    atacante = buscar_pokemon(atacante_nombre)

    objetivo_nombre = input("Nombre del Pokémon objetivo: ").strip()
    objetivo = buscar_pokemon(objetivo_nombre)

    if atacante and objetivo:
        if atacante == objetivo:
            print(" Un Pokémon no puede atacarse a sí mismo.")
        else:
            atacante.atacar(objetivo)
    else:
        print(" Uno o ambos Pokémon no fueron encontrados.")


def main():
    while True:
        print("\n========================================")
        print("      SIMULADOR DE ENTRENAMIENTO    ")
        print("========================================")
        print("1. Capturar nuevo Pokémon ")
        print("2. Entrenar un Pokémon ")
        print("3. Ver información de todos los Pokémon ")
        print("4. Calcular cuántos Pokémon existen ")
        print("5. Simular un combate corto ")
        print("6. Liberar un Pokémon ")
        print("7. Salir ")
        print("========================================")

        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            menu_capturar()
        elif opcion == "2":
            menu_entrenar()
        elif opcion == "3":
            menu_ver_pokemons()
        elif opcion == "4":
            Pokemon.total_pokemons()
        elif opcion == "5":
            menu_combate_demo()
        elif opcion == "6":
            menu_liberar()
        elif opcion == "7":
            print("\n ¡Gracias por usar el Simulador Pokémon! ¡Hasta pronto!\n")
            sys.exit()
        else:
            print(" Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    main()