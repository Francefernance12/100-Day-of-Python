import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, LoginManager, login_required, current_user, logout_user, login_user
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("SQLALCHEMY_DATABASE_URI")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login page if user is not authenticated


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)


# Create a user_loader callback to get User ID
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # user forms
        email = request.form.get('email')
        name = request.form.get('name')
        hash_salted_password = generate_password_hash(
            password=request.form.get('password'),
            salt_length=8
        )

        # checking if the user exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User already exists. Please log in.')
            return redirect(url_for('register'))

        # adding new user to DB
        new_user = User(
            name=name,
            email=email,
            password=hash_salted_password
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("You have successfully registered")
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # user info
        email = request.form.get('email')
        password = request.form.get('password')

        # find user by email entered to check if email exists or not
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # check if email and password are valid
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')  # Retrieve the 'next' parameter
            return redirect(next_page or url_for('secrets'))  # Redirect to next or secrets
        else:
            flash('Invalid credentials. Please try again.')
            redirect(url_for('login'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    # method logs user out
    logout_user()
    flash("You have successfully logged out")
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
