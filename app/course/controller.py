from flask import render_template, redirect, request
from . import course_bp
import app.models as models
from app.course.forms import CourseForm, SearchForm

@course_bp.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@course_bp.route("/search", methods =["POST"])
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

@course_bp.route("/courses", methods = ['GET', 'POST'])
def courses():
    coursesList = models.Courses.all()
    return render_template("courses.html", coursesList = coursesList)

@course_bp.route('/courses/add', methods = ['GET', 'POST'])
def add_courses():
    form = CourseForm()
    colleges = models.Colleges.all()
    form.college.choices = [(college[0],college[1]) for college in colleges]
    if request.method == 'POST' and form.validate_on_submit():
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
    if request.method == 'GET':
        details = models.Courses.search(course_code)
        form.code.data = details[0][0]
        form.name.data = details[0][1]
        form.college.data = details[0][2]
    if request.method == 'POST' and form.validate_on_submit():
        course = models.Courses(form.code.data, form.name.data, form.college.data)
        course.edit(course_code)
        return redirect('/courses')
    return render_template("edit_course.html", form=form, course_code=course_code)