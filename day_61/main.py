from flask import Flask, render_template, request, redirect, url_for
from login_forms import LoginForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = 'placeholder'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        print(email, password)
        if email == 'admin@email.com' and password == '12345678':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=login_form)


@app.route("/success")
def success():
    return render_template('success.html')


@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
