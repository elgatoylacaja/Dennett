import datetime

from bson.objectid import ObjectId

from database import mongo


class MongoCollection(object):

    def __init__(self, collection_name):
        self._db_collection = getattr(mongo.db, collection_name)

    def fetch(self, filters):
        items = self._db_collection.find()

        if filters.get('cron', 'old') == 'new':
            items.sort([('_id', -1)])
        else:
            items.sort([('_id', 1)])

        page = int(filters.get('page', 1)) - 1
        size = int(filters.get('size', 1000))

        items.skip(page * size).limit(size)

        # if filters.get('format', 'legacy') == 'pretty':
        #    items = [prettify(trial) for trial in items]

        return items

    def add(self, item):
        item['postDate'] = datetime.datetime.utcnow()
        result = self._db_collection.insert_one(item)

        inserted_item = self.get_single(result.inserted_id)

        return result.inserted_id if inserted_item else None

    def add_batch(self, items):
        saved_items_ids = []
        for item in items:
            inserted_id = self.add(item)
            saved_items_ids.append(inserted_id)
        return saved_items_ids

    def get_single(self, item_id):
        return self._db_collection.find_one({'_id': ObjectId(item_id)})

    def stats(self):
        items_count = self._db_collection.count()
        return {
            'items': items_count
        }
