from flask import Flask
from flask_mysqldb import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL, CLOUD_NAME, API_KEY, API_SECRET
from flask_wtf.csrf import CSRFProtect
import cloudinary
import cloudinary.uploader

mydb = MySQL()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['MYSQL_HOST'] = DB_HOST
    app.config['MYSQL_USER'] = DB_USERNAME
    app.config['MYSQL_PASSWORD'] = DB_PASSWORD
    app.config['MYSQL_DB'] = DB_NAME
    app.config['SECRET_KEY'] = SECRET_KEY

    cloudinary.config( 
        cloud_name = CLOUD_NAME, 
        api_key = API_KEY, 
        api_secret = API_SECRET 
    )

    mydb.init_app(app)
    CSRFProtect(app)

    from .user import user_bp as user_blueprint
    app.register_blueprint(user_blueprint)

    from .student import student_bp as student_blueprint
    app.register_blueprint(student_blueprint)

    from .course import course_bp as course_blueprint
    app.register_blueprint(course_blueprint)

    from .college import college_bp as college_blueprint
    app.register_blueprint(college_blueprint)

    return app