from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

CADASTROS_FILE = "cadastros.json"

def carregar_cadastros():
    if not os.path.exists(CADASTROS_FILE):
        return []
    with open(CADASTROS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_cadastros(cadastros):
    with open(CADASTROS_FILE, "w", encoding="utf-8") as f:
        json.dump(cadastros, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        dados = {
            "nome": request.form.get("nome"),
            "cpf": request.form.get("cpf"),
            "telefone": request.form.get("telefone"),
            "cidade": request.form.get("cidade"),
            "renda": request.form.get("renda"),
            "membros": request.form.get("membros"),
            "situacao": request.form.get("situacao"),
        }
        cadastros = carregar_cadastros()
        cadastros.append(dados)
        salvar_cadastros(cadastros)
        return redirect(url_for("cadastro") + "?sucesso=1")
    return render_template("cadastro.html")

@app.route("/programas")
def programas():
    return render_template("programas.html")

if __name__ == "__main__":
    app.run(debug=True)
