from app import app, db
from flask import render_template, url_for, request
from app.forms import ContatoForm

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
    

    return render_template('contato.html', context=context, form=form)

