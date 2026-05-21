from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    return f"""
    <h1>Student Added Successfully!</h1>
    <p>Name: {name}</p>
    <p>Email: {email}</p>
    <p>Course: {course}</p>
    <a href='/'>Go Back</a>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
