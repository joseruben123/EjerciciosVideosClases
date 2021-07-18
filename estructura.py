""" num=20
nombre="ana"
print(num,type(num))
print(nombre,type(nombre))

def mensaje(msg):
    print(msg)

mensaje("Mi primer progrmaa en python")
mensaje("Mi segundo progrma en python") """

class Sintaxis: 
    instancia=0 #atributo de clase
    # __init__ Metodoconstructor que se ejecuta cuando se instancia la clase cuyo objeto es creado 
    #e iniciado los atributos de la clase. Self es un objeto que representa la clase creada
    def __init__(self,datos="llamando al constructor"):
        self.frase=datos
        Sintaxis.instancia = Sintaxis.instancia+1
        
    def usoVariables(self):
        edad, _peso = 50, 70.5
        nombres = 'Jose'
        tipo_sexo = 'M' 
        civil = True
        #tupas =() son colecciones de datos de cia;quier tipo inmutables
        usuario=()
        usuario=('dchiki', '1234', 'jose@gmail.com')
        #usuario[0]='jose'
        #print(usuario[2], nombres[7])
        #listas = [] colecciones mutables
        materias = ['programacion web', 'PHP', 'POO']
        aux=materias[1]
        materias[1] = 'PYTHON'
        materias.append("Go")
        #print(materias,aux,materias[1])
        #diccionario = {} cooleccion de objetos clave: valor tipo json
        docente={}
        docente = {'nombre': 'Daniel', 'edad':50, 'activo': True}
        edad=docente['edad']
        docente['edad']=51
        docente['carrera']='IS'
        #print(docente,edad,docente['edad'])
        #print(usuario, usiario[0],usiario[0:2], usuario[-1])
        print(materias,materias[2:], materias[3:], materias[::-1], materias[-2:])
        # presentacion con format
        # print("""Mi nombre es {}, tengo {} anos""".format(nombre, edad))
        
        
print("Sintaxis antes de instancia es: {}".format(Sintaxis.instancia))   
ejer1 = Sintaxis() #instanci la clase sinstaxis y crea el objeto ejer1(copia de la clase)
# print("Sintaxis de ejer1 es: {}".format(Sintaxis.instancia))   
# ejer2 = Sintaxis("instancia2")
# print(ejer1.frase)
# print("Sintaxis de ejer2 es: {}".format(Sintaxis.instancia))    
# print("Sintaxis nuevamente de ejer1 es: {}".format(Sintaxis.instancia))   
# print(ejer1.frase)    