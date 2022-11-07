class Students():

    def __init__(self, id_num=None, name=None, college=None, course=None, year=None, gender=None):
        self.id = id_num
        self.name = name
        self.college = college
        self.course = course
        self.year = year
        self.gender = gender

    def add(self, mysql):
        cursor = mysql.connection.cursor()

        sql = "INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.id, self.name, self.college, self.course, self.year, self.gender))

        mysql.connection.commit()

    def all(mysql):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def delete(mysql, data_id):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(sql,(data_id,))
            mysql.connection.commit()
            return True
        except:
            return False

    def edit(self, mysql, data_id):
        cursor = mysql.connection.cursor()

        sql = "UPDATE students SET student_id = %s, full_name = %s, college = %s, course_code = %s, year_level = %s, gender = %s where student_id = %s"
        cursor.execute(sql, (self.id, self.name, self.college, self.course, self.year, self.gender,data_id))

        mysql.connection.commit()
    
    def search(mysql, searched):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM students WHERE %s in (student_id, full_name, college, course_code, year_level, gender)"
        cursor.execute(sql, (searched, ))

        result = cursor.fetchall()

        return result
    
    def get_student(mysql, data_id):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from students where student_id = %s"
        cursor.execute(sql, (data_id,))
        result = cursor.fetchone()
        return result

class Colleges():
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name


    def add(self, mysql):
        cursor = mysql.connection.cursor()

        sql = "INSERT INTO colleges VALUES (%s, %s)"
        cursor.execute(sql, (self.code, self.name))

        mysql.connection.commit()

    def all(mysql):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def get_college_from_course(mysql, college):
        cursor = mysql.connection.cursor()
        resultValue = cursor.execute("SELECT * FROM course_info where college = %s", (college,))
        if resultValue > 0:
            colleges = cursor.fetchall()
        return colleges


    def delete(mysql, code):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM colleges WHERE CollegeCode = %s"
            cursor.execute(sql,(code,))
            mysql.connection.commit()
            return True
        except:
            return False

    def edit(self, mysql, college_code):
        cursor = mysql.connection.cursor()

        sql = "UPDATE colleges SET CollegeCode = %s, CollegeName = %s WHERE CollegeCode = %s"
        cursor.execute(sql, (self.code, self.name, college_code))

        mysql.connection.commit()

class Courses():
    def __init__(self, code=None, name=None, college=None):
        self.code = code
        self.name = name
        self.college = college

    def add(self, mysql):
        cursor = mysql.connection.cursor()

        sql = "INSERT INTO course_info VALUES (%s, %s,%s)"
        cursor.execute(sql, (self.code, self.name, self.college))

        mysql.connection.commit()

    def all(mysql):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from course_info"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def delete(mysql, code):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM course_info WHERE course_code = %s"
            cursor.execute(sql,(code,))
            mysql.connection.commit()
            return True
        except:
            return False

    def edit(self, mysql, course_code):
        cursor = mysql.connection.cursor()

        sql = "UPDATE course_info SET course_code = %s, course = %s, college = %s WHERE course_code = %s"
        cursor.execute(sql, (self.code, self.name, self.college, course_code))

        mysql.connection.commit()
        
