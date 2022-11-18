from flask import render_template, redirect
from . import college_bp
import app.models as models
from app.college.forms import CollegeForm

@college_bp.route("/colleges", methods = ['GET', 'POST'])
def colleges():
    collegesList = models.Colleges.all()
    return render_template("colleges.html", collegesList = collegesList)

@college_bp.route('/colleges/add', methods = ['GET', 'POST'])
def add_colleges():
    form = CollegeForm()
    if form.validate_on_submit():
        college = models.Colleges(form.code.data, form.name.data)
        college.add()
        return redirect('/colleges')
    return render_template("add_college.html", form=form)

@college_bp.route('/colleges/edit/<course_code>', methods = ["POST","GET"])
def edit_college(course_code):
    form = CollegeForm()
    if form.validate_on_submit():
        college = models.Colleges(form.code.data, form.name.data)
        college.edit(course_code)
        return redirect('/colleges')
    return render_template("edit_college.html", form=form, course_code=course_code)

@college_bp.route('/colleges/delete/<college_code>')
def delete_college(college_code):
    if models.Colleges.delete(college_code):
        return redirect('/colleges')
    else:
        return "There was a problem"