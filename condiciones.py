class Condicion:
    
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.numero2
        self.numero3=numero
        
    def usoIf(self):
        #if....elif....els... permiten condicionar la ejecuicion de  un o varios bloques
        #de sentencias al cumlimiento de una o variables condiciones.
        if self.numero1 == self.numero2:
            print("numero1={}=numero2={}: son iguales".format(self.numero,self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1 y numero3 son iguales")
        else:
            print("numeros diferentes")
        print("fin if")
            
# print("instancia de la clase")
# cond2= Condicion()
# print(cond2.numero3)
# cond2.usoIf()
cond1= Condicion(10,20)
cond1.usoIf()
print("Gracias por su visita")