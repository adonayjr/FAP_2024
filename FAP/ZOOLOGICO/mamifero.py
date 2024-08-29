from animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, idade, tem_pelo):
        super().__init__(nome, idade)
        self.tem_pelo = tem_pelo
   
    def fazer_som(self):
        print("O mamífero está rugindo.")