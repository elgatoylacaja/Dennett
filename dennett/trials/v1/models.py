from database import mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.exceptions import InternalServerError, NotFound
import datetime


class Trial():

    @classmethod
    def get_all(self):
        trials = mongo.db.trials.find()
        return dumps(trials)

    @classmethod
    def get(self, id):
        trial = mongo.db.trials.find_one({'_id': ObjectId(id)})
        if trial:
            return dumps(trial)
        else:
            raise NotFound

    @classmethod
    def post(self, trial):
        trial['postDate'] = datetime.datetime.utcnow()
        result = mongo.db.trials.insert_one(trial)
        if result.acknowledged:
            return dumps(result.inserted_id)
        else:
            raise InternalServerError

    @classmethod
    def delete(self, id):
        mongo.db.trials.delete_one({'_id': ObjectId(id)})
