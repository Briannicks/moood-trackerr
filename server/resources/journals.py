from flask import request, session
from flask_restful import Resource

from config import db
from helpers import find_owned, login_required, paginate
from models import Journal
from schemas import JournalSchema

journal_schema = JournalSchema()
journals_schema = JournalSchema(many=True)

EDITABLE_FIELDS = ("title", "content")


class Journals(Resource):
    method_decorators = [login_required]

    def get(self):
        query = Journal.query.filter_by(user_id=session["user_id"]).order_by(
            Journal.created_at.desc(), Journal.id.desc()
        )
        return paginate(query, journals_schema), 200
        