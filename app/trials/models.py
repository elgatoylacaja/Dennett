from database import db, mongo
from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import datetime


class Trial(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(512))
    op_type = db.Column(db.String(512))

    def __init__(self, data):
        self.user = data.get('user')
        self.op_type = data.get('op_type')

    @classmethod
    def get_mongolab_all(self):
        trials = mongo.db.trials.find()
        return dumps(trials)

    @classmethod
    def get_mongolab(self, id):
        trial = mongo.db.trials.find_one({'_id': ObjectId(id)})
        if trial:
            return dumps(trial)
        return trial

    @classmethod
    def post_mongolab(self, trial):
        trial['postDate'] = datetime.datetime.utcnow()
        mongo.db.trials.insert(trial)
        return dumps(trial)

    @classmethod
    def delete_mongolab(self, id):
        mongo.db.trials.delete_one({'_id': ObjectId(id)})

    @classmethod
    def get(self, request_filters):
        trials = Trial.query
        if request_filters.get('op_type'):
            trials = trials.filter_by(op_type=request_filters.get('op_type'))
        if request_filters.get('user'):
            trials = trials.filter_by(user=request_filters.get('user'))
        page = Trial.paginate(trials.all())
        return jsonify(page)

    def save(self):
        db.session.add(self)
        db.session.commit()
        instance = self.serialize(self)
        return jsonify(instance)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def paginate(self, trials):
        return {
            'data': [Trial.serialize(t) for t in trials]
        }

    @classmethod
    def serialize(self, trial):
        return {
            'user': trial.user, 
            'op_type': trial.op_type
        }
