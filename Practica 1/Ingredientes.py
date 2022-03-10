class NodoIngredientes:

    def __init__(self, ingrediente, tiempo):
        self.Ingrediente = ingrediente
        self.Tiempo = tiempo
        self.Tiempo_total = 0
        self.Siguiente = None

    
class ListaIngredientes:

    def __init__(self):
        self.Primero = None
        self.Ultimo = None

    
    def InsertarAlFrente(self, ingrediente, tiempo):
        Nuevo_ingrediente = NodoIngredientes(ingrediente, tiempo)
        estaVacio = self.Primero == None

        if estaVacio:
            self.Primero = self.Ultimo = Nuevo_ingrediente
        
        else:
            curr = self.Primero
            while curr.Siguiente != None:
                curr = curr.Siguiente
            
            curr.Siguiente = Nuevo_ingrediente

    
    def Imprimir(self):
        Actual = self.Primero
        tiempo_de_orden = 0
        while Actual != None:
            tiempo_de_orden+=Actual.Tiempo
            Actual = Actual.Siguiente
        return tiempo_de_orden
        



