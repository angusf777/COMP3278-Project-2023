from PyQt5.QtCore import QEasingCurve, Qt, QUrl, QVariantAnimation
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtWidgets import (QFrame, QLabel, QPushButton, QScrollArea,
                             QSizePolicy, QVBoxLayout, QWidget)

import data
import database

course_widget = QWidget()

course_layout = QVBoxLayout()
course_layout.setAlignment(Qt.AlignCenter)

course_widget.setLayout(course_layout)

main_scroll_content = QWidget()
main_scroll_content.setLayout(course_layout)

main_scroll_area = QScrollArea()
main_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
main_scroll_area.setWidgetResizable(True)
main_scroll_area.setWidget(main_scroll_content)
main_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)


main_wrap_layout = QVBoxLayout()
course_widget.setLayout(main_wrap_layout)
main_wrap_layout.addWidget(main_scroll_area)

def create_course_widget(course):
    course_entity_widget = QWidget()
    course_entity_layout = QVBoxLayout()
    course_entity_layout.setAlignment(Qt.AlignCenter)

    down_button = QPushButton(QIcon("assets/down.png"), f"{course.course_code}: {course.course_name}")
    down_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    down_button.setFlat(True)
    button_stylesheet = '''
        QPushButton {
            background-color: #4AA080; 
            border-radius: 2px; 
            border: 2px #B1B2FF;
            padding: 5px 10px;
            color: #ffffff; 
            font-family: Arial, sans-serif; 
            font-size: 18px;
            border-style: none solid solid none;
        } 
        
        QPushButton:hover {
            border: 0;
            background-color: #34AD81;
        }
    '''
    down_button.setStyleSheet(button_stylesheet)  

    expand_layout = QVBoxLayout()

    content_stylesheet = '''
        QLabel {
            margin-bottom: 1px;
            padding-left: 5px;
            font-size: 14px;
        }
    '''

    description_label = QLabel(f"Course Description:\n{course.course_description}")
    description_label.setWordWrap(True)
    description_label.setStyleSheet(content_stylesheet)
    description_label.adjustSize()

    teachers_info = database.getTeachersForCourse(course.course_code)
    teacher_label = QLabel(
        "Teacher information:" + 
        "".join(
            f"\nName: {teacher_info[0]}\nEmail: {teacher_info[1]}\n"
            for teacher_info in teachers_info
        )[:-1]
    )
    teacher_label.setWordWrap(True)
    teacher_label.setStyleSheet(content_stylesheet)

    zoom_text = f"Zoom link: <a href=\"{course.zoom_link}\" style=\"color: {{color}}\">{course.zoom_link}</a>"
    zoom_link_label = QLabel(zoom_text.format(color="white"))
    zoom_link_label.setTextFormat(Qt.TextFormat.RichText)
    zoom_link_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
    zoom_link_label.setOpenExternalLinks(True)
    zoom_link_label.setStyleSheet(content_stylesheet)

    classrooms = database.getClassroomsForCourse(course.course_code)
    classrooms = list(dict.fromkeys(classrooms))
    classroom_label = QLabel(
        "Classroom(s): " + 
        "".join(
            f"{classroom}, "
            for classroom in classrooms
        )[:-2]
    )
    classroom_label.setWordWrap(True)
    classroom_label.setStyleSheet(content_stylesheet)

    teacher_msgs = database.getTeacherMessages(course.course_code)
    teacher_msgs_label = QLabel(
        "Teacher Messages:\n" + 
        "".join(
            f"{teacher_msg[1]}\n{teacher_msg[0]}\n\n"
            for teacher_msg in teacher_msgs
        )[:-2]
    )
    teacher_msgs_label.setWordWrap(True)
    teacher_msgs_label.setStyleSheet(content_stylesheet)

    group_dict = {}
    for group_id, group_name in database.getMaterialGroupsForCourse(course.course_code):
        if database.getMaterialsForGroup(course.course_code, group_id) != None:
            group_dict[group_name] = database.getMaterialsForGroup(course.course_code, group_id)
    
    def get_email_main_content():
        main_content = ""
        main_content += f"{description_label.text()}\n\n"
        main_content += f"{teacher_label.text()}\n\n"
        main_content += f"link: {course.zoom_link}\n\n"
        main_content += classroom_label.text() + "\n\n"
        main_content += teacher_msgs_label.text() + "\n\n"
        main_content += "Material:\n"
        for group, materials in group_dict.items():  
            main_content += group + "\n"
            for i, material in enumerate(materials):
                link, name = material
                main_content += f"{i + 1}. {name}: link: {link}\n"
        return main_content

    text = get_email_main_content()
    mail_to_link = QUrl(
        f"mailto:{database.getStudent(data.student_id)[2]}" +
        f"?subject={QUrl.toPercentEncoding(f'Course {course.course_code} Detail: {course.course_name}').data().decode()}"  +
        f"&body={QUrl.toPercentEncoding(text).data().decode()}",
        QUrl.ParsingMode.TolerantMode
    )
    email_button = QPushButton("Send to email")
    email_button.setFlat(True)
    email_button.clicked.connect(
        lambda: QDesktopServices.openUrl(mail_to_link)
    )
    email_button.setStyleSheet(content_stylesheet)

    expand_layout.addWidget(description_label)
    expand_layout.addWidget(teacher_label)
    expand_layout.addWidget(zoom_link_label)
    expand_layout.addWidget(classroom_label)
    expand_layout.addWidget(teacher_msgs_label)
    for group, materials in group_dict.items():     #expand_layout.addWidgets(materialss)
        group_label = QLabel(group+':\n')
        group_label.setWordWrap(True)
        group_label.setStyleSheet(content_stylesheet)
        expand_layout.addWidget(group_label)
        idx = 1
        for material in materials:
            material_label = QLabel(f"{idx}.&nbsp;<a href=\"{material[0]}\">{material[1]}</a>")
            material_label.setTextFormat(Qt.TextFormat.RichText)
            material_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
            material_label.setOpenExternalLinks(True)
            material_label.setStyleSheet(content_stylesheet)
            idx += 1
            expand_layout.addWidget(material_label)
    expand_layout.addWidget(email_button)

    expand_content = QFrame()
    expand_content.setLayout(expand_layout)

    frame_stylesheet = '''
        QFrame {
            background-color: #4AA080;
            color: white;
            border: 0;
            border-radius: 2px;
            width: 80px;
            padding: 5px;
            font-size: 12px;
        }

        QPushButton {
            background-color: #4AA080; 
            border: 2px #B1B2FF;
            border-radius: 2px; 
            border-style: none solid solid none;
            padding: 5px 10px;
            color: #ffffff; 
            font-family: ubuntu, arial; 
            font-size: 12px;
        } 
        
        QPushButton:hover {
            background-color: #34AD81;
            border: 0;
        }
    '''
    expand_content.setStyleSheet(frame_stylesheet)

    scroll_content = QWidget()
    scroll_content.setLayout(course_entity_layout)

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    scroll_area.setWidget(scroll_content)

    wrap_layout = QVBoxLayout()
    wrap_layout.addWidget(scroll_area)
    course_entity_widget.setLayout(wrap_layout)

    expand_height = expand_content.sizeHint().height()
    expand_content.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
    expand_content.setFixedHeight(0)

    expand_anim = QVariantAnimation()
    expand_anim.setDuration(100)
    expand_anim.setEasingCurve(QEasingCurve.Type.Linear)

    def update_animation():
        if expand_content.height() == 0:
            expand_anim.setStartValue(expand_content.height())
            expand_anim.setEndValue(expand_height)
            down_button.setIcon(QIcon('assets/up.png'))
        else:
            expand_anim.setStartValue(expand_content.height())
            expand_anim.setEndValue(0)
            down_button.setIcon(QIcon('assets/down.png'))
        expand_anim.start()

    def update_animation_on_click():
        update_animation()
        expand_content.setFixedHeight(expand_anim.currentValue())

    down_button.clicked.connect(update_animation_on_click)
    expand_anim.valueChanged.connect(expand_content.setFixedHeight)

    course_entity_layout.addWidget(down_button)
    course_entity_layout.addWidget(expand_content)
    course_entity_widget.setLayout(course_entity_layout)

    return course_entity_widget

class Course(object):
    def __init__(self, course_code, teacher_id, course_name, zoom_link, course_description):
        self.course_code = course_code
        self.teacher_id = teacher_id
        self.course_name = course_name
        self.zoom_link = zoom_link
        self.course_description = course_description

def update_course_content():
    for i in reversed(range(course_layout.count())): 
        course_layout.itemAt(i).widget().setParent(None)
    courses = []
    for _, course_code in database.getEnrolled(data.student_id):
        if course_code is not None:
            course_data = database.getCourse(course_code)
            course = Course(
                course_code=course_data[0],
                teacher_id=course_data[1],
                course_name=course_data[2],
                zoom_link=course_data[3],
                course_description=course_data[4]
            )
            courses.append(course)

    for course in courses:
        course_entity_widget = create_course_widget(course)
        course_layout.addWidget(course_entity_widget)
