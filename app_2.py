from flask import Flask, render_template, request
import sqlite3

conn = sqlite3.connect('restaurantes.db')
cursor = conn.cursor()

criacao_de_tabela = """
    CREATE TABLE IF NOT EXISTS restaurantes (
        id_restaurante INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    """

tabela_filha = """
    CREATE TABLE IF NOT EXISTS comidas_restaurantes (
        id INTEGER PRIMARY KEY,
        restaurante_id INTEGER NOT NULL,
        name TEXT NOT NULL
        carne INTEGER NOT NULL
        ovo INTEGER NOT NULL
        leite INTEGER NOT NULL
        gluten INTEGER NOT NULL
        frutosdomar INTEGER NOT NULL
        alcool INTEGER NOT NULL
        amendoim INTEGER NOT NULL
        soja INTEGER NOT NULL
        nozesoucastanhas INTEGER NOT NULL
        acucar INTEGER NOT NULL
        FOREIGN KEY (restaurante_id) REFERENCES restaurantes (id_restaurante)
    """

cursor.execute(criacao_de_tabela)
cursor.execute((tabela_filha))

app = Flask(__name__)

@app.route("/")
def main_page():
    return ("<h1> This is the main page. Here you can create or login and then change your restaurant's data, as well"
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
