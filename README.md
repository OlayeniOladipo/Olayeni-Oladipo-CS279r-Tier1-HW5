# Olayeni-Oladipo-CS279r-Tier1-HW5
[Tier 1] Programming HW4: Make a To-Do App with Flask <br />
Olayeni Oladipo <br />
October 3, 2022 <br />

**Reflection:** What are the significant software concepts that this combination of technologies has that each previous set of technologies did not? Or that they handle significantly differently?

Flask is a minimal, web framework written in Python. It's different than Node.Js as node uses javascript. This is a similar case with the HTML/CSS/JS hybrid. Flask does utilize HTML through its template folder. It can take in a reference CSS stylesheet, or one could create a CSS file directly. In comparison to Flutter/Dart, Flask is more of a framework while Dart is a programming language. ObservableHQ utilized some HTML and javascript via D3.js, but for the most part differs from Flask. Flask is very lightweight which makes it great for small to medium projects. 

SQLAlchemy is a Python SQL tooklit that allows a lot of flexibility with database creation and updating within the Python code. MongoDB on the otherhand is a noSQL database. Firebase's Firestore is also a noSQL database. Generally SQL is better for multi-row operations and vertical scaling, while noSQL is better for more complex forms of data like json or documents and thus can be horizontally scaled.

**Important files to view:** 
- app.py
- templates/base.html

**Instructions** to launch prototype:

1) Clone or download this repo, saving the files to a directory
2) Open terminal and CD into the directory of the downloaded files.
3) Enter the following lines into your terminal.
> python3 -m venv venv
> . venv/bin/activate
> pip install Flask
> pip install Flask-SQLAlchemy
> export FLASK_APP=app.py
> export FLASK_ENV=development
> python app.py
4) Open the link (similar to http://127.0.0.1:5000) that pops up in your terminal.

On the link, play around with the following features: <br />
1) Add a to-do list item by typing in a todo item and pressing the 'Add' button or hitting the enter key.
2) Check off the to-do list item by pressing the 'update' button next to an individual todo item.
3) Press the 'Delete' button to delete a todo item.
4) The above encapsulate basic functionality of a todo app.

Worked off the code from the following sources:
- https://github.com/python-engineer/flask-todo <br/>
- https://www.python-engineer.com/posts/flask-todo-app/ <br/>

Comments informed by the following:
- https://www.educba.com/flask-redirect/ <br/>
- https://www.integrate.io/blog/the-sql-vs-nosql-difference/#:~:text=SQL%20databases%20are%20vertically%20scalable,data%20like%20documents%20or%20JSON.
