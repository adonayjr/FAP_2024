if __name__ == "__main__":
    leao = Mamifero("Leão", 5, True)
    leao.fazer_som()
    leao.movimentar()

    aguia = Ave("Águia", 3, True)
    aguia.fazer_som()
    aguia.movimentar()

    cobra = Reptil("Cobra", 2, "escamas")
    cobra.fazer_som()
    cobra.movimentar()