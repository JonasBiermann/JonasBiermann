import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.executescript(
    """
    CREATE TABLE classes 
(
    CId	INT,
    grade	INT,
    TId	INT
);

INSERT INTO classes (CId, grade, TId) VALUES
	('101', '10', '1'),
	('102', '10', '2'),
	('103', '10', '3'),
	('104', '10', '4'),
	('111', '11', '5'),
	('112', '11', '6'),
	('113', '11', '7'),
	('114', '11', '8'),
	('121', '12', '9'),
	('122', '12', '10'),
	('123', '12', '11'),
	('124', '12', '12');
    """
)

cursor.executescript(
    """
    CREATE TABLE students 
(
    SId	INT,
    firstname	VARCHAR(512),
    name	VARCHAR(512),
    birthdate	VARCHAR(512),
    CId	INT
);

INSERT INTO students (SId, firstname, name, birthdate, CId) VALUES
	('1', 'William', 'Campbell', '2007-05-17', '101'),
	('2', 'Emma', 'Harris', '2007-03-28', '101'),
	('3', 'Isabella', 'Nelson', '2007-12-17', '103'),
	('4', 'Taylor', 'Martinez', '2007-05-25', '102'),
	('5', 'Alyssa', 'Moore', '2006-01-01', '104'),
	('6', 'Sofia', 'Lewis', '2006-02-28', '111'),
	('7', 'Melissa', 'Evans', '2006-04-11', '112'),
	('8', 'Joshua', 'Moore', '2006-09-23', '112'),
	('9', 'Haley', 'Brown', '2005-04-04', '113'),
	('10', 'Ava', 'Young', '2005-11-09', '121'),
	('11', 'Joshua', 'Moore', '2005-07-02', '122'),
	('12', 'Haley', 'Brown', '2005-10-03', '123');
    """
)

cursor.executescript(
    """
    CREATE TABLE teachers
(
    TId	INT,
    firstname	VARCHAR(512),
    lastname	VARCHAR(512),
    specialization	INT
);

INSERT INTO teachers (TId, firstname, lastname, specialization) VALUES
	('1', 'William', 'Campbell', '1'),
	('2', 'Emma', 'Harris', '4'),
	('3', 'Isabella', 'Nelson', '3'),
	('4', 'Taylor', 'Martinez', '5'),
	('5', 'Alyssa', 'Moore', '6'),
	('6', 'Sofia', 'Lewis', '8'),
	('7', 'Melissa', 'Evans', '7'),
	('8', 'Joshua', 'Moore', '1'),
	('9', 'Haley', 'Brown', '2'),
	('10', 'Ava', 'Young', '3'),
	('11', 'Ava', 'Robinson', '9'),
	('12', 'Ethan', 'Peterson', '10');
    """
)

cursor.executescript(
    """
    CREATE TABLE rooms
(
    RId	VARCHAR(512),
    size	INT,
    type	VARCHAR(512)
);

INSERT INTO rooms (RId, size, type) VALUES
	('UG1', '20', '1'),
	('UG2', '21', '2'),
	('UG3', '21', '1'),
	('UG4', '23', '1'),
	('UG5', '22', '1'),
	('UG6', '24', '2'),
	('UG7', '30', '2'),
	('UG8', '20', '1'),
	('UG9', '20', '2'),
	('UG10', '21', '2'),
	('EG1', '15', '1'),
	('EG2', '18', '1'),
	('EG3', '20', '1'),
	('EG4', '21', '1'),
	('EG5', '23', '1'),
	('EG6', '25', '1'),
	('EG7', '26', '1'),
	('EG8', '28', '1'),
	('EG9', '29', '1'),
	('EG10', '30', '1'),
	('OG1', '31', '1'),
	('OG2', '28', '1'),
	('OG3', '26', '1'),
	('OG4', '24', '3'),
	('OG5', '16', '3'),
	('OG6', '19', '3'),
	('OG7', '29', '3'),
	('OG8', '22', '1'),
	('OG9', '21', '1'),
	('OG10', '25', '2');
    """
)

cursor.executescript(
    """
    CREATE TABLE points 
(
    duration	INT,
    points	INT
);

INSERT INTO points (duration, points) VALUES
	('45', '1'),
	('90', '2'),
	('135', '3'),
	('180', '4'),
	('225', '5');
    """
)

cursor.executescript(
    """
    CREATE TABLE presentations 
(
    PId	INT,
    title	VARCHAR(512),
    description	VARCHAR(512),
    starttime	VARCHAR(512),
    subject	VARCHAR(512),
    date	VARCHAR(512),
    attendance	INT,
    TId	INT,
    RId	VARCHAR(512),
    duration	INT
);

INSERT INTO presentations (PId, title, description, starttime, subject, date, attendance, TId, RId, duration) VALUES
	('1', 'HTML', 'Lorem ipsum dolor sit amet.', '7,35', '1', '2023-03-27', '15', '1', 'OG10', '90'),
	('2', 'Python', 'Lorem ipsum dolor sit amet.', '7,35', '1', '2023-03-29', '15', '3', 'EG7', '60'),
	('3', 'Experimente', 'Lorem ipsum dolor sit amet.', '9,00', '2', '2023-03-28', '20', '5', 'OG2', '120'),
	('4', 'USA', 'Lorem ipsum dolor sit amet.', '10,15', '3', '2023-03-29', '25', '7', 'UG3', '45'),
	('5', 'Gedichte', 'Lorem ipsum dolor sit amet.', '11,00', '4', '2023-03-30', '20', '3', 'UG10', '90');
    """
)

cursor.executescript(
    """
    CREATE TABLE attendance 
(
    SId	INT,
    PId	INT,
    presenter	VARCHAR(512)
);

INSERT INTO attendance (SId, PId, presenter) VALUES
	('1', '1', '1'),
	('4', '5', '0'),
	('3', '4', '1'),
	('2', '2', '0'),
	('6', '3', '1');
    """
)