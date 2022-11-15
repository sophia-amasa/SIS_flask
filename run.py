from flask import Flask, redirect, url_for, render_template, request
from flask import jsonify, json
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, RadioField, SelectField
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from wtforms.validators import  InputRequired
import models as models

app = Flask(__name__)

#Configure db
app.config['MYSQL_HOST'] = DB_HOST
app.config['MYSQL_USER'] = DB_USERNAME
app.config['MYSQL_PASSWORD'] = DB_PASSWORD
app.config['MYSQL_DB'] = DB_NAME
app.config['SECRET_KEY'] = SECRET_KEY

mydb = MySQL(app)

@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

class StudentForm(FlaskForm):
    id_year = StringField(validators=[InputRequired()])
    id_num = StringField(validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    college = SelectField("College", choices=[], validate_choice=False)
    course = SelectField("Course", choices=['Choose...'], validate_choice=False)
    year = SelectField("Year", choices=[1, 2, 3, 4], validate_choice=False)
    gender = RadioField("Gender",  choices=[("Male","Male"), ("Female","Female")], validate_choice=False)
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices, validate_choice=False)
    submit = SubmitField("Add")

class EditForm(FlaskForm):
    id_year = StringField(validators=[InputRequired()])
    id_num = StringField(validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    college = SelectField("College", choices=[], validate_choice=False)
    course = SelectField("Course", choices=['Choose...'], validate_choice=False)
    year = SelectField("Year", choices=[1, 2, 3, 4], validate_choice=False)
    gender = RadioField("Gender",  choices=[("Male","Male"), ("Female","Female")], validate_choice=False)
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices, validate_choice=False)
    submit = SubmitField("Add")

class CollegeForm(FlaskForm):
    code = StringField("Code", validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices, validate_choice=False)
    submit = SubmitField("Add")

class CourseForm(FlaskForm):
    code = StringField("Code", validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    college = SelectField("College", choices=[], validate_choice=False)
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices, validate_choice=False)
    submit = SubmitField("Add")

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[InputRequired()])
    choices=[('Student', 'Student'), ('Course', 'Course'), ('College', 'College')]
    select = SelectField('Search', choices=choices)
    submit = SubmitField("Submit")

@app.route("/search", methods =["POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        searched = form.searched.data
        field = form.select.data
        if field == 'Student':
            result = models.Students.search(mydb, searched)
            return render_template("search.html", searched=searched, studentsList=result, field = field)
        elif field == 'Course':
            result = models.Courses.search(mydb, searched)
            return render_template("search.html", searched=searched, coursesList=result, field = field)
        elif field == 'College':
            result =  models.Colleges.search(mydb, searched)
            return render_template("search.html", searched=searched, collegesList=result, field = field)

@app.route("/home")
def home():
    studentsList=models.Students.all(mydb)
    return render_template("index.html", studentsList = studentsList)

@app.route("/courses", methods = ['GET', 'POST'])
def courses():
    coursesList = models.Courses.all(mydb)
    return render_template("courses.html", coursesList = coursesList)

@app.route('/courses/add', methods = ['GET', 'POST'])
def add_courses():
    form = CourseForm()
    colleges = models.Colleges.all(mydb)
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if form.validate_on_submit():
        course = models.Courses(form.code.data, form.name.data, form.college.data)
        course.add(mydb)
        return redirect('/courses')
    return render_template("add_course.html", form=form)

@app.route('/courses/delete/<course_code>')
def delete_course(course_code):
    if models.Courses.delete(mydb, course_code):
        return redirect('/courses')
    else:
        return "There was a problem"

@app.route('/courses/edit/<course_code>', methods = ["POST","GET"])
def edit_course(course_code):
    form = CourseForm()
    colleges = models.Colleges.all(mydb)
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if form.validate_on_submit():
        course = models.Courses(form.code.data, form.name.data, form.college.data)
        course.edit(mydb,course_code)
        return redirect('/courses')
    return render_template("edit_course.html", form=form, course_code=course_code)

@app.route("/colleges", methods = ['GET', 'POST'])
def colleges():
    collegesList = models.Colleges.all(mydb)
    return render_template("colleges.html", collegesList = collegesList)

@app.route('/colleges/add', methods = ['GET', 'POST'])
def add_colleges():
    form = CollegeForm()
    if form.validate_on_submit():
        college = models.Colleges(form.code.data, form.name.data)
        college.add(mydb)
        return redirect('/colleges')
    return render_template("add_college.html", form=form)

@app.route('/colleges/edit/<course_code>', methods = ["POST","GET"])
def edit_college(course_code):
    form = CollegeForm()
    if form.validate_on_submit():
        college = models.Colleges(form.code.data, form.name.data)
        college.edit(mydb,course_code)
        return redirect('/colleges')
    return render_template("edit_college.html", form=form, course_code=course_code)

@app.route('/colleges/delete/<college_code>')
def delete_college(college_code):
    if models.Colleges.delete(mydb, college_code):
        return redirect('/colleges')
    else:
        return "There was a problem"

@app.route('/students', methods = ['GET', 'POST'])
def students():
    form = StudentForm()
    colleges = models.Colleges.all(mydb)
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if form.validate_on_submit():
        student_ID = form.id_year.data + '-' + form.id_num.data
        try:
            int(form.id_year.data)
            int(form.id_num.data)
        except:
            return("Cannot")
        student = models.Students(student_ID, form.name.data, form.college.data, form.course.data, form.year.data, form.gender.data)
        student.add(mydb)
        return redirect('/home')
    return render_template("add_student.html", form=form)

@app.route('/students/delete/<data_id>')
def delete_student(data_id):
    if models.Students.delete(mydb, data_id):
        return redirect('/home')
    else:
        return "There was a problem"

@app.route('/edit/<data_id>', methods =["POST","GET"])
def edit_student(data_id):
    form = EditForm()
    colleges = models.Colleges.all(mydb)
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if form.validate_on_submit():
        student_ID = form.id_year.data + '-' + form.id_num.data
        try:
            int(form.id_year.data)
            int(form.id_num.data)
        except:
            return("Cannot")
        student = models.Students(student_ID, form.name.data, form.college.data, form.course.data, form.year.data, form.gender.data)
        student.edit(mydb,data_id)
        return redirect('/home')
    return render_template("edit_student.html", form=form, data_id=data_id)

@app.route("/",methods =["POST","GET"])
def register():
    if request.method == "POST":
        return redirect('/home')
    else:
        return render_template("register.html")

@app.route('/students/<get_college>')
def get_course(get_college):
    colleges = models.Colleges.get_college_from_course(mydb, get_college)
    coursesArray = []
    for course in colleges:
        courseObj = {}
        courseObj['id'] = course[0]
        courseObj['name'] = course[1]
        coursesArray.append(courseObj)
    return jsonify({'courselist' : coursesArray})

@app.route('/edit/<id>/<get_college>')
def edit_get_course(id,get_college):
    colleges = models.Colleges.get_college_from_course(mydb, get_college)
    coursesArray = []
    for course in colleges:
        courseObj = {}
        courseObj['id'] = course[0]
        courseObj['name'] = course[1]
        coursesArray.append(courseObj)
    return jsonify({'courselist' : coursesArray})

if __name__ == "__main__":
    app.run(debug=True)