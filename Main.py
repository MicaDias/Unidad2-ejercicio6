from ManejadorViajero import ManejadorViajero
from ViajeroFrecuente import ViajeroFrecuente
if __name__=='__main__':
    manejador=ManejadorViajero()
    manejador.cargarDatos()
    viajero=ViajeroFrecuente(100,20455567,'Jose','Perez',1000)
    viajero2=ViajeroFrecuente(130,25089998,'Juan','Olivares',3000)
    print("--------Viajeros------")
    print(viajero)
    print(viajero2)
    print("***Viajeros con mayor cantidad de millas***")
    manejador.mayores()
    print("***Acumular millas***")
    viajero3=viajero+200
    print(viajero3)
    print("***Canjear millas***")
    viajero4=viajero2-100
    print(viajero4)
    manejador.funcionTestManejador()
    viajero.funcionTestViajero()
