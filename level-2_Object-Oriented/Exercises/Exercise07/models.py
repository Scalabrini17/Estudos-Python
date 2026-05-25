# Atividade 1
class Livro:
    # Atividade 1
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
    
    # Atividade 2
    def __str__(self):
        return f'Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação:  {self.ano_publicacao} '
   
    # Atividade 3
    def emprestar(self):
        self.disponivel = False

# Atividade 4
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

#atividade2
livro1 = Livro('As Crônicas de Narnia', 'C.S. Lewis', 1950)    
livro2 = Livro('O Cristianismo Puro e Simples', 'C.S. Lewis', 1952)
print(f'{livro1} \n {livro2}')

# Atividade 3
livro3 = Livro('Um Tratado Sobre a Meditação: Um Cristão no Monte', 'Thomas Watson', 1659)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

#Atividade 4
Livro.livros = [livro1, livro2, livro3]
