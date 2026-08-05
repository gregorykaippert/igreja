# forms
from igreja import bcrypt
from igreja.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, length, EqualTo, ValidationError
from email_validator import validate_email


class UserForm(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired('Obrigatório preencher o campo nickname!')])
    email = StringField('Email', validators=[DataRequired('Obrigatório preencher o campo email!'), Email(message='Insira um email válido!')])
    password = PasswordField('Password', validators=[DataRequired(message='Obrigatório o preenchimento do campo SENHA!'), length(6,15, message='Os campos senha e confirmar senha devem ter entre 6 a 15 caracteres!')])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(message='Obrigatório o preenchimento do campo CONFIRMAR SENHA!'), EqualTo('password', message='Os campos senha e confirmar senha devem ser iguais!')])
    button_register = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email já existente, faça login!')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    button_login = SubmitField('Log in')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Usuário {} não cadastrado, clique no botão REGISTRAR!'.format(email.data.upper()))

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not bcrypt.check_password_hash(user.password, password.data):
            raise ValidationError('Senha incorreta para o email {}.'.format(self.email.data.upper()))

