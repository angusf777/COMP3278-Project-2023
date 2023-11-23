CREATE TABLE
  IF NOT EXISTS Student (
    student_id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    face_id int NOT NULL UNIQUE,
    PRIMARY KEY (student_id)
  ) ENGINE = INNODB;

CREATE TABLE
  IF NOT EXISTS Teacher (
    teacher_id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (teacher_id)
  ) ENGINE = INNODB;

CREATE TABLE
  IF NOT EXISTS Course (
    course_code varchar(255) NOT NULL,
    teacher_id int NOT NULL,
    course_name varchar(255) NOT NULL,
    zoom_link varchar(255) NOT NULL,
    course_description varchar(255) NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES Teacher (teacher_id),
    PRIMARY KEY (course_code)
  ) ENGINE = INNODB;

CREATE TABLE
  IF NOT EXISTS Enrolled (
    student_id int NOT NULL,
    course_code varchar(255) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student (student_id),
    FOREIGN KEY (course_code) REFERENCES Course (course_code),
    PRIMARY KEY (student_id, course_code)
  ) ENGINE = INNODB;

CREATE TABLE
  IF NOT EXISTS Schedule (
    course_code varchar(255) NOT NULL,
    start_time datetime NOT NULL,
    end_time datetime NOT NULL,
    classroom varchar(255) NOT NULL,
    FOREIGN KEY (course_code) REFERENCES Course (course_code),
    PRIMARY KEY (course_code, start_time, end_time)
  ) ENGINE = INNODB;

CREATE TABLE
  IF NOT EXISTS CourseMaterialSection (
    group_id int NOT NULL AUTO_INCREMENT,
    course_code varchar(255) NOT NULL,
    group_name varchar(255) NOT NULL,
    FOREIGN KEY (course_code) REFERENCES Course (course_code),
    PRIMARY KEY (group_id, course_code)
  ) ENGINE = INNODB;

CREATE TABLE
  IF NOT EXISTS Material (
    material_id int NOT NULL AUTO_INCREMENT,
    course_code varchar(255) NOT NULL,
    group_id int NOT NULL,
    material_name varchar(255) NOT NULL,
    link varchar(255) NOT NULL,
    FOREIGN KEY (course_code) REFERENCES Course (course_code),
    FOREIGN KEY (group_id) REFERENCES CourseMaterialSection (group_id),
    PRIMARY KEY (material_id, group_id, course_code)
  ) ENGINE = INNODB;

CREATE TABLE
  IF NOT EXISTS TeacherMessage (
    message_id int NOT NULL AUTO_INCREMENT,
    course_code varchar(255) NOT NULL,
    message varchar(255) NOT NULL,
    post_time datetime NOT NULL,
    FOREIGN KEY (course_code) REFERENCES Course (course_code),
    PRIMARY KEY (message_id, course_code)
  ) ENGINE = INNODB;


CREATE TABLE 
  IF NOT EXISTS LoginData (
  student_id int NOT NULL,
  loginTime datetime NOT NULL,
  logoutTime datetime NOT NULL,
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  PRIMARY KEY (student_id, loginTime, logoutTime)
) ENGINE = INNODB;
