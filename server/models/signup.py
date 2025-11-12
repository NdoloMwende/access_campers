from . import db

class Signup(db.Model):
    __tablename__ = "signups"

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, nullable=False)

    camper_id = db.Column(db.Integer, db.ForeignKey("campers.id"), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey("activities.id"), nullable=False)

    def validate(self):
        errors = []
        if not isinstance(self.time, int):
            errors.append("time must be an integer")
        else:
            if self.time < 0 or self.time > 23:
                errors.append("time must be between 0 and 23")
        if not self.camper_id:
            errors.append("camper_id is required")
        if not self.activity_id:
            errors.append("activity_id is required")
        return errors

    def to_dict(self, nest_camper=False, nest_activity=False):
        base = {"id": self.id, "camper_id": self.camper_id, "activity_id": self.activity_id, "time": self.time}
        if nest_camper:
            base["camper"] = self.camper.to_dict()
        if nest_activity:
            base["activity"] = self.activity.to_dict()
        return base
