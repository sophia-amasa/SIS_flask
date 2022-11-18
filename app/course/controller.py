from flask import render_template, redirect
from . import course_bp
import app.models as models
from app.course.forms import CourseForm

@course_bp.route("/courses", methods = ['GET', 'POST'])
def courses():
    print("i was here")
    coursesList = models.Courses.all()
    return render_template("courses.html", coursesList = coursesList)

@course_bp.route('/courses/add', methods = ['GET', 'POST'])
def add_courses():
    form = CourseForm()
    colleges = models.Colleges.all()
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if form.validate_on_submit():
        course = models.Courses(form.code.data, form.name.data, form.college.data)
        course.add()
        return redirect('/courses')
    return render_template("add_course.html", form=form)

@course_bp.route('/courses/delete/<course_code>')
def delete_course(course_code):
    if models.Courses.delete(course_code):
        return redirect('/courses')
    else:
        return "There was a problem"

@course_bp.route('/courses/edit/<course_code>', methods = ["POST","GET"])
def edit_course(course_code):
    form = CourseForm()
    colleges = models.Colleges.all()
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if form.validate_on_submit():
        course = models.Courses(form.code.data, form.name.data, form.college.data)
        course.edit(course_code)
        return redirect('/courses')
    return render_template("edit_course.html", form=form, course_code=course_code)