class Cargo:
    secuencia=0
    def __int__(self,des):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des
        
cargo1=Cargo()
print("cargo 1",cargo1.codigo,cargo1.descripcion)
cargo2=Cargo("Docente")
print("cargo 2",cargo2.codigo,cargo2.descripcion)
cargo3=Cargo()
print("cargo 3",cargo3.codigo,cargo3.descripcion)
print(Cargo.secuencia)