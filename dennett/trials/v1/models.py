from database import mongo
from bson import BSON, decode_all
from bson.objectid import ObjectId
import datetime



class Trial():

    @classmethod
    def get_all(self):
        return mongo.db.trials.find()

    @classmethod
    def get(self, id):
        return mongo.db.trials.find_one({'_id': ObjectId(id)})

    @classmethod
    def post(self, trial):
        trial['postDate'] = datetime.datetime.utcnow()
        result = mongo.db.trials.insert_one(trial)
        inserted_trial = Trial.get(result.inserted_id)
        return result.inserted_id if inserted_trial else None

    @classmethod
    def delete(self, id):
        return mongo.db.trials.delete_one({'_id': ObjectId(id)})

    @classmethod
    def export_to(self, file_name, n):
        trials = mongo.db.trials.find().sort([("_id", 1)]).limit(n)
        with open(file_name, 'w') as f:
            for trial in trials:
                f.write(BSON.encode(trial))

    @classmethod
    def import_from(self, file_name):
        with open(file_name, 'rb') as f:
            trials = decode_all(f.read())
            mongo.db.trials.insert(trials)
