# CAMP API

A simple Flask RESTful API for managing campers, activities, and signups at a summer camp. This project demonstrates Flask, SQLAlchemy, Flask-Migrate, validations, and API best practices..

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the API](#running-the-api)
- [Seeding the Database](#seeding-the-database)
- [API Endpoints](#api-endpoints)
- [Quick Postman Test Examples](#quick-postman-test-examples)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Project Overview

This project simulates a camp management system with three core entities:

- **Camper** – camp attendees, age 8–18
- **Activity** – camp activities with a difficulty rating
- **Signup** – links campers to activities, including a time (hour of day)

Relationships:

- A camper can sign up for multiple activities.
- An activity can have multiple campers.
- Signups belong to both a camper and an activity.
- Deleting an activity or camper cascades to related signups.

---

## Features

- RESTful API using Flask and SQLAlchemy
- CRUD operations for Campers and Activities
- Create and manage Signups
- Validation for camper age, signup time, and required fields
- Cascading deletes for Signups
- Structured JSON responses
- Error handling with proper HTTP status codes

---

## Project Structure

```

access_camp/
│
├── server/
│   ├── app.py              # Flask application factory
│   ├── config.py           # Configuration settings
│   ├── models/             # SQLAlchemy models
│   │   ├── **init**.py
│   │   ├── camper.py
│   │   ├── activity.py
│   │   └── signup.py
│   ├── routes/             # API route handlers
│   │   ├── campers.py
│   │   ├── activities.py
│   │   └── signups.py
│   ├── migrations/         # Alembic migrations folder
│   └── seed.py             # Database seeding script
│
├── instance/
│   └── app.db              # SQLite database file
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

````

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd access_camp
````

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the Flask server:

```bash
python server/app.py
```

The API will run at: `http://localhost:5555`

---

## Seeding the Database

To populate the database with initial data:

```bash
python server/seed.py
```

---

## API Endpoints

| Method | Route            | Description                               |
| ------ | ---------------- | ----------------------------------------- |
| GET    | /campers         | List all campers                          |
| GET    | /campers/<id>    | Retrieve camper details including signups |
| POST   | /campers         | Create a new camper                       |
| PATCH  | /campers/<id>    | Update camper's name and/or age           |
| GET    | /activities      | List all activities                       |
| POST   | /activities      | Create a new activity                     |
| DELETE | /activities/<id> | Delete an activity (cascade signups)      |
| GET    | /signups         | List all signups                          |
| POST   | /signups         | Create a signup for a camper & activity   |

---

## Quick Postman Test Examples

### Campers

**GET all campers**

* `http://localhost:5555/campers`

**GET camper by ID**

* `http://localhost:5555/campers/1`

**POST create a camper**

* `http://localhost:5555/campers`
* Body:

```json
{
  "name": "Zoe",
  "age": 11
}
```

**PATCH update a camper**

* `http://localhost:5555/campers/1`
* Body:

```json
{
  "name": "Ashley",
  "age": 12
}
```

---

### Activities

**GET all activities**

* `http://localhost:5555/activities`

**POST create an activity**

* `http://localhost:5555/activities`
* Body:

```json
{
  "name": "Archery",
  "difficulty": 3
}
```

**DELETE an activity**

* `http://localhost:5555/activities/1`

---

### Signups

**GET all signups**

* `http://localhost:5555/signups`

**POST create a signup**

* `http://localhost:5555/signups`
* Body:

```json
{
  "camper_id": 1,
  "activity_id": 2,
  "time": 9
}
```

**Validation Error Example**

```json
{
  "camper_id": 1,
  "activity_id": 2,
  "time": 25
}
```

Returns:

```json
{
  "errors": ["validation errors"]
}
```
---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Description"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

---

## License

This project is for **educational purposes**. You may modify and use it as a learning resource.

---

## Author

**Mercy Ndolo Mwende**

* [LinkedIn](https://www.linkedin.com/in/mercyndolomwende)
* [GitHub](https://github.com/NdoloMwende)
