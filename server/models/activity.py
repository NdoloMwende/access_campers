from server.models import db

class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)

    signups = db.relationship(
        "Signup",
        backref="activity",
        cascade="all, delete-orphan"
    )

    def validate(self):
        errors = []
        if not self.name or not self.name.strip():
            errors.append("name is required")
        if not isinstance(self.difficulty, int):
            errors.append("difficulty must be an integer")
        elif self.difficulty < 1 or self.difficulty > 5:
            errors.append("difficulty must be between 1 and 5")
        return errors

    def to_dict(self, include_signups=False):
        base = {"id": self.id, "name": self.name, "difficulty": self.difficulty}
        if include_signups:
            base["signups"] = [s.to_dict(nest_camper=True) for s in self.signups]
        return base
