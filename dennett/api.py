from bson.json_util import dumps
from flask import request
from werkzeug.exceptions import InternalServerError


def simple_endpoint(mongo_collection):
    if request.method == 'GET':
        filters = request.args.to_dict()
        items = mongo_collection.fetch(filters)
        return dumps(items)

    if request.method == 'POST':
        data = request.get_json()
        if isinstance(data, list):
            saved_items_ids = mongo_collection.add_batch(data)
        else:
            saved_items_ids = [mongo_collection.add(data)]
        if len(saved_items_ids) == 0:
            raise InternalServerError
        return dumps(saved_items_ids), 201
