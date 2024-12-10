# Mini-Project-Docker-Anastasiya
FINAL: Mini Project: University Timetable Web Application - Docker 

1. Pulled the Latest PostgreSQL Docker Image with this command:

docker pull postgres:latest

Run PostgreSQL Container:

docker run --name university-db -e POSTGRES_USER=student -e POSTGRES_PASSWORD=student_pass -d -p 5433:5432 postgres:latest

Access the PostgreSQL Container:

docker exec -it university-db bash

Connect to PostgreSQL Database:

psql -U student -d postgres

2. In Terminal of Visual Studio: 

Then Setting Up the Django Project

Install Required Python Packages

Install psycopg2 for PostgreSQL integration: to connect Django to PostgreSQL:

pip install psycopg2

Installation and preparation of Django:

pip install django


Create and Activate Virtual Environment
Activate the Virtual Environment:

To activate the virtual environment:

.venv\Scripts\activate

Create a New Django Project:

Start a new Django project in the current directory:

django-admin startproject project .

Create a new Django app for the project:

python manage.py startapp nastya_app

Running the Django Server
Once the database is set up and the project is configured, i ran the Django development server with the these steps:

Make Migrations:
Creating migration files for the database schema changes - telling python to use models.py and translate it to sql with this code: 

python manage.py makemigrations

Apply the migrations to the database - Telling python, giving instructions to transfer sql data to data base:

python manage.py migrate

Create a Superuser:

Create a superuser for accessing the Django admin panel:

python manage.py createsuperuser

Run the Server:

Start the local server:

python manage.py runserver

The server will run locally, and I can access it at http://127.0.0.1:8000/.

3. THEN Configuring and Inserting Data into the Database with SQL commands using Shell Terminal:
Inserting Data into Tables

SQL:

INSERT INTO nastya_app_course (name)
VALUES
    ('IT Project Management'),
    ('Operating Systems'),
    ('Cybersecurity'),
    ('Political Theory'),
    ('Art Appreciation'),
    ('International Relations'),
    ('Principles of Programming'),
    ('Data Structures');
    
Insert student timetable data into the timetable table:

INSERT INTO nastya_app_timetable (course_id, student_id, room, day, time, level)
VALUES
    (2, 2, 'Room 102', 'Friday', '10:00 AM', 1),
    (2, 2, 'Room 201', 'Wednesday', '9:00 AM', 2),
    (2, 2, 'Room 202', 'Wednesday', '11:00 AM', 2);

INSERT INTO nastya_app_timetable (course_id, student_id, room, day, time, level)
VALUES
    (9, 3, 'Room 145', 'Friday', '10:00 AM', 3);
    



