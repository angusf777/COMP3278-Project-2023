from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt
from datetime import datetime
import database
import data

home_widget = QWidget()

home_layout = QVBoxLayout()
home_layout.setAlignment(Qt.AlignTop)
home_layout.setContentsMargins(20, 20, 20, 20)
home_layout.setSpacing(20)

home_widget.setLayout(home_layout)

login = QLabel()
stay = QLabel()
login.setAlignment(Qt.AlignLeft)
login.setFont(QFont('Arial', 10))
stay.setAlignment(Qt.AlignLeft)
stay.setFont(QFont('Arial', 10))

label = QLabel()
label.setAlignment(Qt.AlignCenter)
label.setFont(QFont('Arial', 25)) 

welcome = QLabel()
welcome.setAlignment(Qt.AlignCenter)
welcome.setFont(QFont('Arial', 70))

home_layout.addWidget(login, alignment=Qt.AlignTop | Qt.AlignLeft)  
home_layout.addWidget(stay, alignment=Qt.AlignTop | Qt.AlignLeft) 
home_layout.addWidget(welcome)
home_layout.addWidget(label)

# check if you have class
def check_class():
    lecture = database.getUpcomingClass(data.student_id)
    if lecture:
        course_code = lecture[0]
        start_time = lecture[1]
        time_diff = start_time - datetime.now()
        if time_diff.total_seconds() // 60 <= 60:
            return f"You have {course_code} in the next hour at {start_time.time()}. " \
                   f"Please see the relevant course materials."

    return "No class in the next hour."

# update homepage
def update_home_content():
    label.setText(check_class())
    # show name
    student_name = database.getStudent(data.student_id)[1]
    welcome.setText(f"Hello {student_name}")
    # show last login time
    last_login = database.LoginTime(data.student_id)
    login.setText(f"Last login: {last_login}")
    # show how long the user has stayed
    staytime = database.StayTime(data.student_id)
    stay.setText(f"Stay Time: {staytime}")
