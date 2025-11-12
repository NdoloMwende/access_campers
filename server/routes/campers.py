from flask import Blueprint, jsonify, request
from models import db
from models.camper import Camper

campers_bp = Blueprint("campers", __name__, url_prefix="/campers")

@campers_bp.get("")
def get_all_campers():
    campers = Camper.query.all()
    result = [c.to_dict() for c in campers]
    return jsonify(result), 200

@campers_bp.get("/<int:id>")
def get_camper(id):
    camper = Camper.query.get(id)
    if not camper:
        return jsonify({"error": "Camper not found"}), 404
    return jsonify(camper.to_dict(include_signups=True)), 200

@campers_bp.post("")
def create_camper():
    data = request.get_json()
    camper = Camper(name=data.get("name"), age=data.get("age"))

    errors = camper.validate()
    if errors:
        return jsonify({"errors": ["validation errors"]}), 400

    db.session.add(camper)
    db.session.commit()
    return jsonify(camper.to_dict()), 201

@campers_bp.patch("/<int:id>")
def update_camper(id):
    camper = Camper.query.get(id)
    if not camper:
        return jsonify({"error": "Camper not found"}), 404

    data = request.get_json()
    camper.name = data.get("name", camper.name)
    camper.age = data.get("age", camper.age)

    errors = camper.validate()
    if errors:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400

    db.session.commit()
    return jsonify(camper.to_dict()), 202
