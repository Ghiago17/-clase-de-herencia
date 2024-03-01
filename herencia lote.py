class lote: 
    def __init__(self, largo, ancho, constructora):
        self.largo = largo
        self.ancho = ancho
        self.constructora = constructora 

    def calcularArea(self):
        print (self.largo * self.ancho)
    def printcontructora(self):
        print (self.constructora)

class casa (lote):
    def __init__(self, largo, ancho, constructora, telefono,  propietario):
        super().__init__(largo, ancho, constructora)
        self.propietario = propietario
        self.telefono= telefono 

    def printpropietario(self):
        print(self.propietario)
    def printtelefono(self):
        print(self.telefono)

x = casa(7,45,"Jay-z Valencia","Daniel Maza","3243829748")
x.calcularArea()
x.printpropietario() 
x.printtelefono()
x.printcontructora() 