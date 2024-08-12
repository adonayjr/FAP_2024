class Biblioteca:
    def __init__(self):
        self.lista_livros = []

    def adicionar_livro(self, livro):
        self.lista_livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca.')

    def listar_livros(self):
        if not self.lista_livros:
            print("Nenhum livro cadastrado na biblioteca.")
        else:
            print("Livros disponíveis na biblioteca:")
            for livro in self.lista_livros:
                livro.exibir_infos()

def pegar_emprestado(livro):
    print("Pegando o livro emprestado")
    foi_emprestado = livro.emprestar()
    if foi_emprestado:
        print("Empréstimo realizado com sucesso")
    else:
        print("Empréstimo não realizado, livro não disponível")