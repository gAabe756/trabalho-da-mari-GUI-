from flask import Flask, render_template, request, redirect, url_for, session, flash
from controller import AnimeController
from functools import wraps

app = Flask(__name__)
app.secret_key = "troque_essa_chave_em_producao"  # troque em produção
controller = AnimeController()

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged"):
            flash("Faça login para continuar.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "").strip()
        if controller.autenticar_usuario(usuario, senha):
            session["usuario"] = usuario
            session["logged"] = True
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Usuário ou senha inválidos.", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    session.pop("logged", None)
    flash("Você saiu da sessão.", "info")
    return redirect(url_for("login"))

@app.route("/")
@login_required
def index():
    animes = controller.listar_animes()
    altos = controller.listar_classificacao_alta()
    usuario = session.get("usuario", "")
    return render_template("index.html", animes=animes, altos=altos, usuario=usuario)

@app.route("/add", methods=["POST"])
@login_required
def add():
    # captura dados do formulário
    autor = request.form.get("autor", "Desconhecido").strip()
    nome = request.form.get("nome", "Sem título").strip()
    temporada = request.form.get("temporada", "1")
    genero = request.form.get("genero", "Anime").strip()
    classificacao = request.form.get("classificacao", "0")
    idioma = request.form.get("idioma", "Português").strip()
    avaliacao = request.form.get("avaliacao", "0")
    episodio = request.form.get("episodio", "1")
    duracao = request.form.get("duracao", "0")

    # conversões seguras
    try:
        temporada = int(temporada)
    except:
        temporada = 1
    try:
        classificacao = int(classificacao)
    except:
        classificacao = 0
    try:
        avaliacao = float(avaliacao)
    except:
        avaliacao = 0.0
    try:
        episodio = int(episodio)
    except:
        episodio = 1
    try:
        duracao = int(duracao)
    except:
        duracao = 0

    # cadastra usando o Controller (usa AnimeVision)
    controller.cadastrar_anime(
        autor, nome, temporada, genero, classificacao, idioma, avaliacao, episodio, duracao
    )
    flash("Item cadastrado com sucesso.", "success")
    return redirect(url_for("index"))

@app.route("/remove/<int:index>", methods=["POST"])
@login_required
def remove(index):
    controller.remover_anime(index)
    flash("Item removido.", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)