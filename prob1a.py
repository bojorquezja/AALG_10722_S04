class Perro:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad
    def muestra(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años")

lista_perros = []

while True:
    print("\n--- MENÚ ---")
    print("a) Crear un perro y agregarlo a la lista")
    print("b) Mostrar todos los perros de la lista")
    print("c) Fin")
    opcion = input("Elija una opción: ").lower()

    if opcion == "a":
        nombre = input("Ingrese el nombre del perro: ")
        try:
            edad = int(input("Ingrese la edad del perro: "))
        except ValueError:
            print("La edad debe ser un número. Se asignará 0.")
            edad = 0

        p = Perro(nombre, edad)
        lista_perros.append(p)
        print("Perro agregado correctamente.")

    elif opcion == "b":
        if not lista_perros:
            print("No hay perros en la lista.")
        else:
            print("\n--- Lista de Perros ---")
            for i, perro in enumerate(lista_perros):
                print(f"{i+1}. ", end="")
                perro.muestra()



    elif opcion == "c":

        print(" Fin del programa.")

        break



    else:

        print(" Opción no válida. Intente de nuevo.")