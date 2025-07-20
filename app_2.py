from flask import Flask, render_template, request
import sqlite3

conn = sqlite3.connect('restaurantes.db')
cursor = conn.cursor()

criacao_de_tabela = """
    CREATE TABLE IF NOT EXISTS RESTAURANTES (
        id INTEGER PRIMARY KEY
        name TEXT NOT NULL
"""

cursor.execute(criacao_de_tabela)

app = Flask(__name__)

@app.route("/")
def main_page():
    return ("<h1> This is the main page. Here you can create or login and then change your restaurants data, as well"
            "as getting the menu´s link or qr-code<h1>")

@app.route("/pegar_login", methods=['POST'])
def pegar_login():
    login = request.form['login']
    senha = request.form['password']
    return login, senha


@app.get("/<restaurante>")
def main_page(restaurante):
    name = restaurante
    # Aqui busco pela database pelo nome
    return f"<h1> This will be the main page. The name of this restaurant is {name}"

@app.route("/<restaurante>/cardapio", methods=['POST'])
def get_data():
    return


if __name__ == "__main__":
    app.run(debug=True)
