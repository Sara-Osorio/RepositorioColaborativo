class Asesoria:
    def __init__ (self, id_asesoria, descripcion, id_empleado):
        self.__id_asesoria = id_asesoria
        self.__descripcion = descripcion 
        self.__id_empleado = id_empleado
 
        
    #Privatizacion de atributos de la clase Asesoria
    @property
    def id_asesoria(self):
        return self.__id_asesoria
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def id_empleado(self):
        return self.__id_empleado
    
    #Se crean los setter de la clase Asesoria
    @id_asesoria.setter
    def id_asesoria(self,valor):
        self.__id_asesoria = valor
    
    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @id_empleado.setter
    def id_empleado(self, valor):
        self.__id_empleado = valor

   #Metodo Agregar
    def agregar_asesoria(self):
        archivo = open("./archivos/Asesoria.txt","a",encoding='utf8')
        archivo.write(f"{self.__id_asesoria}| {self.__descripcion:<20} | {self.__id_empleado}| \n")
        archivo.close()
    
    #Metodo estatico para pedir opciones
    @staticmethod
    def clave(cadena):
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input(f"{cadena}"))
                correcto=True
            except ValueError:
                print('Error, solo se aceptan numeros enteros')
        return num

    @staticmethod
    def empleado(cadena):
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input(f"{cadena}"))
                correcto=True
            except ValueError:
                print('Error, solo se aceptan numeros enteros')
        return num

    @staticmethod
    def nombre_asesoria(cadena):
        nombre = input(f"{cadena}")
        return nombre
    

   #Metodo consultar todo
    @classmethod
    def consultar_todo(self, fichero):
        archivo = open(fichero,encoding='utf8')
        print(archivo.read())
        archivo.close()

    #Metodo consulta especifica
    @classmethod
    def consultar_asesoria(self,codigo):
        archivo = open("./archivos/Asesoria.txt",encoding='utf8')
        for linea in archivo.readlines():
            info = linea.split('|')
            if codigo == info[0]:
                print(linea)
        archivo.close()

    #Metodo de eliminar una asesoria
    @classmethod
    def eliminar(self,archivo,clave):
        Lista = []
        fichero = open(archivo, encoding='utf8')
        for dato in fichero:
            Lista.append(dato)
            info = dato.split('|')
            if clave == info[0]:
                Lista.remove(dato)
            resultado = open(archivo,"w",encoding = "utf8")
            for nuevo in Lista:
                resultado.write(nuevo)
            resultado.close()
        fichero.close()
        
        

   #Metodo de actualizar
    @classmethod
    def modificar(self,archivo,clave,nombre,empleado):
        Lista = []
        fichero = open(archivo, encoding='utf8')
        for dato in fichero:
            Lista.append(dato)
            info = dato.split('|')
            if clave == info[0]:
                Lista.remove(dato)
                Lista.append(f"{clave}| {nombre:<20} | {empleado}| \n")
            resultado = open(archivo,"w",encoding = "utf8")
            for nuevo in Lista:
                resultado.write(nuevo)
            resultado.close()
        fichero.close()
    #Metodo para generar codigos
    @classmethod
    def Agregarid(self,contador):
        nombre, empleado = input('Nombre de la asesoria: '), input('Empleado asigando: ')
        Lista = []
        archivo1 = open('./archivos/Numeros.txt', encoding='utf8')
        cont = 6
        for n in archivo1:
            dato = n.split('\n')
            contador = contador - 1
            cont = cont - 1
            Lista.append(dato[0])
            if contador == 0:
                id_asesoria = str(int(dato[0]) + 1)
                Lista.remove(dato[0])
                Lista.append(id_curso)
            archivo2 = open('./archivos/Numeros.txt',"w",encoding = "utf8")
            for a in Lista:
                archivo2.write(a + '\n')
            archivo2.close()
            if cont == 0:
                break
        archivo1.close()
        C = Asesoria(id_Asesoria,nombre,empleado)
        C.agregar_asesoria()
        
    #Metodo para elegir opciones
    @staticmethod
    def gestion_Asesorias(Opcion):
        if Opcion == 1:
            contador = 2
            Asesoria.Agregarid(contador)
        elif Opcion == 2:
            codigo = Asesoria.clave("Ingresa la clave del registro que vas a eliminar: ")
            clave = str(codigo)
            archivo = "./archivos/Asesoria.txt"
            Asesoria.eliminar(archivo,clave)
            
        elif Opcion == 3:
            fichero = "./archivos/Asesorias.txt"
            clave = Asesoria.clave("Ingresa la clave del registro que vas a actualizar: ")
            nombre = Asesoria.nombre_Asesoria("Nuevo nombre de la asesoria:")
            empleado = Asesoria.empleado(f"Nuevo empleado asignado a la asesoria {nombre}:")
            codigo = str(clave)
            Asesoria.modificar(fichero,codigo, nombre, empleado)
            print("Actualizada con exito")
        elif Opcion == 4:
            fichero = "./archivos/Asesoria.txt"
            Asesoria.consultar_todo(fichero)
        elif Opcion == 5:
            clave = Asesoria.clave("Clave de la asesoria que desea consultar: ")
            codigo = str(clave)
            Asesoria.consultar_asesoria(codigo)
            