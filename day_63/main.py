from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from sqlalchemy import inspect
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from dataBase import Book, db
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("SQLALCHEMY_DATABASE_URI")
Bootstrap5(app)
# Initialize the db with the app
db.init_app(app)


class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    book_rating = FloatField('Ratings', validators=[DataRequired()])
    submit = SubmitField('Submit')


# check if DB exist, if not create DB
with app.app_context():
    inspector = inspect(db.engine)
    # check if the DB exists
    if not inspector.has_table('book'):
        db.create_all()


@app.route('/')
def home():
    with app.app_context():
        # reading through the DB
        DB_books = db.session.query(Book).all()
        all_books = []
        for book in DB_books:
            all_books.append(book)
            print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add_book():
    book_forms = BookForm()
    if book_forms.validate_on_submit():
        # adding data to DB
        with app.app_context():
            insert_data = Book(title=book_forms.book_name.data,
                               author=book_forms.book_author.data,
                               rating=float(book_forms.book_rating.data))
            db.session.add(insert_data)
            db.session.commit()

        # all_books.append(new_book)
        return redirect(url_for('home'))

    return render_template('add.html', form=book_forms)


if __name__ == "__main__":
    app.run(debug=True)
