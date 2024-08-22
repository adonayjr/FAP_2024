from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, senha, saldo=0):
        super().__init__(titular, senha, saldo)
    
    def render_juros(self, porcentagem):
        rendimento = self.get_saldo() * (porcentagem/100)
        self.set_saldo(self.get_saldo() + rendimento)