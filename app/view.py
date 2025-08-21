from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import ContatoForm, UserForm, LoginForm, PostForm, PostComentariosForm
from app.models import Contato, User, Post, PostComentarios
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/', methods=['GET', 'POST'])
def homepage():
    usuario = 'Maria'
    idade = 16
    form = LoginForm()

    context = {
        'usuario':usuario,
        'idade':idade
    }

    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)


    
    return render_template('index.html', context=context, form=form)


@app.route('/contato/', methods = ['GET', 'POST'])
@login_required
def contato():
    form = ContatoForm()
    context = {}

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template('contato.html', context=context, form=form)


@app.route('/contato/lista/')
@login_required
def contatoLista():

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    dados = Contato.query.order_by(Contato.nome)

    if pesquisa != '':
        dados = dados.filter(Contato.nome == pesquisa)

    context = {'dados':dados.all()}

    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>')
def contatoDetail(id):
    obj=Contato.query.get(id)
    return render_template('contato_detail.html', obj=obj)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = UserForm()

    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))

    return render_template('cadastro.html', form=form)

@app.route('/sair/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/post/novo', methods=['GET', 'POST'])
@login_required
def PostNovo():
    form = PostForm()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('homepage'))
    return render_template('post_novo.html', form=form)


@app.route('/post/lista')
@login_required
def PostLista():
    posts = Post.query.all()
    return render_template('post_lista.html', posts=posts)

@app.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def PostDetail(id):
    post = Post.query.get_or_404(id)
    form = PostComentariosForm()

    if form.validate_on_submit():
        form.save(current_user.id, id)
        return redirect(url_for('PostDetail', id=id))

    return render_template('post.html', post=post, form=form)
