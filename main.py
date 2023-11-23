from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget
from PyQt5.QtGui import QPixmap, QPalette, QBrush
import mysql.connector
from datetime import datetime
import sys
from dotenv import load_dotenv
import FaceRecognition.faces  # for using the function studentID to get the student_id of the face being detected
import database
import data  # global student_id


app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle("Intelligent Course Management System")

from login_gui import login_widget
from main_gui import main_widget, stack

main_stack = QStackedWidget()
main_stack.addWidget(login_widget)
main_stack.addWidget(main_widget)

load_dotenv()

myconn = mysql.connector.connect(host="localhost",
user=os.environ["MYSQL_USER"],
passwd=os.environ["MYSQL_PASSWORD"],
database=os.environ["MYSQL_DATABASE"])
cursor = myconn.cursor()

def login():
    user_input = login_widget.e_id.text()
    if user_input == "":
        QMessageBox.information(login_widget, "Insert Status", "All fields are required")
    else:
        user = database.getStudent(user_input)
        if user is not None:
            student_id = FaceRecognition.faces.face_recognition()
            if student_id == int(user_input):
                data.student_id = student_id
                from home import update_home_content
                from schedule import update_schedule_content
                from course import update_course_content
                update_home_content()
                update_schedule_content()
                update_course_content()
                date = datetime.now()
                # UPDATE DATA (LoginTime) IN DATABASE 
                update = "UPDATE loginData SET loginTime= %s WHERE student_id= %s"
                val = (date, user_input)
                cursor.execute(update,val)
                myconn.commit()

                stack.setCurrentIndex(0)
                main_stack.setCurrentIndex(1)
            else:
                QMessageBox.critical(login_widget, "Error!", "Face doesn't match the inputted student_id!!!!!!")
        else:
            QMessageBox.critical(login_widget, "Oops", "User not found in database.")


#pass in the student_id and update the student's logout time 
def logout():
    main_stack.setCurrentIndex(0)
    date = datetime.now()
    update = "UPDATE LoginData SET logoutTime = %s WHERE student_id = %s "
    val = (date, data.student_id)
    cursor.execute(update,val)
    myconn.commit()
    data.student_id = 0

login_widget.login_button.clicked.connect(login)
main_widget.logout_button.clicked.connect(logout)
main_window.setCentralWidget(main_stack)

main_window.resize(850, 534)

pixmap = QPixmap('assets/login_background.jpg')
pal = QPalette()
pal.setBrush(QPalette.Background, QBrush(pixmap))
main_window.setPalette(pal)

main_window.show()
sys.exit(app.exec_())
