from app.api import bp
from flask import request, jsonify
from app.models import Person
from app import db

@bp.route("/<int:id>", methods=["GET"])
def get_person(id):
    """ Handle GET requests """
    
    person = Person.query.get(id)
    if person:
        response = jsonify(person.to_dict())
        return response
    response = jsonify({"errror": "user not found", "status":401})
    response.status_code = 401
    return response

@bp.route("", methods=["POST"])
def create_person():
    """ Handle POST request """
    try:
        person = Person()
        data = request.json
        print(data)
        person.from_dict(data)
    except KeyError:
       response = jsonify({"errror": "invalid data", "status":400})
       response.status_code = 400
       return response
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
        response = jsonify({"errror": "user not found", "status":401})
        response.status_code = 401
        return response
    try:
        data = request.json
        person.from_dict(data)
    except:
        response = jsonify({"errror": "invalid data", "status":400})
        response.status_code = 400
        return response
    db.session.commit()
    return jsonify(person.to_dict())

@bp.route("/<int:id>", methods=["DELETE"])
def delete_person(id):
    """ Handles DELETE requests """
    person = Person.query.get(id)
    if not person:
        response = jsonify({"errror": "user not found", "status":401})
        response.status_code = 401
        return response
    db.session.delete(person)
    db.session.commit()
    return "", 204