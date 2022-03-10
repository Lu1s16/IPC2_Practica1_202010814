


from Ordenes import ColaOrdenes
t = ColaOrdenes()

def Ingresar_datos():

    global t
    
    global ORDEN
    global PIZZA
    

    print("Ingrese su nombre:")
    nombre = input()
    print("")

    print("Ingrese cuantas pizzas quiere:")
    no_pizzas = int(input())
    ORDEN = t.InsertarAlFrente(nombre, no_pizzas)
    print("")
    print("""Ingredientes disponibles:
1. Pepperoni
2. Salchicha
3. Carne
4. Queso
5. Piza""")

    for c in range(no_pizzas):
        numero = c + 1
        PIZZA = ORDEN.Pizzas.InsertarAlFrente()
        print("Cuantos ingredientes desea para la pizza: ", numero)
        no_ingredientes = int(input())
        print("")

        print("Ingrese los ingredientes: ")

        for c in range(no_ingredientes):
            ingrediente = input().lower()

            if ingrediente == "pepperoni":
                tiempo = 3
                PIZZA.Ingredientes.InsertarAlFrente(ingrediente, tiempo)


            elif ingrediente == "salchicha":
                tiempo = 4
                PIZZA.Ingredientes.InsertarAlFrente(ingrediente, tiempo)

            elif ingrediente == "carne":
                tiempo = 10
                PIZZA.Ingredientes.InsertarAlFrente(ingrediente, tiempo)

            elif ingrediente == "queso":
                tiempo = 5
                PIZZA.Ingredientes.InsertarAlFrente(ingrediente, tiempo)

            elif ingrediente == "piña":
                tiempo = 2
                PIZZA.Ingredientes.InsertarAlFrente(ingrediente, tiempo)
            
    Menu()
    





def Extraer_orden():
    t.Mostrar_primero()
    Menu()

def Mostrar_ordenes():
    t.Imprimir()
    Menu()

def Mostrar_datos_desarrollador():
    print("""Nombre: Luis Enrique Garcia Gutierrez
Carnet: 202010814""")
    Menu()

def Salir():
    print("se ha salido del programa")


def Menu():
    print("""---------------
Menu:
1. Ingresar datos
2. Entregar
3. Mostrar ordenes
4. Mostrar datos del desarrolador
5. Salir
----------------
Ingrese una opcion:""")

    op = int(input())

    if op == 1:
        Ingresar_datos()

    elif op == 2:
        Extraer_orden()

    elif op == 3:
        Mostrar_ordenes()

    elif op == 4:
        Mostrar_datos_desarrollador()

    elif op == 5:
        Salir()

    else:
        print("opcion invalida")
        Menu()



if __name__ == '__main__':
    
    Menu()
    
    

    