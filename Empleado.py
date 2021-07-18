from cargo import Cargo

class Empleado:
    secuencia=0
    def __init__(self, nom="", sue=0,car=None):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.suelo=sue
        self.cargoEmp=car
        
    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuenia
    def mostrar(self):
        print("Codigo:{} Nombre:{} Cargo({}):{}".format(self.codigo,self.nombre, self.cargoEmp.codigo))
        
cargo1 = Cargo("Docente")
emp1= Empleado("Daniel", 1000,cargo1)
emp1.mostrar()
emp2= Empleado("Moises", 1000,cargo1)
emp2.mostrar()