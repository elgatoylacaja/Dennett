import datetime

from bson.objectid import ObjectId

from database import mongo


class TrialsCollection(object):

    def __init__(self, collection_name):
        self._db_collection = getattr(mongo.db, collection_name)

    def fetch(self, filters):
        trials = self._db_collection.find()

        if filters.get('cron', 'old') == 'new':
            trials.sort([('_id', -1)])
        else:
            trials.sort([('_id', 1)])

        page = int(filters.get('page', 1)) - 1
        size = int(filters.get('size', 1000))
        trials.skip(page * size).limit(size)

        # if filters.get('format', 'legacy') == 'pretty':
        #    trials = [prettify(trial) for trial in trials]

        return trials

    def add(self, trial):
        trial['postDate'] = datetime.datetime.utcnow()
        result = self._db_collection.insert_one(trial)
        inserted_trial = self.get_single(result.inserted_id)
        return result.inserted_id if inserted_trial else None

    def add_batch(self, trials):
        saved_trials_ids = []
        for trial in trials:
            inserted_id = self.add(trial)
            saved_trials_ids.append(inserted_id)
        return saved_trials_ids

    def get_single(self, trial_id):
        return self._db_collection.find_one({'_id': ObjectId(trial_id)})

    def stats(self):
        trials_count = self._db_collection.count()
        return {
            'trials': trials_count
        }
