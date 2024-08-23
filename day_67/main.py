from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, inspect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
Bootstrap5(app)
ckeditor = CKEditor()
ckeditor.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    inspector = inspect(db.engine)
    # check if the DB exists
    if not inspector.has_table('blog_post'):
        db.create_all()


# WTFORMS Post Forms
class PostForm(FlaskForm):
    blog_title = StringField('Title', validators=[DataRequired()])
    blog_subtitle = StringField('Subtitle', validators=[DataRequired()])
    blog_author = StringField('Author', validators=[DataRequired()])
    blog_img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    blog_body = CKEditorField('Body', validators=[DataRequired()])
    blog_submit = SubmitField('Submit')


# Routes
# home page
@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    all_posts = result.scalars().all()
    posts = [{
        "id": post.id,
        "title": post.title,
        "date": post.date,
        "body": post.body,
        "author": post.author,
        "img_url": post.img_url,
        "subtitle": post.subtitle,
    } for post in all_posts]
    return render_template("index.html", all_posts=posts)


# show the chosen post
@app.route('/blog/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# creating new posts
@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        new_post = BlogPost(
            title=post_form.blog_title.data,
            subtitle=post_form.blog_subtitle.data,
            date=date.today().strftime("%B %d, %Y"),
            body=post_form.blog_body.data,
            author=post_form.blog_author.data,
            img_url=post_form.blog_img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=post_form)


# Editing Post
@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    # Autopopulate the form
    post_form = PostForm(
        blog_title=requested_post.title,
        blog_subtitle=requested_post.subtitle,
        blog_img_url=requested_post.img_url,
        blog_author=requested_post.author,
        blog_body=requested_post.body
    )
    if post_form.validate_on_submit():
        requested_post.title = post_form.blog_title.data
        requested_post.subtitle = post_form.blog_subtitle.data
        requested_post.body = post_form.blog_body.data
        requested_post.author = post_form.blog_author.data
        requested_post.img_url = post_form.blog_img_url.data
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=post_form, is_edit=True)


# Deleting Post
@app.route('/delete-post/<post_id>')
def delete_post(post_id):
    requested_deletion = db.get_or_404(BlogPost, post_id)
    db.session.delete(requested_deletion)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
