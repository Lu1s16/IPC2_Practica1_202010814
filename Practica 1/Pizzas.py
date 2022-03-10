from Ingredientes import ListaIngredientes


class NodoPizza:

    def __init__(self):
        self.Ingredientes = ListaIngredientes()
        self.Siguiente = None

    
class ListaPizza:

    def __init__(self):
        self.Primero = None
        self.Ultimo = None
        self.NO_pizzas = 0

    
    def InsertarAlFrente(self):
        estaVacio = self.Primero == None
        Nueva_pizza = NodoPizza()

        if estaVacio:
            self.Primero = self.Ultimo = Nueva_pizza

        else:
            curr = self.Primero
            while curr.Siguiente != None:
               
                curr = curr .Siguiente
            
            curr.Siguiente = Nueva_pizza
            

        self.NO_pizzas+=1
        return Nueva_pizza

    def Imprimir(self):
        pizza_no = 1
        Actual = self.Primero
        Tiempo_total = 0
        while Actual != None:
            
            Tiempo_total+=Actual.Ingredientes.Imprimir()
            Actual = Actual.Siguiente
            pizza_no+=1
        return Tiempo_total