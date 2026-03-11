from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YourNewPass", # Put your password here
        database="school_db"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, course) VALUES (%s, %s, %s)", (name, email, course))
    conn.commit()
    cursor.close()
    conn.close()
    return f"<h1>Success! {name} added to MySQL.</h1><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
