from app.api import bp
from flask import request, jsonify
from app.models import Person
from app import db

@bp.route("/<int:id>", methods=["GET"])
def get_person(id):
    """ Handle GET requests """
    person = Person.query.get(id)
    if person:
        return jsonify(person.to_dict())
    return

@bp.route("", methods=["POST"])
def create_person():
    """ Handle POST request """
    try:
        person = Person()
        data = request.json
        person.from_dict(data)
    except:
        return
    else:
        db.session.add(person)
        db.session.commit()
        response = jsonify(person.	to_dict())
        response.status_code = 201
        return response

@bp.route("/<int:id>", methods=["PUT"])
def update_person(id):
    """ Handle PUT requests """
    person = Person.query.get(id)
    if not person:
        return
    try:
        data = request.json
        person.from_dict(data)
    except:
        return
    db.session.commit()
    return jsonify(person.to_dict())

@bp.route("/<int:id>", methods=["DELETE"])
def delete_person(id):
    """ Handles DELETE requests """
    person = Person.query.get(id)
    if not person:
        return
    db.session.delete(person)
    db.session.commit()
    return "", 204