from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['Secret_Key'] = 'ba79d314625ee40103217db43a6e536b'

posts =[
    {
    'author': 'Clayton Wagner',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2018'
    },
    {
    'author': 'Himothy Bonj',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 21, 2018'
    }


]
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'Success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form = form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data =='password':
            flash('You have been logged in!', 'Success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful Login, check username and password', 'danger')
    return render_template('Login.html', title='Login',form = form)

if __name__ =='__main__':
    app.run(debug=True)