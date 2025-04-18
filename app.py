from flask import Flask, render_template, request
from markupsafe import escape
import sqlite3

con = sqlite3.connect("assignments.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS assignments(name);"
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    # here we present the form

@app.route('/new_assignment', methods=("GET","POST"))
def new_assignment():
    if request.method == "POST":
        new_assignment = {"name": request.form['assignment_name']}
        # save_assignment(new_assignment)   
        return render_template("show_assignment.html", new_assignment=new_assignment)
    return render_template("index.html")

def save_assignment(assignment):
    con = sqlite3.connect("assignments.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO assignments(name) VALUES (?);",
        (assignment["name"])
    )
    con.commit()
    return

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


