from carro import Carro

def main():
    meu_carro = Carro("Fiat", "Uno", 1998)
    meu_carro.exibir_infos()  # Exibe informações após atribuir os valores
    print(meu_carro.velocidade)
    meu_carro.acelerar()
    meu_carro.frear()
    meu_carro()
    print(meu_carro.velocidade)
if __name__ == "__main__":
    main()