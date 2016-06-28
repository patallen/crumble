import json

from flask import Blueprint, make_response, request

from app.models import Document


public = Blueprint('public', __name__)


@public.route("/documents/<title>", methods=['GET'])
def get_document(title):
    document = Document.query.filter_by(title=title).first()
    if document:
        document = document.to_dict()
    else:
        document = {"title": title}
    return make_response(json.dumps(document))


@public.route("/documents/<title>", methods=['POST'])
def post_document(title):
    req = request.get_json()
    document = Document.query.filter_by(title=title).first()
    if document is None:
        document = Document(title=title)
    if req.get('title'):
        req.pop('title')
    document.update_attributes(req)
    document.save()
    return make_response(json.dumps(document.to_dict()))
