class Ordenar:
    def __init__(self,lista):
        self.lista=lista
        
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    def recorrerPosicion(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
    
    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos, self.lista[pos])       
    
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:return pos
        else:return -1
        
    def ordenarAsc(self):
        for pos in range(0,len(self.linsta)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos]>self.lista[sig]:
                    aux=self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
                    
    def ordenarDes(self):
        for pos,ele in enumerate(self.lista):
            for sig in range(pos+1,len(self.lista)):
                if ele<self.lista[sig]:
                    aux=self.lista[sig]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
                    
    def primer(self):
        return self.lista[0]
    
    def primerEliminado(self):
        primer=self.lista[0]
        auxlista=[]
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primer
    
    def primerEliminado2(self):
        primer=self.lista[0]
        self.lista=self.lista[1:]
        return primer
    
    def ultimo(self):
        return self.lista[-1]
            
    def ultimoEliminado(self):
        ultimo=self.lista[-1]
        self.lista=self.lista[0:-1]
        return ultimo
    
    def insertar(self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num<ele:
                auxlista.append(num)
                break
        self.liista=self.lista[0:pos]+auxlista+self.lista[pos:]
        
    
    def insertarOrden(self, num):
        self.lista.append(num)
        self.ordenarAsc()
        
    def eliminar(self,num):
        enc=False
        for pos, ele in enumerate(self.lista):
            if num==ele:
                enc=True
                break
        if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
        
        

lista=[2,3,8,10]
#insertar=5=[2,3,8,10]
ord1=Ordenar(lista)
#print(ord1.lista)
print(ord1.eliminar(5))
print(ord1.lista)
# print("Normal",ord1.lista)
# ord1.ordenarAsc()
# print("Asc", ord1.lista)
# ord1.ordenarDes()
# print("Des", ord1,lista)

lista=[2,4,8,5,10]
x=lista[2]
list1=lista[1:]

list2=lista[:-1]
for pos in range(len(lista)-1):
    print("Primer for", pos,lista[pos])
    for j in range(pos+1,len(lista)):
        print("segundo for",j,lista[j])
    input("presione una tecla para continuar .....")