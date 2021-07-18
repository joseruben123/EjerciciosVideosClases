class Ejercicios:
    def __init__(self,datos):
        self.__lista=datos
        self.nom=""
        
    
    def parImpar(self,numero):
        if numero %2==0:
            print("{} es par".format(numero))
        else:
            print("{} es impar".format(numero))
            
    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero%i==0:
                acu=acu+i
        if numero==acu:
            print("{} es perfecto".format(numero))
        else:
            print("{} no es perfecto".format(numero))
    
    def perfecto2(self, numero):
        acu=0
        for i in range(1,numero):
          if numero%i==0:
              acu=acu+i
        return acu  
    
class Programacion(Ejercicios):
    def __init__(self):
        pass

    def divisores(self,num):
        cont=1
        divisores=[]
        while cont<num:
            rec=num%cont
            if rec==0:
               divisores.append(num)
            cont=cont+1
        print(divisores)
        
class Programacion(Ejercicios):
    def __init__(self, valor):
        self.dato=valor
    
    def divisores(self,num):
        divisores=[]
        for cont in range(1,num):
            rec=num%cont
            if rec ==0:
                divisores.append(cont)
        return divisores

       
prog1=Programacion()
