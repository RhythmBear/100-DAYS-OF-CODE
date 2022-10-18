from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

API_KEY = "ADMINRIGHTS23629459"

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ------------------------------ CLASS AND FUNCTIONS -----------------------------#
# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # TO Dictionary Function
    def to_dict(self):
        # Using Dictionary Comprehension to access the attributes in the Cafe class and creating a Dict with it
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random_cafe')
def random_cafe():
    cafes_list = Cafe.query.all()
    cafe_to_get = random.choice(cafes_list)
    print(cafe_to_get)

    return jsonify(cafe_to_get.to_dict())


@app.route("/all_cafes")
def all_cafes():
    cafes = Cafe.query.all()
    return jsonify(
        {"cafes": [cafe.to_dict() for cafe in cafes]}
    )


@app.route('/search')
def search():
    # Collect search parameter from URL e.g ?location="Location to be searched for"
    cafe_location = request.args['location']
    cafes_gotten_from_db = Cafe.query.filter_by(location=cafe_location).all()
    print(cafe_location, cafes_gotten_from_db)

    if len(cafes_gotten_from_db) != 0:
        return jsonify({
            "cafes": [cafe.to_dict() for cafe in cafes_gotten_from_db]
        })

    else:
        return jsonify(
            {
                "errors": {
                    'Not Found': f"Sorry we do not have a cafe in {cafe_location}"
                    }

            }
        )


# HTTP POST - Create Record
@app.route('/add_cafe', methods=['POST'])
def add_cafe():
    print(request.form)
    for column in Cafe.__table__.columns:
        if column.name == "id":
            continue
        print(f"{column.name}: {request.form[column.name]}")

        # Check if the Cafe does not already exist in the Database
    cafe_check = Cafe.query.filter_by(name=request.form['name']).first()
    print(cafe_check)

    if cafe_check:
        return jsonify(
            {
                'error': f"{request.form['name']} already exists"
            }
        )

    else:
        new_cafe = Cafe(name=request.form['name'],
                        map_url=request.form['map_url'],
                        img_url=request.form['img_url'],
                        location=request.form['location'],
                        seats=request.form['seats'],
                        has_toilet=request.form['has_toilet'] == "True",
                        has_wifi=request.form['has_wifi'] == "True",
                        has_sockets=request.form['has_sockets'] == "True",
                        can_take_calls=request.form['can_take_calls'] == "True",
                        coffee_price=request.form['coffee_price']
                        )
        db.session.add(new_cafe)
        db.session.commit()

    return "Success"


# HTTP PUT/PATCH - Update Record
@app.route('/update_price/<cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    if request.method == "PATCH":

        cafe_to_update = Cafe.query.get(int(cafe_id))
        print(cafe_to_update)
        # Checks to see if the cafe exists
        if cafe_to_update:
            cafe_to_update.coffee_price = request.args['coffee_price']
            db.session.commit()

            return jsonify(
                {
                    "response": f"Successfully Changed {cafe_to_update.name}'s Coffee price to {cafe_id}"
                }

            )
        else:
            return jsonify(
                {
                    "response": {"error": f"Cafe with {cafe_id} does not exist in database"}
                }

            )


# HTTP DELETE - Delete Record
@app.route('/delete_cafe/<cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.method == "DELETE":
        if request.args['API_KEY'] == API_KEY:
            cafe_to_delete = Cafe.query.get(int(cafe_id))
            db.session.delete(cafe_to_delete)
            db.session.commit()

            return jsonify(
                {"response": f"Successfully deleted {cafe_to_delete.name} from database"}
            )

        else:
            return jsonify(
                {
                    "error": f"You do not have the rights to edit a Cafe, Ensure you have the right API key"
                }
            )


if __name__ == '__main__':
    app.run(debug=True, port=80)
