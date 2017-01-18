from database import mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
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
        return trial

    @classmethod
    def post(self, trial):
        trial['postDate'] = datetime.datetime.utcnow()
        mongo.db.trials.insert(trial)
        return dumps(trial)

    @classmethod
    def delete(self, id):
        mongo.db.trials.delete_one({'_id': ObjectId(id)})
