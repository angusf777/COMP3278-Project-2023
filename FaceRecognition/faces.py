import urllib
import numpy as np
import mysql.connector
import cv2
import pyttsx3
import pickle
from datetime import datetime
import sys
import os
import time
from dotenv import load_dotenv
load_dotenv()

# 1 Create database connection
myconn = mysql.connector.connect(host="localhost",
    user=os.environ["MYSQL_USER"],
    passwd=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"])
date = datetime.utcnow()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
cursor = myconn.cursor()


#2 Load recognize and read label from model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("FaceRecognition/train.yml")

labels = {"person_name": 1}
with open("FaceRecognition/labels.pickle", "rb") as f:
    labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}

# create text to speech
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 175)


def face_recognition():
    # Define camera and detect face
    face_cascade = cv2.CascadeClassifier('FaceRecognition/haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    # 3 Open the camera and start face recognition
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)

            # IF THE FACE IS RECOGNIZED 
            if conf >= 30:
                # print(id_)
                # print(labels[id_])
                font = cv2.QT_FONT_NORMAL
                id = 0
                id += 1
                name = labels[id_]
                current_name = name

                #
                query = "SELECT student_id FROM student WHERE name = %s"
                cursor.execute(query, (name,))
                #global student_id 
                student_id = cursor.fetchone()[0] #without [0], will give sth like (4,) ;  with [0], give 4
                #print(name)
                #print(student_id)


                color = (255, 0, 0)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                # FIND THE STUDENT'S INFO IN THE DATABASE facerecognition
                select = "SELECT student_id, name, email, face_id FROM student WHERE name='%s'" % (name)
                name = cursor.execute(select)
                result = cursor.fetchall()
                #print(result)
                
                data = "error"

                for x in result:
                    data = x

                # IF STUDENT'S INFO NOT FOUND IN DATABASE 
                if data == "error":
                    print("The student", current_name, "is NOT FOUND in the database.")

                # IF STUDENT'S INFO FOUND IN DATABASE
                else:
                    """
                    Implement useful functions here.
                    Check the course and classroom for the student.
                        If the student has class room within one hour, the corresponding course materials
                            will be presented in the GUI.
                        if the student does not have class at the moment, the GUI presents a personal class 
                            timetable for the student.

                    """
                    hello = ("Hello ", current_name, "You did attendance today")
                    print(hello)
                    engine.say(hello)
                    # engine.runAndWait()
                    cap.release()
                    cv2.destroyAllWindows()
                    #return the student_id 
                    return student_id

            # IF FACE IS NOT RECOGNIZED
            else: 
                #print(conf)
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                hello = ("Your face is not recognized")
                print(hello)
                engine.say(hello)
                # engine.runAndWait()

        cv2.imshow('Attendance System', frame)
        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    return None

