from Pizzas import ListaPizza


class NodoOrden:

    def __init__(self, Nombre_cliente, numero_pizzas):
        self.Nombre_cliente = Nombre_cliente
        self.Numero_pizzas = numero_pizzas
        self.Pizzas = ListaPizza()  #lista de pizzas
        self.Siguiente = None
        self.Anterior = None

    


class ColaOrdenes:

    def __init__(self):
        self.PrimerNodo = None
        self.UltimoNodo = None
        self.Tamaño = 0

    
    def InsertarAlFrente(self, nombre, numero):
        estaVacio = self.PrimerNodo == None
        Nueva_orden = NodoOrden(nombre, numero)

        if estaVacio:
            self.PrimerNodo = self.UltimoNodo = Nueva_orden

        else:
            Nueva_orden.Siguiente = self.PrimerNodo
            self.PrimerNodo.Anterior = Nueva_orden
            self.PrimerNodo = Nueva_orden
            

        
        return Nueva_orden

    def EliminarDelFinal(self):
        pass

    def Imprimir(self):
        Actual = self.PrimerNodo
        Actual1 = self.UltimoNodo #de reversa
        Tiempo_para_orden = 0
        while Actual1 != None:
            Tiempo_para_orden+=Actual1.Pizzas.Imprimir()
            
            print("Nombre del cliente: ", Actual1.Nombre_cliente, "Tiempo de espera: ", Tiempo_para_orden, "\n")
            Actual1 = Actual1.Anterior
          
            
        

    def Mostrar_primero(self):
        Actual = self.UltimoNodo
        
        if self.UltimoNodo == self.PrimerNodo:

            if self.UltimoNodo == None:
                print("Ya no hay entregas pendientes")
            
            else: 
                print("Se entrego la orden de:", Actual.Nombre_cliente)
                self.PrimerNodo = self.UltimoNodo = None

            
        else:
            print("Se entrego la orden de:", Actual.Nombre_cliente)
            self.UltimoNodo = Actual.Anterior
            self.UltimoNodo.Siguiente = None