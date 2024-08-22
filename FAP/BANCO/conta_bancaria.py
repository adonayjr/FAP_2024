class ContaBancaria:
    def __init__(self, titular, senha):
        self.titular = titular
        self.__saldo = 0 
        self.__senha = senha

    def consultar_saldo(self):
        print(f"Seu saldo é: R$ {self.__saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor, senha):
        if self.validar_senha(senha):
            if 0 < valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente ou valor inválido.")
        else:
            print("Senha incorreta. Não foi possível realizar o saque.")

    def alterar_senha(self, senha_atual, nova_senha):
        if self.validar_senha(senha_atual):
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("Senha atual incorreta. Não foi possível alterar a senha.")

    def validar_senha(self, senha):
        return self.__senha == senha