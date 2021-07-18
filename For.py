class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        datos=["Daniel",50,True]
        numeros=(2,5.6,4,1)
        docente={'nombre':'Daniel','edad':50, 'frac': 'fraci'}
        listaNotas=[(30,40),(20,40,50),(50,40)]
        #listaAlumnos = (("nombre":"Erick","final":70), ("nombre":"Yady", "final":60), ("nombre":"Yady", "final":60))
        
        # se ejecuta desde inicio hasta el limite
        # fro  con range() o con colecciones
        
    # j=0
    #     while j<5:
    #         print(j)
    #         j=j+1 
            
        # for i in range(5): #rango(0,1,2,3,4)
        #     print('for',i,end='')
        # print()
        
        # for i in range(1,5): #rango(0,1,2,3,4)
        #     print('for',i,end='')
        # print()
        
        # for i in range(2,10,2): #rango(0,1,2,3,4)
        #     print('for',i,end='')
        # print()
        
        # for i in range(12,3,-3): #rango(0,1,2,3,4)
        #     print('for',i,end='')
        
        # lon=len(nombre)
        # for pos in range(lon):
        #     if pos ==0 and pos !=0:
        #         print(post, nombre[post])
        
        # lon=len(datos)
        # for pos in range(lon):
        #     print(pos,datos[pos])
            
        # for pos, valor in enumerate(datos):
        #     print(pos,valor)
            
        # for clave, valor in docente.items():
        #     print(clave, valor,end="")
        
        # print(listaNotas)
        # for notas in listaNotas:
        #     print("For externo", notas)
        #     for notas in notas:
        #         print(nota, end="")
        #     print("Saliendo del for interno")
            
        # print(listaNotas)
        # for notas in listaNotas:
        #     acum=0
        #     for notas in notas:
        #         acum=acum+notas
        #     print(acum/len(notas), end=" ")
        
        # print("\nDiccionario de alumnos")
        # print(listaAlumnos)
        # for alumnos in listaAlumnos:
        #     print(alumnos)
        #     for clave.valor in alumnos.items():
        #         print(clave,":", valor,end="")
        #     print()
        
        # listaAlumnos = listaAlumnos = (("nombre":"Erick","final":70), ("nombre":"Yady", "final":60), ("nombre":"Yady", "final":60))
        # print("\nDiccionario de alumnos")
        # print(listaAlumnos)
        # acum=0
        
        # for alumnos in listaAlumnos:
        #     print(alumnos,";",len(alumnos))
            
        #     for clave,valor in alumnos.items():
        #         print(clave,";",valor, end=" ")
        #         if clave == 'final':
        #             acum=acum+valor
                    
        #     print()
        # print("promedio", acum/len(listaAlumnos))
        listaNotas=[(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum,cont=0,0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            for nota in nota:
                acumparcial+=nota
            cont=cont+acumparcial
            print("Total Parcial1: {} Promedio Parcial: {}".format(acumparcial,acumparcial/len(notas)))
        print("totalGeneral: {} PromedioGeneral:{}".format(acum,acum/cont))
        
bucle= For()
bucle.usoFor()     
    