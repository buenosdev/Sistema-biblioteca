from livro import Livro
from usuario import Usuario

class Biblioteca:
    Acervo:list[Livro] = []


    @staticmethod
    def emprestar(usuario: Usuario, livros: list[Livro] ):

        for item in livros:
            if len(usuario.lista_livros) == usuario.MAX_EMPRESTIMO:
                return
            usuario.pegar_emprestado(item)
            item.emprestar_livro(usuario)

    # @staticmethod
    # def devolver(livro: Livro, usuario: Usuario):
    #     livro.devolver_livro()
    #     usuario.