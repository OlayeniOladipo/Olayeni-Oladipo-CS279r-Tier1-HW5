from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Basic app definition for Flask.
app = Flask(__name__)

# Add in the database.
# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLAlchemy is a SQL toolkit through which you can create databases
# and query them.
db = SQLAlchemy(app)


# Model Class for Todo itmes including id, title, and complete fields
# and a type per field.
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# @app.route('path/to/your/url'), '/' since todo list will be on the home
# page.
@app.route("/")
# def name(): is a function defintion syntax.
def home():
    # grabs all the todo items from the Todo db.Model 
    todo_list = Todo.query.all()
    # render_template renders the proper HTML instead of just a string
    return render_template("base.html", todo_list=todo_list)

# Different app url route to /add and uses POST method.
@app.route("/add", methods=["POST"])
def add():
    # request is a Flask library api - getting what's from the user input
    title = request.form.get("title")
    # create a new-todo item given the title
    new_todo = Todo(title=title, complete=False)
    # update the databse
    db.session.add(new_todo)
    # commut the current transaction, like saving it.
    db.session.commit()
    # flask.redirect(<location>,<status-code>, <response> )
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    # get the first result when querying for thte todo_id in the Todo database model
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    # creates the initial database
    db.create_all()
    # then run the app
    app.run(debug=True)
