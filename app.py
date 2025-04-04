from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def show_assignment_input(name=None):
    return render_template('assignment_input.html')
    # here we present the form

@app.route('/new_assignment')
def add_assignmnt():
    pass
    

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('art/hello.html', person=name)

# @app.route("/age/<int:age>")
# def yourname(age):
#   return f"Hello. your age is a int {escape(age)}"

@app.route("/age/<uuid:age>")
def age(age):
    return f"Hello, you age is a float {escape(age)} years old!"


