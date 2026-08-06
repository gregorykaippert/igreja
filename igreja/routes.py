# routes

from flask import render_template, url_for, redirect, flash, request
from igreja import app, bcrypt, database
from flask_login import login_required, login_user, logout_user, current_user
from igreja.forms import UserForm, LoginForm
from igreja.models import User

@app.route("/", methods=["GET", "POST"])
def homepage():
    formLogin = LoginForm()
    user = User.query.filter_by(email=formLogin.email.data).first()
    if formLogin.validate_on_submit() and bcrypt.check_password_hash(user.password.encode('utf-8'), formLogin.password.data):
    # if formLogin.validate_on_submit() and bcrypt.check_password_hash(user.password, formLogin.password.data):
        login_user(user)
        flash('Seja bem vindo, ' + user.nickname + '!', 'success')
        return redirect(url_for('perfil', user=user.nickname ))
    else:
        print(formLogin.errors)
    return render_template("login.html", form=formLogin, rota=request.url_rule)

@app.route('/register', methods=["GET", "POST"])
def register():
    formUser = UserForm()
    if formUser.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(formUser.password.data).decode('utf-8')
        user = User(nickname=formUser.nickname.data,
                    email=formUser.email.data,
                    password=senha_cript)
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        flash('Usuário registrado com sucesso!', 'success')
        return redirect(url_for('perfil', user=user.nickname))
    # else:
    #     print(formUser.errors)
    return render_template("register.html", form=formUser, rota=request.url_rule)

@app.route("/contact")
def contact():
    users = User.query.all()
    return render_template("contact.html", users=users)
    for user in users:
        print(user.nickname)
    return 'ok'

@app.route("/about")
def about():
    return render_template("about.html", title="About me Greg rsrsrs")

@app.route('/perfil/<user>')
@login_required
def perfil(user):
    return render_template("perfil.html", user=user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'warning')
    return redirect(url_for('homepage'))

@app.route('/members', methods=['GET', 'POST'])
@login_required
def members():
    return render_template("members.html", rota=request.path)

@app.route('/teste')
def teste():
    formUser = UserForm()
    if formUser.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(formUser.password.data)
        user = User(nickname=formUser.nickname.data,
                    email=formUser.email.data,
                    password=senha_cript)
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        flash('Usuário registrado com sucesso!', 'success')
        return redirect(url_for('perfil', user=user.nickname))
    return render_template('register.html', form=formUser)