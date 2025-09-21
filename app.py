from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Usuario, Produto
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SECRET_KEY'] = "MEGA_SUPER_DIFICIL"

db.init_app(app)

with app.app_context():
    
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'logar'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_usuario', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        senha = request.form['password']
        
        if Usuario.query.filter_by(email=email).first():
            flash('Email já cadastrado. Tente outro email.', 'erro')
            return render_template('cadastro_usuario.html', usuario_existe=True)
        
        usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(usuario)
        db.session.commit()
        
       
        return redirect(url_for('logar'))
    
    return render_template('cadastro_usuario.html')

@app.route('/login', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']
        
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.senha == senha:
            login_user(usuario)
            flash('Login realizado com sucesso!', 'sucesso')
            return redirect(url_for('lista_produtos'))
        else:
            flash('Email ou senha incorretos.', 'erro')
    
    return render_template('login.html')

@app.route('/sair')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('index'))

@app.route('/produtos')
@login_required
def lista_produtos():
    produtos = Produto.query.all()
    return render_template('listar_produtos.html', produtos=produtos)

@app.route('/produtos/adicionar', methods=['GET', 'POST'])
@login_required
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        
        novo_produto = Produto(nome=nome, descricao=descricao, preco=preco)
        db.session.add(novo_produto)
        db.session.commit()
        
        flash('Livro adicionado com sucesso!', 'sucesso')
        return redirect(url_for('lista_produtos'))
    
    return render_template('adicionar_produtos.html')

@app.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_produto(id):
    produto = Produto.query.get(id)
    
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']
        produto.preco = request.form['preco']
        db.session.commit()
        
        flash('Livro atualizado com sucesso!', 'sucesso')
        return redirect(url_for('lista_produtos'))
    
    return render_template('editar_produtos.html', produto=produto)

@app.route('/produtos/excluir/<int:id>')
@login_required
def excluir_produto(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    
    flash('Livro excluído com sucesso!', 'sucesso')
    return redirect(url_for('lista_produtos'))

if __name__ == '__main__':
    app.run(debug=True)