class Ave(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def movimentar(self):
        if self.pode_voar:
            print(f"A ave {self.nome} está voando.")
        else:
            print(f"A ave {self.nome} está andando.")