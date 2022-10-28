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

aguja1 = Cola()
aguja2 = Cola()
aguja3 = Cola()
for i in range(74):
    aguja1.encolar(i+1)
print(aguja1.items)
while aguja1.es_vacia() == False:
    aguja2.encolar(aguja1.desencolar)
print(aguja2.items)