from flask import Blueprint, jsonify, request
from server.models import db
from server.models.signup import Signup
from server.models.camper import Camper
from server.models.activity import Activity

signups_bp = Blueprint("signups", __name__, url_prefix="/signups")

@signups_bp.post("")
def create_signup():
    data = request.get_json()
    signup = Signup(
        time=data.get("time"),
        camper_id=data.get("camper_id"),
        activity_id=data.get("activity_id")
    )

    errors = signup.validate()
    if errors:
        return jsonify({"errors": ["validation errors"]}), 400

    camper = Camper.query.get(signup.camper_id)
    activity = Activity.query.get(signup.activity_id)
    if not camper or not activity:
        return jsonify({"errors": ["validation errors"]}), 400

    db.session.add(signup)
    db.session.commit()

    signup = Signup.query.get(signup.id)
    return jsonify(signup.to_dict(nest_activity=True, nest_camper=True)), 201
