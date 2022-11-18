from flask import render_template, redirect, jsonify
from . import student_bp
import app.models as models
from app.student.forms import StudentForm, EditForm      

@student_bp.route('/students', methods = ['GET', 'POST'])
def students():
    form = StudentForm()
    colleges = models.Colleges.all()
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if form.validate_on_submit():
        student_ID = form.id_year.data + '-' + form.id_num.data
        try:
            int(form.id_year.data)
            int(form.id_num.data)
        except:
            return("Cannot")
        student = models.Students(student_ID, form.name.data, form.college.data, form.course.data, form.year.data, form.gender.data)
        student.add()
        #result = cloudinary.uploader.upload(form.profile_pic.data)
        #url = result.get("url")

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
    if form.validate_on_submit():
        student_ID = form.id_year.data + '-' + form.id_num.data
        try:
            int(form.id_year.data)
            int(form.id_num.data)
        except:
            return("Cannot")
        student = models.Students(student_ID, form.name.data, form.college.data, form.course.data, form.year.data, form.gender.data)
        student.edit(data_id)
        return redirect('/home')
    return render_template("edit_student.html", form=form, data_id=data_id)

@student_bp.route("/home")
def home():
    studentsList=models.Students.all()
    return render_template("index.html", studentsList = studentsList)

@student_bp.route('/students/<get_college>')
@student_bp.route('/edit/<id>/<get_college>')
def get_course(id,get_college):
    colleges = models.Colleges.get_college_from_course(get_college)
    coursesArray = []
    for course in colleges:
        courseObj = {}
        courseObj['id'] = course[0]
        courseObj['name'] = course[1]
        coursesArray.append(courseObj)
    return jsonify({'courselist' : coursesArray})