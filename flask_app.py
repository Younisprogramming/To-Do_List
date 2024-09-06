from flask import Flask, redirect, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_wtf import FlaskForm, CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [ {
            'author': 'younis taher',
            'title': 'Blog Post 1',
            'age' : 21,
            'date_posted': 'April 20, 2018'
},
         {
             'author' : 'mina talla',
             'title' : 'Blog Post 2',
             'age' : 22,
             'date_posted' : 'April 21, 2018'
         }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)