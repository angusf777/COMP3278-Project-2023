INSERT INTO
    Student (name, email, face_id)
VALUES
    ('Eddie', 'eddie@connect.hku.hk', 1);

INSERT INTO
    Student (name, email, face_id)
VALUES
    ('Amaris', 'amaris@connect.hku.hk', 2);

INSERT INTO
    Student (name, email, face_id)
VALUES
    ('Angus', 'angus@connect.hku.hk', 3);

INSERT INTO
    Student (name, email, face_id)
VALUES
    ('Jonathan', 'jonathan@connect.hku.hk', 4);

INSERT INTO
    Student (name, email, face_id)
VALUES
    ('Dex', 'dex@connect.hku.hk', 5);

INSERT INTO
    Teacher (name, email)
VALUES
    ('Dr. Ping Luo', 'pluo@cs.hku.hk');

INSERT INTO
    Course (
        course_code,
        teacher_id,
        course_name,
        zoom_link,
        course_description
    )
VALUES
    (
        'COMP3278',
        1,
        'Introduction to Database Management Systems',
        'https://hku.zoom.us/j/98307568693?pwd=QmlqZERWeDdWRVZ3SGdqWG51YUtndz09',
        'Able to understand the modeling of real-life information in a database system.'
    );

INSERT INTO
    Enrolled (student_id, course_code)
VALUES
    (1, 'COMP3278');

INSERT INTO
    Enrolled (student_id, course_code)
VALUES
    (2, 'COMP3278');

INSERT INTO
    Schedule (course_code, start_time, end_time, classroom)
VALUES
    (
        'COMP3278',
        '2023-11-02 13:30:00',
        '2023-11-02 15:20:00',
        'MWT1'
    );

INSERT INTO
    Schedule (course_code, start_time, end_time, classroom)
VALUES
    (
        'COMP3278',
        '2023-11-06 14:30:00',
        '2023-11-06 15:20:00',
        'MWT1'
    );

INSERT INTO
    CourseMaterialSection (course_code, group_name)
VALUES
    ('COMP3278', 'Announcement');

INSERT INTO
    CourseMaterialSection (course_code, group_name)
VALUES
    ('COMP3278', 'Assignment');

INSERT INTO
    CourseMaterialSection (course_code, group_name)
VALUES
    ('COMP3278', 'SQL Challenge');

INSERT INTO
    Material (course_code, group_id, material_name, link)
VALUES
    (
        'COMP3278',
        1,
        'News Announcement',
        'https://moodle.hku.hk/mod/forum/view.php?id=2987421'
    );

INSERT INTO
    Material (course_code, group_id, material_name, link)
VALUES
    (
        'COMP3278',
        2,
        'Assignment 1',
        'https://moodle.hku.hk/mod/assign/view.php?id=3097603'
    );

INSERT INTO
    Material (course_code, group_id, material_name, link)
VALUES
    (
        'COMP3278',
        2,
        'Assignment 2',
        'https://moodle.hku.hk/mod/assign/view.php?id=3145076'
    );

INSERT INTO
    TeacherMessage (course_code, message, post_time)
VALUES
    (
        'COMP3278',
        'Welcome to COMP3278!',
        '2023-11-06 14:30:00'
    );


INSERT INTO
    LoginData (student_id,loginTime, logoutTime)
VALUES
    (1, '2023-10-02 11:32:42', '2023-10-02 17:24:44');

INSERT INTO
    LoginData (student_id,loginTime, logoutTime)
VALUES
    (2, '2023-10-02 11:32:42', '2023-10-02 17:24:44');

INSERT INTO
    LoginData (student_id,loginTime, logoutTime)
VALUES
    (3, '2023-10-02 11:32:42', '2023-10-02 17:24:44');

INSERT INTO
    LoginData (student_id,loginTime, logoutTime)
VALUES
    (4, '2023-10-02 11:32:42', '2023-10-02 17:24:44');

INSERT INTO
    LoginData (student_id,loginTime, logoutTime)
VALUES
    (5, '2023-10-02 11:32:42', '2023-10-02 17:24:44');


INSERT INTO `Course` (`course_code`, `teacher_id`, `course_name`, `zoom_link`, `course_description`) VALUES
('COMP2119', 1, 'Introduction to Data Structures & Algorithms', 'https://hku.zoom.us/j/98307568693?pwd=QmlqZERWeDdWRVZ3SGdqWG51YUtndz09', 'Understand the concept of time, space complexity and analyze the time and space complexities of an algorithm and a data structure.'),
('COMP2501', 1, 'Introduction to Data Science', 'https://hku.zoom.us/j/98307568693?pwd=QmlqZERWeDdWRVZ3SGdqWG51YUtndz09', 'Introduction to concepts of data science');

INSERT INTO `CourseMaterialSection` (`group_id`, `course_code`, `group_name`) VALUES
(4, 'COMP2501', 'Lectures'),
(5, 'COMP2119', 'Lectures');

INSERT INTO `Enrolled` (`student_id`, `course_code`) VALUES
(1, 'COMP2119'),
(2, 'COMP2119'),
(3, 'COMP2119'),
(1, 'COMP2501'),
(2, 'COMP2501'),
(3, 'COMP2501');

INSERT INTO `Material` (`material_id`, `course_code`, `group_id`, `material_name`, `link`) VALUES
(4, 'COMP2119', 5, 'Lecture 1', 'https://moodle.hku.hk/mod/resource/view.php?id=3081895'),
(5, 'COMP2501', 4, 'Lecture 1', 'https://moodle.hku.hk/mod/resource/view.php?id=3081960');

INSERT INTO `Schedule` (`course_code`, `start_time`, `end_time`, `classroom`) VALUES
('COMP2119', '2023-11-21 10:00:00', '2023-11-21 11:30:00', 'MWT2'),
('COMP2501', '2023-11-24 15:00:00', '2023-11-24 17:00:00', 'MWT3');

INSERT INTO `TeacherMessage` (`message_id`, `course_code`, `message`, `post_time`) VALUES
(2, 'COMP2501', 'Lecture 1 has been released. Please review this and attempt the tutorial questions before class.', '2023-11-20 14:29:57'),
(3, 'COMP2119', 'Welcome to COMP2119! Please review lecture 1 before class.', '2023-11-21 09:00:00');
