from flask import Flask, render_template, request
import sqlite3

conn = sqlite3.connect('restaurantes.db')
cursor = conn.cursor()

criacao_de_tabela = """
    CREATE TABLE IF NOT EXISTS restaurantes (
        id_restaurante INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        email TEXT,
        senha TEXT,
        imagem_principal BLOB
        )
    """

tabela_filha = """
    CREATE TABLE IF NOT EXISTS comidas_restaurantes (
        id INTEGER PRIMARY KEY,
        restaurante_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        carne INTEGER NOT NULL,
        ovo INTEGER NOT NULL,
        leite INTEGER NOT NULL,
        gluten INTEGER NOT NULL,
        frutosdomar INTEGER NOT NULL,
        alcool INTEGER NOT NULL,
        amendoim INTEGER NOT NULL,
        soja INTEGER NOT NULL,
        nozesoucastanhas INTEGER NOT NULL,
        acucar INTEGER NOT NULL,
        foto BLOB,
        FOREIGN KEY (restaurante_id) REFERENCES restaurantes (id_restaurante)
        )
    """

checar_senha = "SELECT * FROM restaurantes WHERE name == ?"

cursor.execute(criacao_de_tabela)
cursor.execute(tabela_filha)

cursor.execute("INSERT INTO restaurantes (email, senha) VALUES (?, ?)", ("batata", "batata"))

conn.commit()

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/<restaurante>/cardapio", methods=["POST"])
def get_data():
    return

@app.route("/<restaurante>")
def hello(restaurante):
    name = restaurante
    return f"<h1>The name of this restaurant is {name} </h1>"

@app.route("/login")
def login():
    return render_template("create_account.html")

@app.route("/process_form", methods=["POST"])
def get_coisas():
    email = request.form.get("email")
    senha = request.form.get("senha")
    print(email)
    cursor.execute("SELECT * FROM restaurantes WHERE name = ?", ( str(email) ) )
    results = cursor.fetchall()
    print(results)


if __name__ == "__main__":
    app.run(debug=True)
