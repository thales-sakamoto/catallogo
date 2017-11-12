import src.product.models
from src.common.database import Database
from src.models.user import User
from src.models.produto2 import Produto2

import os

__author__ = 'jslvtr'

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def home_template():
    return render_template('home.html')


@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route('/register')
def register_template():
    return render_template('registro.html')


@app.route('/catalogo')
def abre_catalogo():
    return render_template('home_produtos.html', products=src.product.models.PRODUCTS)

@app.route('/catalogo2')
def abre_catalogo2():
    resposta = Database.find(collection="produtos", query={})
    for r in resposta:
        return r['nome']

@app.route('/catalogo3')
def abre_catalogo3():
    post_data = Database.find(collection='produtos', query={})
    posts = [post for post in post_data]
    return render_template('posts.html', posts=posts)

def retorna_lista():
    post_data = Database.find(collection='produtos', query={})
    return [post for post in post_data]

@app.route('/register2')
def register_template2():
    return render_template('insere_produto.html')


@app.route('/product/<key>')
def product(key):
    product = src.product.models.PRODUCTS.get(key)
    if not product:
        os.abort(404)
    return render_template('product.html', product=product)


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template("profile.html", email=session['email'])


@app.route('/auth/produto', methods=['POST'])
def register_produto():
    nome = request.form['Nome']
    preco = request.form['Preco']
    descricao = request.form['Descricao']
    Produto3 = Produto2(nome, preco, descricao,_id=None)
    Produto3.save_to_mongo()
    return render_template("produto_cadastrado.html", produto=nome)


def busca_produtos():
    return Database.find(collection="produtos", query={})


if __name__ == '__main__':
    app.run(port=4995, debug=True)
