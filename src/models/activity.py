from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class Activity:
    def __init__(self, user_id, date, start_time, end_time, activity, log_type, steps, distance, calories):
        self._id = ObjectId()
        self.user = user_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.duration = (datetime.strptime(end_time, "%I:%M:%S %p") - datetime.strptime(start_time, "%I:%M:%S %p")).total_seconds() / 60
        self.activity = activity
        self.log_type = log_type
        self.steps = steps
        self.distance = distance
        self.calories = calories

    def to_dict(self):
        return {
            "_id": self._id,
            "user": self.user,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration": self.duration,
            "activity": self.activity,
            "log_type": self.log_type,
            "steps": self.steps,
            "distance": self.distance,
            "calories": self.calories
        }
