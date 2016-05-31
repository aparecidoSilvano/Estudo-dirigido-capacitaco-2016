from flask import Flask, request, url_for, current_app, render_template

from db import noticias


app = Flask('wtf', static_folder='assets')


@app.route("/noticias/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        dados_do_formulario = request.form.to_dict()
        id_nova_noticia = noticias.insert(dados_do_formulario)
        return render_template('cadastro_sucesso.html', id_nova_noticia=id_nova_noticia)
	
    else:  # GET
        return render_template('cadastro.html', title=u"Inserir nova noticia")

	

@app.route("/")
def index():
	todas_as_noticias = noticias.all()
	return render_template('index.html', noticias=todas_as_noticias, title=u"Todas as noticias")


@app.route("/noticia/<int:noticia_id>")
def noticia(noticia_id):
    noticia = noticias.find_one(id=noticia_id)  # query no banco de dados
    return render_template('noticia.html', noticia=noticia)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)