from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, RadioField, SelectField, FileField
from wtforms.validators import  InputRequired

class StudentForm(FlaskForm):
    id_year = StringField(validators=[InputRequired()])
    id_num = StringField(validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    college = SelectField("College", choices=[], validate_choice=False)
    course = SelectField("Course", choices=['Choose...'], validate_choice=False)
    year = SelectField("Year", choices=[1, 2, 3, 4, 5], validate_choice=False)
    gender = RadioField("Gender",  choices=[("Male","Male"), ("Female","Female")], validate_choice=False)
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices, validate_choice=False)
    profile_pic = FileField('Picture', validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Add")

class EditForm(FlaskForm):
    id_year = StringField(validators=[InputRequired()])
    id_num = StringField(validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    college = SelectField("College", choices=[], validate_choice=False)
    course = SelectField("Course", choices=['Choose...'], validate_choice=False)
    year = SelectField("Year", choices=[1, 2, 3, 4, 5], validate_choice=False)
    gender = RadioField("Gender",  choices=[("Male","Male"), ("Female","Female")], validate_choice=False)
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices, validate_choice=False)
    profile_pic = FileField('Picture', validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Add")

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[InputRequired()])
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices)
    submit = SubmitField("Submit")