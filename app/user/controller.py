from flask import render_template, redirect, request
from . import user_bp
#import app.models as models
from app.user.forms import UserForm

@user_bp.route("/",methods =["POST","GET"])
def register():
    form = UserForm()
    if request.method == "POST" and form.validate_on_submit():
        return redirect('/home')
    else:
        return render_template("register.html", form = form)          