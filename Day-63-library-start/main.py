from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create a new DataBaseModel
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Sets a way in which records in the database will be identified. IF not added Books will be identified by id
    # def __repr__(self):
    #     return '<Books %r>' % self.title


def delete_record(index: int):
    book_to_delete = Books.query.get(index)
    db.session.delete(book_to_delete)
    db.session.commit()


db.create_all()


@app.route('/')
def home():
    books_from_db = Books.query.all()
    all_books = [book.title for book in books_from_db]

    print(all_books)
    if len(all_books) == 0:
        return render_template('index.html', books=None)

    return render_template('index.html', books=books_from_db)


@app.route("/<delete>", methods=["GET", "POST"])
def delete_rec(delete):
    delete_record(index=int(delete))
    return redirect('/')


@app.route("/add", methods=["GET", "POST"])
def add():
    books_from_db = Books.query.all()
    all_books = [book.title for book in books_from_db]

    if request.method == "POST":

        # A Post request has been made hence add new Book to database

        # Check if the book about to be collected already exists in the Database
        if request.form['Book Name'] in all_books:
            print(f"{request.form['Book Name']} already Exists in Database")

            message = f"' {request.form['Book Name']} ' already Exists in Database"
            flash(message, 'info')

            return redirect('/add')

        else:
            db.session.add(Books(title=request.form['Book Name'],
                                 author=request.form['Book Author'],
                                 rating=request.form['Book rating']))
            db.session.commit()

        return redirect('/')

    return render_template('add.html')


@app.route('/edit-<num>', methods=["GET", "POST"])
def edit_rating(num):
    print(num)
    book_for_edit = Books.query.filter_by(id=int(num)).first()
    print(book_for_edit)

    if request.method == "POST":
        # I'm getting the new rating from the form and Editing it from the Database
        new_rating = request.form['New Rating']
        book_to_edit = Books.query.get(int(num))
        book_to_edit.rating = float(new_rating)
        db.session.commit()

        print(Books.id)

        return redirect('/')

    return render_template("edit.html", book_edit=book_for_edit)


if __name__ == "__main__":
    app.run(debug=True)
