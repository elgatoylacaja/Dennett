import datetime
from database import mongo
from bson import BSON, decode_all
from bson.objectid import ObjectId
#from prettify import prettify


class Trial():

    @classmethod
    def get(self, collection_name, filters):

        collection = getattr(mongo.db, collection_name)
        trials = collection.find()

        if filters.get('cron', 'old') == 'new':
            trials.sort([('_id', -1)])
        else:
            trials.sort([('_id', 1)])

        page = int(filters.get('page', 1)) - 1
        size = int(filters.get('size', 1000))
        trials.skip(page * size).limit(size)

        #if filters.get('format', 'legacy') == 'pretty':
        #    trials = [prettify(trial) for trial in trials]

        return trials




    @classmethod
    def post(self, collection_name, trial):
        collection = getattr(mongo.db, collection_name)
        trial['postDate'] = datetime.datetime.utcnow()
        result = collection.insert_one(trial)
        inserted_trial = Trial.get_single(collection_name, result.inserted_id)
        return result.inserted_id if inserted_trial else None



    @classmethod
    def get_single(self, collection_name, trial_id):
        collection = getattr(mongo.db, collection_name)
        return collection.find_one({'_id': ObjectId(trial_id)})



    @classmethod
    def stats(self, collection_name):
        collection = getattr(mongo.db, collection_name)
        trials_count = collection.count()
        return { 
            'trials': trials_count
        }
