import csv
class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apellido=''
    __milla_acum=0
    
    def __init__(self,num_viajero=0, dni='',nombre='',apellido='',milla_acum=0):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__milla_acum=milla_acum
    def getMillas(self):
        return self.__milla_acum
    def __gt__(self,otroViajero):
        return self.__milla_acum>otroViajero.getMillas()
    def __eq__(self,otroViajero):
        return self.__milla_acum==otroViajero.getMillas()
    def __add__(self,can):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__milla_acum+can)
    def __sub__(self,can):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__milla_acum-can)
    def __str__(self):
        return "Numero de viajero:%d, DNI:%s,Nombre:%s,Apellido:%s, Cantidad de millas:%d"%(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__milla_acum)
    def funcionTestViajero(self):
        print("*****Funcion test Viajero*****")
        viajero1=ViajeroFrecuente(500,'33444555','Paulo','Diaz',600) 
        viajero2=ViajeroFrecuente(400,'21345678','Kevin','Trump',700)
        print("------Viajeros-----")
        print(viajero1)
        print(viajero2)
        print("---Acumular millas---")
        viajero3=viajero1+400
        viajero4=viajero2+300
        print(viajero3)
        print(viajero4)
        print("---Canjear Millas---")
        viajero5=viajero1-100
        viajero6=viajero2-100
        print(viajero5)
        print(viajero6)
        print("---Metodo getMillas()---")
        print(viajero3.getMillas())
        print(viajero4.getMillas())