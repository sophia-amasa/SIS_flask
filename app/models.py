from app import mydb

class Students():

    def __init__(self, id_num=None, name=None, college=None, course=None, year=None, gender=None):
        self.id = id_num
        self.name = name
        self.college = college
        self.course = course
        self.year = year
        self.gender = gender

    def add(self):
        cursor = mydb.connection.cursor()

        sql = "INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.id, self.name, self.college, self.course, self.year, self.gender))

        mydb.connection.commit()

    def all():
        cursor = mydb.connection.cursor()
        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def delete(data_id):
        try:
            cursor = mydb.connection.cursor()
            sql = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(sql,(data_id,))
            mydb.connection.commit()
            return True
        except:
            return False

    def edit(self, data_id):
        cursor = mydb.connection.cursor()

        sql = "UPDATE students SET student_id = %s, full_name = %s, college = %s, course_code = %s, year_level = %s, gender = %s where student_id = %s"
        cursor.execute(sql, (self.id, self.name, self.college, self.course, self.year, self.gender,data_id))

        mydb.connection.commit()
    
    def search(searched):
        cursor = mydb.connection.cursor()
        sql = "SELECT * FROM students WHERE %s in (student_id, full_name, college, course_code, year_level, gender)"
        cursor.execute(sql, (searched, ))
        result = cursor.fetchall()
        return result
    
    def search(searched):
        cursor = mydb.connection.cursor()
        sql = "SELECT * FROM students WHERE %s IN (student_id, full_name, college, course_code, year_level, gender);"
        resultValue = cursor.execute(sql, (searched,))
        if resultValue > 0:
            result = cursor.fetchall()
        else:
            return False
        return result

class Colleges():
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name


    def add(self):
        cursor = mydb.connection.cursor()

        sql = "INSERT INTO colleges VALUES (%s, %s)"
        cursor.execute(sql, (self.code, self.name))

        mydb.connection.commit()

    def all():
        cursor = mydb.connection.cursor()

        sql = "SELECT * from colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def get_college_from_course(college):
        cursor = mydb.connection.cursor()
        resultValue = cursor.execute("SELECT * FROM course_info where college = %s", (college,))
        if resultValue > 0:
            colleges = cursor.fetchall()
        return colleges

    def delete(code):
        try:
            cursor = mydb.connection.cursor()
            sql = "DELETE FROM colleges WHERE CollegeCode = %s"
            cursor.execute(sql,(code,))
            mydb.connection.commit()
            return True
        except:
            return False

    def edit(self, college_code):
        cursor = mydb.connection.cursor()

        sql = "UPDATE colleges SET CollegeCode = %s, CollegeName = %s WHERE CollegeCode = %s"
        cursor.execute(sql, (self.code, self.name, college_code))

        mydb.connection.commit()

    def search(searched):
        cursor = mydb.connection.cursor()
        sql = "SELECT * from colleges where %s in (CollegeCode, CollegeName)"
        cursor.execute(sql, (searched, ))
        result = cursor.fetchall()
        return result

class Courses():
    def __init__(self, code=None, name=None, college=None):
        self.code = code
        self.name = name
        self.college = college

    def add(self):
        cursor = mydb.connection.cursor()

        sql = "INSERT INTO course_info VALUES (%s, %s,%s)"
        cursor.execute(sql, (self.code, self.name, self.college))

        mydb.connection.commit()

    def all():
        cursor = mydb.connection.cursor()
        sql = "SELECT * from course_info"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def delete(code):
        try:
            cursor = mydb.connection.cursor()
            sql = "DELETE FROM course_info WHERE course_code = %s"
            cursor.execute(sql,(code,))
            mydb.connection.commit()
            return True
        except:
            return False

    def edit(self, course_code):
        cursor = mydb.connection.cursor()

        sql = "UPDATE course_info SET course_code = %s, course = %s, college = %s WHERE course_code = %s"
        cursor.execute(sql, (self.code, self.name, self.college, course_code))

        mydb.connection.commit()

    def search(searched):
        cursor = mydb.connection.cursor()
        sql = "SELECT * from course_info where %s in (course_code, course, college)"
        cursor.execute(sql, (searched, ))
        result = cursor.fetchall()
        return result
        
