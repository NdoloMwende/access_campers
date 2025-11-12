from faker import Faker
import random

from server.app import create_app
from server.models import db
from server.models.camper import Camper
from server.models.activity import Activity
from server.models.signup import Signup


app = create_app()
fake = Faker()

with app.app_context():
    # Reset tables
    db.drop_all()
    db.create_all()

    # Seed campers
    campers = []
    for _ in range(10):
        camper = Camper(
            name=fake.name(),
            age=random.randint(8, 18)  # enforce age validation
        )
        campers.append(camper)
        db.session.add(camper)

    # Seed activities (5 random activities)
    activities = []
    for _ in range(5):
        activity = Activity(
            name=fake.sentence(nb_words=3),  # short random phrase
            difficulty=random.randint(1, 5)
        )
        activities.append(activity)
        db.session.add(activity)

    db.session.commit()

    # Seed signups (each camper gets 1–3 random activities)
    for camper in campers:
        chosen_activities = random.sample(activities, random.randint(1, 3))
        for activity in chosen_activities:
            signup = Signup(
                time=random.randint(0, 23),
                camper_id=camper.id,
                activity_id=activity.id
            )
            db.session.add(signup)

    db.session.commit()

    print("Database seeded succesfully!")
