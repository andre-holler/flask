from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app import db, bcrypt
from app.models import Contato, User, Post

class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Enviar')   

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Usuário já cadastro com esse E-Mail')
        
    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        print('aaa')

        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha
        )

        print(user)

        db.session.add(user)
        db.session.commit()
        return user

class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()

class LoginForm(FlaskForm):
    nome_usuario = StringField('Nome de Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')

    def login(self):
        user = User.query.filter_by(nome_usuario=self.nome_usuario.data).first()

        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                return user
            
            else:
                raise Exception('Senha incorreta')
            
        else:
            raise Exception('Usuário não encontrado')
        
class PostForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id):
        post = Post(
            titulo = self.titulo.data,
            mensagem = self.mensagem.data,
            user_id = user_id
        )

        db.session.add(post)
        db.session.commit()