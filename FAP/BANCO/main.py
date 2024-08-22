from conta import Conta

def mostrar_menu():
    print("\nMenu:")
    print("1. Consultar Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Alterar Senha")
    print("5. Sair")

def main():
    titular = input("Digite o nome do titular da conta: ")
    senha = input("Digite a senha para a conta: ")
    conta = Conta(titular=titular, senha=senha)
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            conta.consultar_saldo()
        
        elif opcao == '2':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        
        elif opcao == '3':
            valor = float(input("Digite o valor a ser sacado: "))
            senha = input("Digite sua senha: ")
            conta.sacar(valor, senha)
        
        elif opcao == '4':
            senha_atual = input("Digite sua senha atual: ")
            nova_senha = input("Digite sua nova senha: ")
            conta.alterar_senha(senha_atual, nova_senha)
        
        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
