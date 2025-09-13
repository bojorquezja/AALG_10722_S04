"""
Usando la clase Perro, agregue el atributo edad y 
haga un menu con estas opciones:
1) crear 1 perro y agregarlos a una lista de perros existente
2) mostrar todos los perros de la lista
3) fin
"""

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

lista_perros = []
while True:
    print("\n1) Crear un perro y agregar a la lista")
    print("2) Mostrar todos los perros")
    print("3) Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del perro: ")
        edad = input("Edad del perro: ")
        nuevo_perro = Perro(nombre, edad)
        lista_perros.append(nuevo_perro)
        print("Perro agregado")

    elif opcion == "2":
        if not lista_perros:
            print("No hay perros en la lista.")
        else:
            print("\nLista de perros:")
            for i, perro in enumerate(1):
                print(f"{i+1}. Nombre: {perro.nombre}, Edad: {perro.edad}")

    elif opcion == "3":
        print("Fin")
        break