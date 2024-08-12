from livro import Livro


def main():
    biblioteca = Biblioteca()
    
    # Cadastrando livros
    meu_livro = Livro(titulo="Antes que o café esfrie",
                      autor="Toshikazu Kawaguchi", ano="2022", 
                      editora="Valentina")
    
    meu_livro2 = Livro("Antes que o café esfrie 2",
                      "Toshikazu Kawaguchi", 2023, "Valentina")
    
    meu_livro3 = Livro(ano=2024, titulo="Antes que o café esfrie 3", 
                       autor="Toshikazu Kawaguchi")
    
    # Adicionando livros à biblioteca
    biblioteca.adicionar_livro(meu_livro)
    biblioteca.adicionar_livro(meu_livro2)
    biblioteca.adicionar_livro(meu_livro3)
    
    # Listando livros da biblioteca
    biblioteca.listar_livros()

    # Pegando emprestado
    pegar_emprestado(meu_livro)
    pegar_emprestado(meu_livro)
    
    # Devolvendo
    meu_livro.devolver()
    meu_livro.exibir_infos()

if __name__ == "__main__":
    main()