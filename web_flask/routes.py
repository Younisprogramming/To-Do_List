from flask import render_template, url_for, flash, redirect
from web_flask import app, db, bcrypt
from web_flask.forms import RegistrationForm, LoginForm
from web_flask.models import User, Todo
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'younis',
        'title': 'todo 1',
        'content': 'First todo content',
        'date_posted': ' 9/8/2024'
    },
    {
        'author': 'mina talla',
        'title': 'todo 2',
        'content': 'Second second content',
        'date_posted': '9/8/2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('register'))

@app.route("/dashboard")
@login_required 
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
    