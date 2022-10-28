class Cola:

    def __init__(self):
        self.items=[]
    
    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
        return self.items == []

def primera_aguja():
    aguja1 = Cola()
    for i in range(74):
        aguja1.encolar(i+1)
    return aguja1

def segunda_aguja():
    aguja2 = Cola()
    return aguja2

def tercera_aguja():
    aguja2 = Cola()
    return aguja2

def pila_a_pila(pila1, pila2):
    while pila1.es_vacia() == False:
        pila2.encolar(pila1.desencolar)