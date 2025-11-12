from flask import Blueprint, jsonify, request
from server.models import db
from server.models.activity import Activity

activities_bp = Blueprint("activities", __name__, url_prefix="/activities")

# GET all activities
@activities_bp.get("/")
def get_all_activities():
    activities = Activity.query.all()
    return jsonify([a.to_dict() for a in activities]), 200

# POST a new activity
@activities_bp.post("/")
def create_activity():
    data = request.get_json()
    activity = Activity(
        name=data.get("name"),
        difficulty=data.get("difficulty")
    )

    errors = activity.validate()
    if errors:
        return jsonify({"errors": errors}), 400

    db.session.add(activity)
    db.session.commit()
    return jsonify(activity.to_dict()), 201

# DELETE an activity (cascade signups)
@activities_bp.delete("/<int:id>")
def delete_activity(id):
    activity = Activity.query.get(id)
    if not activity:
        return jsonify({"error": "Activity not found"}), 404

    db.session.delete(activity)  # cascades to signups
    db.session.commit()
    return "", 204
