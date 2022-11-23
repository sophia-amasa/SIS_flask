from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import  InputRequired

class CollegeForm(FlaskForm):
    code = StringField("Code", validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices, validate_choice=False)
    submit = SubmitField("Add")

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[InputRequired()])
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices)
    submit = SubmitField("Submit")