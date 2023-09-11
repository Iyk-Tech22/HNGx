from app.api import bp
from flask import request, jsonify
from app.models import Person
from app import db

@bp.route("/<int:id>", methods=["GET"])
def get_person(id):
    """ Handle get requests """
    try:
        person = Person.query.get(id)
    except:
        return
    else:
        data = jsonify(person.to_dict())
        return (data)

@bp.route("/", methods=["POST"])
def create_person():
    """ Handle POST requests """
    person = Person()
    try:
        name = request.form
        person.from_dict(name)
    except KeyError:
        return
    else:
        db.session.add(person)
        db.session.commit()
        return jsonify(person.to_dict())

@bp.route("/<int:id>", methods=["PUT"])
def update_person(id):
    """ Handle PUT requests """
    try:
        person = Person.query.get(id)
        data = request.form
        person.from_dict(data)
    except:
        return
    else:
        db.session.commit()
        return (jsonify(person.to_dict()))

@bp.route("/<int:id>", methods=["DELETE"])
def delete_person(id):
    """ Handle DELETE requests """
    
