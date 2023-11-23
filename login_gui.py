import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from dotenv import load_dotenv
import mysql.connector as mysql

load_dotenv()

class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setParent(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Create a label for the title
        title_label = QLabel("Intelligent Course Management System")
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title_label,alignment=Qt.AlignCenter)

        self.setLayout(layout)

# Create the original interface widget
login_widget = QWidget()

# Create a vertical layout for the original interface
layout = QVBoxLayout(login_widget)
layout.setAlignment(Qt.AlignCenter)  # Center align the contents

# Create the custom title bar
title_bar = CustomTitleBar(login_widget)
layout.addWidget(title_bar)

# Create a horizontal layout for the logo and transparent box
logo_layout = QHBoxLayout()

# Create the logo label
logo_label = QLabel(login_widget)
logo_label.setPixmap(QIcon("assets/login.png").pixmap(300, 300))  # Set your logo image path here
logo_label.setAlignment(Qt.AlignCenter)
logo_layout.addWidget(logo_label)

layout.addLayout(logo_layout)

# Create background
pixmap = QPixmap("assets/login_background.jpg")
pal = QPalette()
pal.setBrush(QPalette.Window, QBrush(pixmap))
login_widget.setPalette(pal)


# Create the ID label
id_label = QLabel("Enter ID", login_widget)
id_label.setFont(QFont("Arial", 14))
id_label.setAlignment(Qt.AlignCenter)
id_label.setFixedSize(200,30)
id_label.setStyleSheet(
    """
    QLabel {
    background-color: rgb(255,255,255);
    color: black;
    }
    """
)
# Create the input field
e_id = QLineEdit(login_widget)
e_id.setFixedWidth(300)
e_id.setFixedHeight(45)
e_id.setStyleSheet(
    """
    QLineEdit {
    background-color: rgb(255,255,255);
    color: black;
    }
    """
)
e_id.setAlignment(Qt.AlignCenter)
login_widget.e_id = e_id
# Create the login button
login_button = QPushButton("Login")
login_button.setFont(QFont("Arial", 14))
login_button.setStyleSheet(
    """
    QPushButton {
        background-color: rgba(76, 175, 80, 200);
        color: white;
        border-radius: 5px;
        padding: 10px;
    }

    QPushButton:hover {
        background-color: rgba(69, 160, 73, 200);
    }
    """
)
login_button.setFixedWidth(200)
login_button.setFixedHeight(40)
login_widget.login_button = login_button

# Create transparent box
box_layout = QVBoxLayout()
transparent_box = QFrame(login_widget)
transparent_box.setLayout(box_layout)
box_layout.addWidget(id_label, alignment=Qt.AlignCenter)
box_layout.addWidget(e_id, alignment=Qt.AlignCenter)
box_layout.addWidget(login_button, alignment=Qt.AlignCenter)
transparent_box.setFixedWidth(500)
transparent_box.setFixedHeight(150)
transparent_box.setStyleSheet("background-color: rgba(0, 0, 0, 150); border-radius: 10px;")
layout.addWidget(transparent_box)
