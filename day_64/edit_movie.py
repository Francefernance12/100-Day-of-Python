from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class EditMovie(FlaskForm):
    rating = FloatField('Your rating from 0 to 10', validators=[DataRequired()])
    review = StringField('Edit Review', validators=[DataRequired()])
    submit = SubmitField('Done')

