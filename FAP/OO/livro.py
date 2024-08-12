class Livro:
    # Construtor
    def __init__(self, titulo, autor, ano, editora="Não informado"):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.disponivel = True

    def exibir_infos(self):
        print("-"*30)
        print("Livro:")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Editora: {self.editora}")
        if self.disponivel:
            print("Livro disponível para empréstimo")
        else:
            print("Livro não disponível para empréstimo")
        print("-"*30)
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        else:
            return False