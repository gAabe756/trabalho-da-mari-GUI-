from model import CatalagoAnime, UsuarioModel, AnimeVision

class AnimeController:
    def __init__(self):
        self.catalogo_anime = CatalagoAnime()  # instância do catálogo de animes
        self.usuario_model = UsuarioModel()    # instância do modelo de usuário

    def cadastrar_anime(self, autor, nome, temporada, genero, classificacao, idioma, avaliacao, episodio, duracao):
        anime = AnimeVision(autor, nome, temporada, genero, classificacao, idioma, avaliacao, episodio, duracao)
        self.catalogo_anime.adicionar_animes(anime)

    def cadastrar_filme(self, autor, nome, classificacao, idioma, avaliacao, duracao):
        filme = AnimeVision(autor, nome, 1, "Filme", classificacao, idioma, avaliacao, 1, duracao)
        self.catalogo_anime.adicionar_animes(filme)

    def listar_animes(self):
        return self.catalogo_anime.listar_animes()

    def remover_anime(self, indice):
        self.catalogo_anime.remover_animes(indice)

    def listar_classificacao_alta(self):
        return self.catalogo_anime.listar_classificacao_alta()

    def autenticar_usuario(self, usuario, senha):
        return self.usuario_model.autenticar(usuario, senha)