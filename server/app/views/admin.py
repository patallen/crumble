import json
from flask import Blueprint, make_response
from app.models import Document, Action
from app import db

admin = Blueprint('admin', __name__)


@admin.route("/actions", methods=['GET'])
def get_actions():
    actions = Action.query.all()
    actions = [action.to_dict() for action in actions]
    return make_response(json.dumps(actions))


@admin.route("/documents/<title>", methods=['DELETE'])
def delete_document(title):
    document = Document.query.filter_by(title=title).first()
    if document is None:
        return make_response(404)
    try:
        db.session.delete(document)
        db.session.commit()
        return make_response(200)
    except:
        return make_response(500)


@admin.route("/documents", methods=['GET'])
def get_documents_admin():
    docs = Document.query.all()
    json_docs = [d.to_dict() for d in docs]
    return make_response(json.dumps(json_docs))
