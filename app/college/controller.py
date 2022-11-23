from flask import render_template, redirect, request
from . import college_bp
import app.models as models
from app.college.forms import CollegeForm, SearchForm

@college_bp.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@college_bp.route("/search", methods =["POST"])
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

@college_bp.route("/colleges", methods = ['GET', 'POST'])
def colleges():
    collegesList = models.Colleges.all()
    return render_template("colleges.html", collegesList = collegesList)

@college_bp.route('/colleges/add', methods = ['GET', 'POST'])
def add_colleges():
    form = CollegeForm()
    if request.method == 'POST' and form.validate_on_submit():
        college = models.Colleges(form.code.data, form.name.data)
        college.add()
        return redirect('/colleges')
    return render_template("add_college.html", form=form)

@college_bp.route('/colleges/edit/<college_code>', methods = ["POST","GET"])
def edit_college(college_code):
    form = CollegeForm()
    if request.method == 'GET':
        details = models.Colleges.search(college_code)
        form.code.data = details[0][0]
        form.name.data = details[0][1]
    if request.method == 'POST' and form.validate_on_submit():
        college = models.Colleges(form.code.data, form.name.data)
        college.edit(college_code)
        return redirect('/colleges')
    return render_template("edit_college.html", form=form, college_code=college_code)

@college_bp.route('/colleges/delete/<college_code>')
def delete_college(college_code):
    if models.Colleges.delete(college_code):
        return redirect('/colleges')
    else:
        return "There was a problem"