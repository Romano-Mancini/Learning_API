from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# export FLASK_APP=newAPI_example.py
# export FLASK_ENV=development 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route("/") # Endpoint (1)
def welcome():
    return "Hello!"

@app.route("/drinks") # Endpoint (2)
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        output.append({"id":drink.id, "name":drink.name, "description":drink.description})
    return {"drinks":output}

@app.route("/drink/<id>") # Endpoint (3)
def get_drink(id):
    output = Drink.query.get_or_404(id)
    return jsonify({"name":output.name, "description":output.description})

@app.route("/drinks", methods=["POST"]) # Endpoint (4)
def post_drink():
    posted_drink = Drink(name=request.json["name"], description=request.json["description"])
    db.session.add(posted_drink)
    db.session.commit()
    return jsonify({"id":posted_drink.id})

@app.route("/drinks/<id>", methods=["DELETE"])
def del_drink(id):
    drink_to_delete = Drink.query.get(id)
    if drink_to_delete:
        db.session.delete()
        db.session.commit()
        return jsonify({"message":"Deleted successfully"})
    else:
        return jsonify({"error":"Not found"})