from PyQt5.QtWidgets import QWidget, QStackedWidget, QToolButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from home import home_widget
from schedule import schedule_widget
from course import course_widget

main_widget = QWidget()

nav_layout = QHBoxLayout()

navbar = QWidget()
navbar.setLayout(nav_layout)
navbar.setStyleSheet('''
    QWidget {
        background-color: #4AA080;
    }
''')
button_stylesheet = '''
            QToolButton {
                background-color: #4AA080;
                color: white;
                border-radius: 3px;
                width: 100%;
                padding: 5px;
            }

            QToolButton:hover {
                background-color: #34AD81;
            }
        '''


home_button = QToolButton()
home_button.setIcon(QIcon('assets/home.png'))
home_button.setIconSize(QSize(35, 35))
home_button.setStyleSheet(button_stylesheet)

schedule_button = QToolButton()
schedule_button.setIcon(QIcon('assets/calendar.png'))
schedule_button.setIconSize(QSize(35, 35))
schedule_button.setStyleSheet(button_stylesheet)

course_button = QToolButton()
course_button.setIcon(QIcon('assets/course.png'))
course_button.setIconSize(QSize(35, 35))
course_button.setStyleSheet(button_stylesheet)

logout_button = QToolButton()
logout_button.setIcon(QIcon('assets/logout.png'))
logout_button.setIconSize(QSize(35, 35))
logout_button.setStyleSheet(button_stylesheet)
main_widget.logout_button = logout_button

nav_layout.addWidget(home_button)
nav_layout.addWidget(schedule_button)
nav_layout.addWidget(course_button)
nav_layout.addWidget(logout_button)

stack = QStackedWidget()

stack.addWidget(home_widget)
stack.addWidget(schedule_widget)
stack.addWidget(course_widget)

# default as home
stack.setCurrentIndex(0)

def switch_tab_generator(i):
    def switch_tab():
        stack.setCurrentIndex(i)
    return switch_tab

home_button.clicked.connect(switch_tab_generator(0))
schedule_button.clicked.connect(switch_tab_generator(1))
course_button.clicked.connect(switch_tab_generator(2))

main_layout = QVBoxLayout()
main_layout.addWidget(stack)
main_layout.addWidget(navbar)
main_layout.setStretch(0, 8)
main_layout.setStretch(8, 9)

main_widget.setLayout(main_layout)
