from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import ContatoForm
from app.models import Contato

@app.route('/')
def homepage():
    usuario = 'Maria'
    idade = 16

    context = {
        'usuario':usuario,
        'idade':idade
    }
    
    return render_template('index.html', context=context)


'''@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}

    if request.method =='POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = form(
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
        )

        db.session.add(contato)
        db.session.commit()


    return render_template('contato.html', context=context, form=form)'''

@app.route('/contato/', methods = ['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template('contato.html', context=context, form=form)


@app.route('/contato/lista/')
def contatoLista():

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    dados = Contato.query.order_by(Contato.nome)

    if pesquisa != '':
        dados = dados.filter(Contato.nome == pesquisa)

    context = {'dados':dados.all()}

    return render_template('contato_lista.html', context=context)
