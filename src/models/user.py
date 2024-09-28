from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class User:
    def __init__(self, name, timezone, version, app, country):
        self._id = ObjectId()
        self.name = name
        self.timezone = timezone
        self.version = version
        self.app = app
        self.country = country
        self.createdAt = datetime.utcnow()
        self.updatedAt = datetime.utcnow()

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "timezone": self.timezone,
            "version": self.version,
            "app": self.app,
            "country": self.country,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }