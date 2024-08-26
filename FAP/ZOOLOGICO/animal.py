class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print(f"O {self.nome} está fazendo um som.")

    def movimentar(self):
        print(f"O {self.nome} está se movimentando.")