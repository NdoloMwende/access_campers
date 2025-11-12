from flask import Blueprint, jsonify
from server.models import db
from server.models.activity import Activity

activities_bp = Blueprint("activities", __name__, url_prefix="/activities")

@activities_bp.get("")
def get_all_activities():
    activities = Activity.query.all()
    result = [a.to_dict() for a in activities]
    return jsonify(result), 200

@activities_bp.delete("/<int:id>")
def delete_activity(id):
    activity = Activity.query.get(id)
    if not activity:
        return jsonify({"error": "Activity not found"}), 404

    db.session.delete(activity)  # cascades to signups automatically
    db.session.commit()
    return "", 204
