from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta

class Sleep:
    def __init__(self, user_id, date, sleep_score, hours_of_sleep, rem_sleep, deep_sleep, heart_rate_below_resting, duration_in_bed):
        self._id = ObjectId()
        self.user = user_id
        self.date = date
        self.sleep_score = sleep_score
        self.hours_of_sleep = hours_of_sleep
        self.rem_sleep = rem_sleep
        self.deep_sleep = deep_sleep
        self.heart_rate_below_resting = heart_rate_below_resting
        self.duration_in_bed = duration_in_bed
        self.hours_in_bed = self._calculate_hours_in_bed()

    def _calculate_hours_in_bed(self):
        start, end = self.duration_in_bed.split(" - ")
        start_time = datetime.strptime(start, "%I:%M%p")
        end_time = datetime.strptime(end, "%I:%M%p")
        if end_time < start_time:
            end_time += timedelta(days=1)
        duration = end_time - start_time
        return f"{duration.total_seconds() / 3600:.2f}"

    def to_dict(self):
        return {
            "_id": self._id,
            "user": self.user,
            "date": self.date,
            "sleep_score": self.sleep_score,
            "hours_of_sleep": self.hours_of_sleep,
            "rem_sleep": self.rem_sleep,
            "deep_sleep": self.deep_sleep,
            "heart_rate_below_resting": self.heart_rate_below_resting,
            "duration_in_bed": self.duration_in_bed,
            "hours_in_bed": self.hours_in_bed
        }