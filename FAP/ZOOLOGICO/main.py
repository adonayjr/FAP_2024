from mamifero import Mamifero
from ave import Ave
from reptil import Reptil

def main():
    leão = Mamifero("Leão", 5, True)
    papagaio = Ave("Papagaio", 2, True)
    cobra = Reptil("Cobra", 4, "escamas")
   
    leão.fazer_som()
    leão.movimentar()
   
    papagaio.fazer_som()
    papagaio.movimentar()
   
    cobra.fazer_som()
    cobra.movimentar()

if __name__ == "__main__":
    main()