class Tarea:
    def __init__(self):
        pass
    def calcularJornada(self):
        ht,he,het=0,0,0
        ph, phe,pt,ph8=0,0,0,0
        ht=input("Ingrese horas trabajadas")
        ph=input("Ingrese valor hora: ")
        if ht>40:
            he = ht-40
            if he>8:
               het= he-8
               ph8=8*ph*2
               phe=het*ph*3
            else:
                phe=0
                ph8=he*ph*2
            pt=40*ph+ph8+phe            
        else:
            pt=ht*ph
        print("Sobretiempo<8:{} Sobretiempo>:{} Jornada:{}".format(ph8,phe,pt))
        
    def factorial(self):
        n=int(input("Ingrese la cantidad de numeros: "))
        
        for i in range(n):
            numero=int(input("Ingrese numero:"))
            acu=1
            for num in range(numero,1,-1):
                acu=acu*num
            print("numero={} factorial={}".format(numero,acu))
            
tarea=Tarea()
tarea.factorial()