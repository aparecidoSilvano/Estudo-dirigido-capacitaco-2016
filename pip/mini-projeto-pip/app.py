from flask import Flask, render_template

app= Flask("")

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/<name>")
def html_page(name):
	if name.lower() == "bruno":
		return "<strong>Oi {}!</strong>".format(name), 200
	else:
		return "Not Founf", 404
	
@app.route("/pagina/<nome>")
def html_page_nome(nome):
	return render_template("index.html", nome=nome)
	
	
app.run()