from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

def mostrar_menu():
    print("\nMenu:")
    print("1. Consultar Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Alterar Senha")
    print("5. Sair")

def operacoes_conta(conta):
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ContaCorrente.consultar_saldo()
        
        elif opcao == '2':
            valor = float(input("Digite o valor a ser depositado: "))
            ContaCorrente.depositar(valor)
        
        elif opcao == '3':
            valor = float(input("Digite o valor a ser sacado: "))
            senha = input("Digite sua senha: ")
            ContaCorrente.sacar(valor, senha)
        
        elif opcao == '4':
            senha_atual = input("Digite sua senha atual: ")
            nova_senha = input("Digite sua nova senha: ")
            ContaCorrente.alterar_senha(senha_atual, nova_senha)
        
        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

def main():
    tipo = int(input("Digite 1 para conta corrente ou 2 para conta poupança: "))

    titular = input("Digite o nome do titular da conta: ")
    senha = input("Digite a senha para a conta: ")

    if tipo == 1:
        conta = ContaCorrente(titular=titular, senha=senha)
    elif tipo == 2:
        conta = ContaPoupanca(titular=titular, senha=senha)
    else:
        print('Opção inválida do tipo de conta!')
        return

    operacoes_conta(conta)

if __name__ == "__main__":
    main()