from animal import Animal

class Reptil(Animal):
    def __init__(self, nome, idade, tipo_de_pele):
        super().__init__(nome, idade)
        self.tipo_de_pele = tipo_de_pele
   
    def movimentar(self):
        print("O réptil está rastejando.")