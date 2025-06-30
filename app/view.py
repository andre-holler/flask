from app import app
from flask import render_template

@app.route('/')
def homepage():
    usuario = 'Maria'
    idade = 16

    context = {
        'usuario':usuario,
        'idade':idade
    }
    
    return render_template('index.html', context=context)

@app.route('/contato')
def novapagina():
    return 'Outras views'
