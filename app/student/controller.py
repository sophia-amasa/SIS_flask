from flask import render_template, redirect, jsonify, request
from app import cloudinary
from . import student_bp
import app.models as models
from app.student.forms import StudentForm, EditForm, SearchForm   

@student_bp.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@student_bp.route("/search", methods =["POST"])
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        searched = form.searched.data
        field = form.select.data
        if field == 'Student':
            result = models.Students.search(searched)
            if result:
                return render_template("search.html", searched=searched, studentsList=result)
            else:
                return render_template("search.html", searched=searched, NoResult=result)
        elif field == 'Course':
            result = models.Courses.search(searched)
            if result:
                return render_template("search.html", searched=searched, coursesList=result)
            else:
                return render_template("search.html", searched=searched, NoResult=result)
        elif field == 'College':
            result =  models.Colleges.search(searched)
            if result:
                return render_template("search.html", searched=searched, collegesList=result)
            else:
                return render_template("search.html", searched=searched, NoResult=result)
            
@student_bp.route('/students', methods = ['GET', 'POST'])
def students():
    form = StudentForm()
    colleges = models.Colleges.all()
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if request.method == 'POST' and form.validate_on_submit():
        student_ID = form.id_year.data + '-' + form.id_num.data
        try:
            int(form.id_year.data)
            int(form.id_num.data)
        except:
            return("Cannot")
        print(form.profile_pic.data)
        result = cloudinary.uploader.upload(form.profile_pic.data)
        url = result.get("url")
        student = models.Students(student_ID, form.name.data, form.college.data, form.course.data, form.year.data,  form.gender.data, url)
        student.add()
        return redirect('/home')
    return render_template("add_student.html", form=form)

@student_bp.route('/students/delete/<data_id>')
def delete_student(data_id):
    if models.Students.delete(data_id):
        return redirect('/home')
    else:
        return "There was a problem"

@student_bp.route('/edit/<data_id>', methods =["POST","GET"])
def edit_student(data_id):
    form = EditForm()
    colleges = models.Colleges.all()
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if request.method == 'GET':
        details = models.Students.search(data_id)
        form.id_year.data = details[0][0][:4]
        form.id_num.data = details[0][0][5:]
        form.name.data = details[0][1]
        form.college.data = details[0][2]
        form.year.data = details[0][4]
        form.gender.data = details[0][5]
    if request.method == 'POST' and form.validate_on_submit():
        student_ID = form.id_year.data + '-' + form.id_num.data
        try:
            int(form.id_year.data)
            int(form.id_num.data)
        except:
            return("Cannot")
        if form.profile_pic.data:
            result = cloudinary.uploader.upload(form.profile_pic.data)
            url = result.get("url")
        else:
            url = 'https://res.cloudinary.com/dfnna5cnx/image/upload/v1669059613/nfivhkrflzk0rmtlyrkt.png'
        student = models.Students(student_ID, form.name.data, form.college.data, form.course.data, form.year.data, form.gender.data, url)
        student.edit(data_id)
        return redirect('/home')
    return render_template("edit_student.html", form=form, data_id=data_id)

@student_bp.route("/home")
def home():
    studentsList=models.Students.all()
    return render_template("index.html", studentsList = studentsList)

@student_bp.route('/students/<get_college>')
def get_course(get_college):
    colleges = models.Colleges.get_college_from_course(get_college)
    coursesArray = []
    for course in colleges:
        courseObj = {}
        courseObj['id'] = course[0]
        courseObj['name'] = course[1]
        coursesArray.append(courseObj)
    return jsonify({'courselist' : coursesArray})

@student_bp.route('/edit/<id>/<get_college>')
def get_id_course(id,get_college):
    colleges = models.Colleges.get_college_from_course(get_college)
    coursesArray = []
    for course in colleges:
        courseObj = {}
        courseObj['id'] = course[0]
        courseObj['name'] = course[1]
        coursesArray.append(courseObj)
    return jsonify({'courselist' : coursesArray})