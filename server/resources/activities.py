from flask import request, session
from flask_restful import Resource

from config import db
from helpers import find_owned, login_required, paginate
from models import Activity, Mood
from schemas import ActivitySchema, MoodSchema

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)
mood_schema = MoodSchema()


def name_taken(name, exclude_id=None):
    """Check whether the logged-in user already has an activity with this name."""
    query = Activity.query.filter_by(user_id=session["user_id"], name=(name or "").strip())
    if exclude_id is not None:
        query = query.filter(Activity.id != exclude_id)
    return query.first() is not None