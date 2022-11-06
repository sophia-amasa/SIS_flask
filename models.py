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

class Colleges():
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name

    """
    def add(self):
        cursor = self.mysql.connection.cursor()

        sql = "INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.id, self.name, self.college, self.course, self.year, self.gender))

        self.mysql.connection.commit()"""

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

"""
    def delete(self):
        try:
            cursor = self.mysql.connection.cursor()
            sql = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(sql,(self.data_id,))
            self.mysql.connection.commit()
            return True
        except:
            return False

    def edit(self):
        cursor = self.mysql.connection.cursor()

        sql = "UPDATE students SET student_id = %s, full_name = %s, college = %s, course_code = %s, year_level = %s, gender = %s where student_id = %s"
        cursor.execute(sql, (self.id, self.name, self.college, self.course, self.year, self.gender,self.data_id))

        self.mysql.connection.commit()"""

class Courses():
    def __init__(self, code=None, name=None, college=None):
        self.code = code
        self.name = name
        self.college = college

    """
    def add(self):
        cursor = self.mysql.connection.cursor()

        sql = "INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.id, self.name, self.college, self.course, self.year, self.gender))

        self.mysql.connection.commit()"""

    def all(mysql):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from course_info"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
"""
    def delete(self):
        try:
            cursor = self.mysql.connection.cursor()
            sql = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(sql,(self.data_id,))
            self.mysql.connection.commit()
            return True
        except:
            return False

    def edit(self):
        cursor = self.mysql.connection.cursor()

        sql = "UPDATE students SET student_id = %s, full_name = %s, college = %s, course_code = %s, year_level = %s, gender = %s where student_id = %s"
        cursor.execute(sql, (self.id, self.name, self.college, self.course, self.year, self.gender,self.data_id))

        self.mysql.connection.commit()"""
        
