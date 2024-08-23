from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv
from dotenv import load_dotenv
import os

# loading environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
Bootstrap5(app)

# Choices
coffee_rating_choices = [('1', '️✘'), ('2', '☕️'), ('3', '☕️☕️'), ('4', '☕️☕️☕️'), ('5', '☕️☕️☕☕️'), ('6', '☕️☕️☕️☕☕')]
wifi_rating_choices = [('1', '️✘'), ('2', '💪'), ('3', '💪️💪'), ('4', '💪💪💪'), ('5', '💪💪💪💪'), ('6', '💪💪💪💪💪')]
power_rating_choices = [('1', '️✘'), ('2', '🔌'), ('3', '🔌🔌'), ('4', '🔌🔌🔌'), ('5', '🔌🔌🔌🔌'), ('6', '🔌🔌🔌🔌🔌')]


# forms
class CafeForm(FlaskForm):
    # Inputs
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location_url = StringField('Cafe Location', validators=[DataRequired()])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    # Dropdown Choices
    coffee_rating = SelectField('Rate the coffee', choices=coffee_rating_choices)
    wifi_rating = SelectField('Rate the WIFI', choices=wifi_rating_choices)
    power_outlet_rating = SelectField('Rate the power', choices=power_rating_choices)
    # Submit
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        format_form = [
            form.cafe.data,
            form.cafe_location_url.data,
            form.open_time.data.replace('\u202f', ''),
            form.closing_time.data.replace('\u202f', ''),
        ]

        # Define a function to handle the rating conversion
        def convert_rating(rating, symbol):
            return symbol * (int(rating) - 1) if int(rating) != 0 else '✘'

        # Append the formatted ratings
        format_form.append(convert_rating(form.coffee_rating.data, '☕'))
        format_form.append(convert_rating(form.wifi_rating.data, '💪'))
        format_form.append(convert_rating(form.power_outlet_rating.data, '🔌'))

        print(format_form)

        # Add the new data into the csv file
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as cafe_file:
            writer = csv.writer(cafe_file)
            writer.writerow(format_form)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = [row for row in csv_data]
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
