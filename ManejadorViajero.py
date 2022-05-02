import csv
from ViajeroFrecuente import ViajeroFrecuente

class ManejadorViajero:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregar(self,viajero):
        if type(viajero)==ViajeroFrecuente:
            self.__lista.append(viajero)
        else:
            print("No se puede agregar.")
    def cargarDatos(self):
        archivo=open('Viajeros.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                #saltear cabecera
                bandera= not bandera
            else:
                num_viajero=int(fila[0])
                dni=fila[1]
                nombre=fila[2]
                apellido=fila[3]
                millas_acum=int(fila[4])
                viajero=ViajeroFrecuente(num_viajero,dni,nombre,apellido,millas_acum)
                self.agregar(viajero)
        archivo.close()
    def mayorCantidadMillas(self):
        ivalormax=0
        for i in range(len(self.__lista)):
            if(self.__lista[i]>self.__lista[ivalormax]):
                ivalormax=i
        return ivalormax
    def mayores(self):
        pos=self.mayorCantidadMillas()
        for i in range(len(self.__lista)):
            if(self.__lista[i]==self.__lista[pos]):
                 print(self.__lista[i])
    def funcionTestManejador(self):
        print("Funcion test Manejador:")
        manejador1=ManejadorViajero()
        manejador2=ManejadorViajero()
        print("Metodo agregar")
        manejador1.agregar(ViajeroFrecuente(150,'23456654','Ailen','Lopez',900))
        manejador2.agregar(ViajeroFrecuente(130,'34567897','Carla','Perez',500))
        print("Metodo cargarDatos")
        manejador1.cargarDatos()
        print("Metodo Mayores")
        manejador1.mayores()        