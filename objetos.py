class Perro:
    def __init__(self, nombre=""):
        self.nombre=nombre
    def muestra(self):
        print(f"Soy {self.nombre}")
        
p = Perro("Fido")
#p.nombre = "Fido"
p.muestra()



"""    
class Perro{
    public string Nombre {get;set;}
    public Perro(){
    }
    public Perro(string nombre){
        this.Nombre = nombre;
    }
    public void Muestra(){
        Console.WriteLine($"Soy {Nombre}")
    }
}
"""

    