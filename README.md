## Intelligent course management system
A course system that requires uid & face recognition for login, which then brings you to a interface that includes home, schedule and course page. 
Group Project in COMP3278 2023, group of 5, I served as the front end and back end developer, mainly focusing on main and course page.

## Installation

```bash
pip install -r requirements.txt
```

#both VScode and local

## Getting Started

1. Rename `.env.example` as `.env`, amend the name, add data/Angus under FaceRecognition, select more photos for face_capture.py

2. Create tables using the sql file `database/create_tables2.sql` and insert dummy values with `database/dummy_data2.sql`
   MySQL Workbench

3. Capture some photo for face recognition

```bash
cd FaceRecognition
python face_capture.py
```

4. Train the model

```bash
python train.py
```

5. Run the main program

```bash
python main.py
```

## INDEX

1. main.py: login page
2. FaceRecognition/faces.py: face recognition
3. home.py: homepage
4. schedule.py: student's weekly schedule
5. course.py: shows student's courses and course materials, also lets them send course details to their email
6. database.py: finds details from sql database
7. data.py: global student id

PPT slides: https://docs.google.com/presentation/d/1Yf7OuEdqYgQwmQ74nxbXVPyFcyTXsXSYJoHCzis7Tsw/edit?usp=sharing
