![GMIT Logo](https://github.com/Munster2020/HDIP_CSDA_COMP08050_PROJECT/blob/main/GMIT_Logo.jpg)
# Higher Diploma in Science in Computing (Data Analytics)
## Data Representation (COMP07085) - Big Project

Write a program that demonstrates that you understand creating and consuming RESTful APIs.

### 1. DVD sql DAO (Database Access Object)
I created a DAO in the file 'MoviesDao.py'. This createds an instance of the class called 'moviesDao'. this gets used with a python server to undertake CRUD operations on the SQL database. The associated configuration for for the SQL database are stored in the 'dbconfig.py'.

### 2. Flask Server
The server 'server.py' was created using Python Flask. This deals with both requests and reponses for the CRUD operations along with the SQL DAO. The server can be run locally or via a local remote virtual environment.

### 3. GUI Interface
A user interface was built in HTML for use with any browser, although I tested it using Microsoft Edge. The interface uses Bootstrap CSS sheet styles from https://getbootstrap.com/ and AJAX/jQuery library from https://developers.google.com/speed/libraries. The interface can be used to view and carry out CRUD operations on the database. It can be accessed when the app server is running. The 'Index' page can be accessed from a web browser if using a localhost 'http://127.0.0.1:5000/'.

### 4. Virtual Environment
I used conda to create a localhost virtual environment (venv) for running the server. 

The following python commands can be used to create the virtual environment.
You can install and save packages for the venv, set the flask_app server and server mode, run the server, stop the server or deactivate the venv.

1. λ conda create --name venv python=3.8
2. λ conda activate venv
3. (venv)λ pip install Flask
4. (venv)λ pip install mysql-connector-python
5. (venv)λ pip freeze > requirements.txt
6. (venv)λ set FLASK_APP=server
7. (venv)λ set FLASK_ENV=development
8. (venv)λ flask run
9. Crtl+c
10. (venv)λ conda deactivate

The package requirements can also be install from the list in the file 'requirement.txt' using the venv command
(venv)λ pip install -r requirements.txt
