from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, inspect
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# secret api key given to user
SECRET_API_KEY = "TopSecretAPIKey"


# Cafe TABLE Configuration
class CafeDB(db.Model):
    __tablename__ = 'cafe'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


# check if DB exist, if not create DB
with app.app_context():
    inspector = inspect(db.engine)
    # check if the DB exists
    if not inspector.has_table('cafe'):
        db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP POST - Create Record
@app.route("/random")
def get_random_cafe():
    with app.app_context():
        # randomly chooses cafe
        random_cafe = db.session.execute(db.select(CafeDB).order_by(db.sql.func.random()).limit(1)).scalar()
        print(random_cafe)

        # Convert the result to a list of dictionaries
        return jsonify(cafe={
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        })


@app.route("/all")
def get_all_cafe():
    with app.app_context():
        # randomly chooses cafe
        result = db.session.execute(db.select(CafeDB))
        all_cafes = result.scalars().all()

        # Convert the result to a list of dictionaries
        cafes_list = [{
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        } for cafe in all_cafes]

        return jsonify(cafes=cafes_list)


@app.route("/search/<string:loc>")
def get_searched_cafe(loc):
    with app.app_context():
        query_location = loc

        if not query_location:
            return jsonify({"error": "Location parameter is missing"}), 400

        result = db.session.execute(db.select(CafeDB).where(CafeDB.location == query_location))
        matching_cafes = result.scalars().all()

        if not matching_cafes:
            return jsonify({"error": "No cafes found for the given location"}), 404

        return jsonify(cafes=[{
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        } for cafe in matching_cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    with app.app_context():
        # add new cafe info
        new_cafe = CafeDB(
            name=request.form.get('name'),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price")
        )

        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "Cafe successfully created"})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    # params
    new_price = request.args.get("new_price")
    # find cafe via ID
    selected_cafe = db.get_or_404(CafeDB, cafe_id)
    # update the price
    if selected_cafe:
        selected_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_close(cafe_id):
    # user's inputted api key
    api_key = request.args.get("api_key")
    # find dead cafe
    selected_cafe = db.get_or_404(CafeDB, cafe_id)
    # if secret api key is correct, they are authorized to delete the cafe
    if api_key == SECRET_API_KEY:
        if selected_cafe:
            db.session.delete(selected_cafe)
            db.session.commit()
            return jsonify(Success={"Cafe Deleted": "The closed Cafe has been deleted."}), 200

        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 400
    else:
        return jsonify(error={"API Not Matched": "You are not authorized to have access to this data."}), 400


if __name__ == '__main__':
    app.run(debug=True)
