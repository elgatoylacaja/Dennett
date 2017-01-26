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
    def export_trials(self, n):
        trials = mongo.db.trials.find().sort([('_id', 1)]).limit(n)
        max_id = trials[n]['_id'] 
        date = datetime.datetime.utcnow().isoformat()
        filename = 'backup_{}'.format(date)
        with open(filename, 'w') as f:
            [f.write(BSON.encode(trial)) for trial in trials]
        mongo.db.trials.update({'_id': {'$lt': max_id}}, {'$set': {'exported': True}}, multi=True)
        return filename

    @classmethod
    def import_trials(self, filename):
        with open(filename, 'rb') as f:
            trials = decode_all(f.read())
            mongo.db.trials.insert(trials)

    @classmethod
    def delete_exported_trials(self):
        mongo.db.trials.remove({'exported': {'$eq': True}})

    @classmethod
    def stats(self):
        trials_count = mongo.db.trials.count()
        return { 
            'trials': trials_count
        }
