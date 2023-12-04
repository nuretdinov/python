from datetime import datetime
from flask_sqlalchemy  import SQLAlchemy
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   date = db.Column(db.Date, nullable=False)
   name = db.Column(db.String(100), nullable=False)
   text = db.Column(db.Text, nullable=False)

   def __str__(self):
       return (
           f"Название: {self.name}\n"
           f"Дата: {self.date}\n"
           f"Содержание: {self.text}"
       )

@app.route('/', methods=['POST'])
def add_note():
   date = datetime.strptime(request.form['noteDate'], '%Y-%m-%d').date()
   name = request.form['noteName']
   text = request.form['noteText']
   note = Note(date=date, name=name, text=text)
   db.session.add(note)
   db.session.commit()
   return redirect('/')

@app.route("/")
def index():
    return render_template("index.html", h1 = "Добавить заметку")

@app.route("/about")
def get_page_about():
    return render_template("about.html", h1 = "О приложении")

@app.route("/notes")
def view_notes():
   notes = Note.query.order_by(Note.date).all()
   return render_template("notes.html", h1 = "Мои заметки", notes=notes)

if __name__ == "__main__":
   with app.app_context():
       db.create_all()
   app.run(debug=True)