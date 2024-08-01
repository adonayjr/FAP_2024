import random

palavras = ("maçã", "banana", "laranja", "uva", "pera", "melancia")

def main():
    continuar = True
    while continuar:
        palavra_aleatoria = random.choice(palavras)
        letras_adivinhadas = []
        tentativas_erradas = 0
        max_tentativas = 6
        
        print("\nBem-vindo ao Jogo da Forca!\n")

        while tentativas_erradas < max_tentativas:
            display_palavra = ""
            for letra in palavra_aleatoria:
                if letra in letras_adivinhadas:
                    display_palavra += letra + " "
                else:
                    display_palavra += "_ "
            
            print(f"A palavra é: {display_palavra.strip()}")
            print(f"Tentativas restantes: {max_tentativas - tentativas_erradas}")
            letra_usuario = input("Digite uma letra: ").lower()

            if letra_usuario in letras_adivinhadas:
                print("Você já tentou essa letra. Tente outra.\n")
                continue
            
            letras_adivinhadas.append(letra_usuario)

            if letra_usuario in palavra_aleatoria:
                print(f"Boa! A letra {letra_usuario.upper()} está na palavra.\n")
            else:
                tentativas_erradas += 1
                print(f"-> Você errou pela {tentativas_erradas}ª vez. Tente de novo!\n")

            if all(letra in letras_adivinhadas for letra in palavra_aleatoria):
                print(f"Parabéns! Você adivinhou a palavra: {palavra_aleatoria.upper()}")
                break

        if tentativas_erradas == max_tentativas:
            print(f"Você perdeu! A palavra era: {palavra_aleatoria.upper()}")

        continuar = input("Deseja jogar novamente? (s/n): ").lower() == 's'

if __name__ == "__main__":
    main()
