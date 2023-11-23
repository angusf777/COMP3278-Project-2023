# this runs after face recog, but will probably be merged onto faces.py/faces_gui.py
# enter your own passwd and database
# this current code is for selecting all the relevant info to be used in displaying the timetable/class within next hour
import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

conn = mysql.connector.connect(host="localhost",
            user=os.environ["MYSQL_USER"],
            passwd=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"])

def getStudent(student_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Student WHERE student_id='{student_id}'")
    student_info = cursor.fetchall()
    if (len(student_info) == 0):
        return None
    return student_info[0]

def getCourse(course_code):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Course WHERE course_code='{course_code}'")
    course_info = cursor.fetchall()
    if (len(course_code) == 0):
        return None
    return course_info[0]

def getEnrolled(student_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Enrolled WHERE student_id='{student_id}'")
    enrolled_info = cursor.fetchall()
    return enrolled_info

def getSchedule(student_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Schedule NATURAL JOIN (SELECT course_code FROM Enrolled WHERE student_id='{student_id}') AS courses ORDER BY start_time")
    schedule = cursor.fetchall()
    return schedule

def getCourseMaterialSections(course_code):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM CourseMaterialSection WHERE course_code='{course_code}'")
    course_sections = cursor.fetchall()
    return course_sections

def getMaterials(group_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Material WHERE group_id='{group_id}'")
    course_materials = cursor.fetchall()
    return course_materials

def getMaterialsForGroup(course_code, group_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT link, material_name FROM Material WHERE course_code = '{course_code}' AND group_id = '{group_id}'")
    materials = cursor.fetchall()
    materials_list = [(material[0], material[1]) for material in materials]
    return materials_list

def getMaterialGroupsForCourse(course_code):
    cursor = conn.cursor()
    cursor.execute(f"SELECT group_id, group_name FROM CourseMaterialSection WHERE course_code = '{course_code}'")
    groups = cursor.fetchall()
    groups_list = [(group[0], group[1]) for group in groups]
    return groups_list

def getTeachersForCourse(course_code):
    cursor = conn.cursor()
    cursor.execute(f"SELECT Teacher.name, Teacher.email FROM Teacher JOIN Course ON Teacher.teacher_id = Course.teacher_id WHERE Course.course_code = '{course_code}'")
    teachers_info = cursor.fetchall()
    teachers_data = [(name, email) for name, email in teachers_info]
    return teachers_data

def getClassroomsForCourse(course_code):
    cursor = conn.cursor()
    cursor.execute(f"SELECT classroom FROM Schedule WHERE course_code = '{course_code}'")
    classrooms = cursor.fetchall()
    classrooms_list = [classroom[0] for classroom in classrooms]
    return classrooms_list

def getTeacherMessages(course_code):
    cursor = conn.cursor()
    cursor.execute(f"SELECT message, post_time FROM TeacherMessage WHERE course_code = '{course_code}' ORDER BY post_time DESC")
    messages = cursor.fetchall()
    messages_list = [(message[0], message[1]) for message in messages]
    return messages_list

def getTeacherLatestMessage(course_code):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM TeacherMessage WHERE course_code='{course_code}' ORDER BY post_time DESC LIMIT 1")
    latest_message = cursor.fetchall()
    if (len(course_code) == 0):
        return None
    return latest_message[0]

def LoginTime(student_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT loginTime FROM LoginData WHERE student_id='{student_id}'")
    login_time = cursor.fetchone()
    if login_time:
        return login_time[0]
    return None

def LogoutTime(student_id):
    cursor = conn.cursor()
    query = f"SELECT logoutTime FROM LoginData WHERE student_id='{student_id}"
    cursor.execute(query)
    conn.commit()

def StayTime(student_id):
    cursor = conn.cursor()
    cursor.execute(f"SELECT TIMEDIFF(logoutTime, loginTime) as duration FROM LoginData WHERE student_id='{student_id}'")
    duration = cursor.fetchone()
    if duration:
        return duration[0]
    return None

def getUpcomingClass(student_id):
    today = datetime.now().date()  # today's date
    time = datetime.now().time()  
    cursor = conn.cursor()# current time
    cursor.execute(
        f"SELECT * FROM (SELECT * FROM Schedule WHERE DATE(start_time)='{today}' AND '{time}' <= TIME(start_time)) as S NATURAL JOIN (SELECT course_code FROM Enrolled WHERE student_id='{student_id}') AS E ORDER BY start_time LIMIT 1")
    earliest = cursor.fetchone()  # fetch next earliest class
    if earliest:
        return earliest
    else:
        return None
