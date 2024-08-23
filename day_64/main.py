from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from sqlalchemy import inspect
from movieDB import MovieDB, db
import requests
from dotenv import load_dotenv
from os import getenv
from edit_movie import EditMovie
from add_movie import AddMovie

load_dotenv()

# Secrets
TMDB_API_KEY = getenv('MOVIE_API_KEY')
TMDB_ACCESS_TOKEN = getenv('MOVIE_ACCESS_KEY')

# flask/Config/DB/Bootstrap5
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
Bootstrap5(app)
db.init_app(app)

# API URL
MOVIE_DB_SEARCH_URL = getenv('MOVIE_DB_SEARCH_URL')
MOVIE_DB_INFO_URL = getenv("MOVIE_DB_INFO_URL")
MOVIE_DB_IMAGE_URL = getenv("MOVIE_DB_IMAGE_URL")
tmdb_headers = {
    "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"
}

# check if DB exist, if not create DB
with app.app_context():
    inspector = inspect(db.engine)
    # check if the DB exists
    if not inspector.has_table('movie'):
        db.create_all()


@app.route("/")
def home():
    with app.app_context():
        # read DB
        movies_query = db.session.query(MovieDB).order_by(MovieDB.ranking.desc()).all()
        movies = []
        for movie in movies_query:
            movie_info = {
                'id': movie.id,
                'title': movie.title,
                'year': movie.year,
                'description': movie.description,
                'rating': movie.rating,
                'ranking': movie.ranking,
                'review': movie.review,
                'img_url': movie.img_url
            }
            movies.append(movie_info)
    return render_template("index.html", movies=movies)


@app.route("/add", methods=["POST", "GET"])
def add():
    add_form = AddMovie()
    if add_form.validate_on_submit():
        movie_title = add_form.movie_title.data
        movie_search_params = {
            "query": movie_title,
            "language": "en-US"
        }
        try:
            # Make a GET request
            search_response = requests.get(MOVIE_DB_SEARCH_URL, headers=tmdb_headers, params=movie_search_params)

            # Check if the request was successful (status code 200)
            if search_response.status_code == 200:
                # Extract and print the response data
                search_data = search_response.json()
                movie_list = [(movie['id'], movie['original_title'], movie['release_date']) for movie in search_data['results']]
                return render_template('select.html', movie_list=movie_list)

            else:
                # Print an error message if the request was unsuccessful
                print(f'Request failed with status code: {search_response.status_code}')
        except requests.RequestException as e:
            # Print an error message if an exception occurred during the request
            print(f'Request failed: {e}')
    return render_template("add.html", add_form=add_form)


@app.route("/edit/<int:movie_id>", methods=["POST", "GET"])
def edit(movie_id):
    # the selected movie
    selected_movie = MovieDB.query.get_or_404(movie_id)
    edit_form = EditMovie(obj=selected_movie)
    if edit_form.validate_on_submit():
        # Updating the information from DB using User's information
        selected_movie.rating = edit_form.rating.data
        selected_movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", edit_form=edit_form, movie=selected_movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    selected_movie = db.get_or_404(MovieDB, movie_id)
    db.session.delete(selected_movie)
    db.session.commit()
    print("Movie Deleted")
    return redirect(url_for('home'))


@app.route("/select", methods=["GET"])
def select():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        try:
            # Make a GET request
            movie_find_params = {
                # "movie_id": movie_api_id,
                "language": "en-US"
            }
            find_response = requests.get(f"{MOVIE_DB_INFO_URL}/{movie_api_id}", headers=tmdb_headers, params=movie_find_params)
            # Check if the request was successful (status code 200)
            if find_response.status_code == 200:
                # Extract and print the response data
                found_data = find_response.json()

                # Get the current highest ranking
                max_ranking = db.session.query(db.func.max(MovieDB.ranking)).scalar()
                new_ranking = (max_ranking or 0) + 1  # Increment the highest ranking

                new_movie = MovieDB(
                    title=found_data["original_title"],
                    # The data in release_date includes month and day, we will want to get rid of.
                    year=found_data["release_date"].split("-")[0],
                    description=found_data["overview"],
                    img_url=f"{MOVIE_DB_IMAGE_URL}{found_data['poster_path']}",
                    ranking=new_ranking
                )
                db.session.add(new_movie)
                db.session.commit()
                print(f"New movie added with ID: {new_movie.id}")
                return redirect(url_for("edit", movie_id=new_movie.id))
            # else:
            #     # Print an error message if the request was unsuccessful
            #     print(f'Request failed with status code: {find_response.status_code}')
        except requests.RequestException as e:
            # Print an error message if an exception occurred during the request
            print(f'Request failed: {e}')
    return render_template('select.html')


if __name__ == '__main__':
    app.run(debug=True)
