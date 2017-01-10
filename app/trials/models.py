from database import db
from flask import jsonify
from flask import json


class Trial(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(512))
    op_type = db.Column(db.String(512))

    def __init__(self, data):
        self.user = data.get('user')
        self.op_type = data.get('op_type')

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
