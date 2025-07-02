from app import app
from flask import render_template, url_for, request

@app.route('/')
def homepage():
    usuario = 'Maria'
    idade = 16

    context = {
        'usuario':usuario,
        'idade':idade
    }
    
    return render_template('index.html', context=context)


@app.route('/contato/', methods=['GET', 'POST'])
def novapagina():
    context = {}

    if request.method == "GET":
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa':pesquisa})
        print(pesquisa)

    elif request.method == "POST":
        pesquisa = request.form['pesquisa']
        context.update({'pesquisa':pesquisa})
        print(pesquisa)



    return render_template('contato.html', context=context)
