class AnimeVision:
    def __init__(self, autor, nome, temporada, genero, classificacao, idioma, avaliacao, episodio, duracao):
        self.autor = autor
        self.nome = nome
        self.temporada = temporada
        self.genero = genero
        self.classificacao = classificacao
        self.idioma = idioma
        self.avaliacao = avaliacao
        self.episodio = episodio
        self.duracao = duracao

    def descricao(self):
        return f"Autor: {self.autor}  Titulo: {self.nome}  Temporada: {self.temporada}  Gênero: {self.genero} | Classificação: {self.classificacao}  Idioma: {self.idioma}  Nota: {self.avaliacao} Episódio {self.episodio} Duração {self.duracao} min"

    def classificacao_alta(self):
        return self.classificacao >= 18


class Anime(AnimeVision):
    def __init__(self, autor, nome, temporada, classificacao, idioma, avaliacao, episodio, duracao):
        super().__init__(autor, nome, temporada, "Anime", classificacao, idioma, avaliacao, episodio, duracao)
        self.duracao = duracao
        

class CatalagoAnime:
    def __init__(self):
        self.animes = []

    def adicionar_animes(self, anime):
        self.animes.append(anime)
        
    def listar_animes(self):
        return self.animes
    
    def remover_animes(self, indice):
        if 0 <= indice < len(self.animes):
            self.animes.pop(indice) 

    def listar_classificacao_alta(self):
        alertas = []
        for anime in self.animes:
            if anime.classificacao_alta():
                alertas.append(anime)
        return alertas


class UsuarioModel:
    def __init__(self):
        self.usuario = 'douglas'
        self.senha = 'guigui'

    def autenticar(self, usuario, senha):
        return usuario == self.usuario and senha == self.senha  # verifica se o usuário e senha estão corretos
