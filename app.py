from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/cadastro_usuario')
def cadastrar():
    return render_template('cadastro_usuario.html')

@app.route('/login')
def logar():
    return render_template('login.html')

@app.route('/produtos')
def lista_produtos():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)