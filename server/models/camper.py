from server.models import db

class Camper(db.Model):
    __tablename__ = "campers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    signups = db.relationship(
        "Signup",
        backref="camper",
        cascade="all, delete-orphan"
    )

    def validate(self):
        errors = []
        if not self.name or not self.name.strip():
            errors.append("name is required")
        if not isinstance(self.age, int):
            errors.append("age must be an integer")
        elif self.age < 8 or self.age > 18:
            errors.append("age must be between 8 and 18")
        return errors

    def to_dict(self, include_signups=False):
        base = {"id": self.id, "name": self.name, "age": self.age}
        if include_signups:
            base["signups"] = [s.to_dict(nest_activity=True) for s in self.signups]
        return base
