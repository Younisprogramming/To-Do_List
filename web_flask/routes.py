from flask import render_template, url_for, flash, redirect
from web_flask import app
from web_flask.forms import RegistrationForm, LoginForm


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@todo.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)