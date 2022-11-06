from flask import Flask, redirect, url_for, render_template, request
from flask import jsonify, json
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import  InputRequired
import models as models

app = Flask(__name__)

#Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sophr@@t1'
app.config['MYSQL_DB'] = 'students'
app.config['SECRET_KEY'] = 'secret secret'

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
    submit = SubmitField("Add")

class CollegeForm(FlaskForm):
    code = StringField("Code", validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    submit = SubmitField("Add")

class CourseForm(FlaskForm):
    code = StringField("Code", validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    college = SelectField("College", choices=[], validate_choice=False)
    submit = SubmitField("Add")

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[InputRequired()])
    submit = SubmitField("Submit")

def append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value


@app.route("/search", methods =["POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        searched = form.searched.data
        return render_template("search.html", form=form, searched=searched)

@app.route("/home")
def home():
    studentsList=models.Students.all(mydb)
    return render_template("index.html", studentsList = studentsList)

@app.route("/courses")
def courses():
    coursesList = models.Courses.all(mydb)
    return render_template("courses.html", coursesList = coursesList)

@app.route("/colleges")
def colleges():
    collegesList = models.Colleges.all(mydb)
    return render_template("colleges.html", collegesList = collegesList)

@app.route('/delete/<data_id>')
def delete(data_id):
    if models.Students.delete(mydb, data_id):
        return redirect('/home')
    else:
        return "There was a problem"

@app.route('/edit/<data_id>', methods =["POST","GET"])
def edit_student(data_id):
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

@app.route("/users",methods =["POST","GET"])
def users():
    if request.method == "POST":
        #userDetails = request.form
        #name = userDetails['name']
        #email = userDetails['password']
        #mycursor = mydb.connection.cursor()

        #sql = "INSERT INTO students(name, email) VALUES (%s, %s)"
        #mycursor.execute(sql, (name,email))

        #mydb.connection.commit()
        #mycursor.close()

        return redirect('/students')
    else:
        return render_template("register.html")

@app.route("/",methods =["POST","GET"])
def register():
    if request.method == "POST":
        #userDetails = request.form
        #name = userDetails['name']
        #email = userDetails['password']
        #mycursor = mydb.connection.cursor()

        #sql = "INSERT INTO students(name, email) VALUES (%s, %s)"
        #mycursor.execute(sql, (name,email))

        #mydb.connection.commit()
        #mycursor.close()

        return redirect('/students')
    else:
        return render_template("register.html")

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

@app.route('/courses/add', methods = ['GET', 'POST'])
def add_courses():
    form = CourseForm()
    colleges = models.Colleges.all(mydb)
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if form.validate_on_submit():
        #course = models.Courses(form.code.data, form.name.data, form.college.data)
        #course.add(mydb)
        return redirect('/home')
    return render_template("add_course.html", form=form)

@app.route('/colleges/add', methods = ['GET', 'POST'])
def add_colleges():
    form = CollegeForm()
    if form.validate_on_submit():
        #course = models.Courses(form.code.data, form.name.data, form.college.data)
        #course.add(mydb)
        return redirect('/home')
    return render_template("add_college.html", form=form)

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



if __name__ == "__main__":
    app.run(debug=True)