from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Todo sno={self.sno}, desc='{self.desc}'>"


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == "POST":

        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(title=title, desc=desc)

        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()

    return render_template("index.html", allTodo=allTodo)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
    
    # crud operations to be done in the database using SQLAlchemy
    #template hierarchy- add base and update html files