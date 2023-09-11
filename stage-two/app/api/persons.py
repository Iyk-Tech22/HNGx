from app.api import bp
from flask import request

@bp.route("/<int:id>", methods=["GET"])
def get_person(id):
    """ Handle get requests """
    pass

@bp.route("/<int:id>", methods=["POST"])
def create_person(id):
    """ Handle POST requests """
    pass

@bp.route("/<int:id>", methods=["PUT"])
def update_person(id):
    """ Handle PUT requests """
    pass

@bp.route("/<int:id>", methods=["DELETE"])
def delete_person(id):
    """ Handle DELETE requests """
    pass
