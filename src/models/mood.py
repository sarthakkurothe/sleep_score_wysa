from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class Mood:
    def __init__(self, user_id, value):
        self._id = ObjectId()
        self.field = "mood_score"
        self.user = user_id
        self.value = value
        self.createdAt = datetime.utcnow()
        self.updatedAt = datetime.utcnow()

    def to_dict(self):
        return {
            "_id": self._id,
            "field": self.field,
            "user": self.user,
            "value": self.value,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
