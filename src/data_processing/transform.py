from datetime import datetime, timedelta

def transform_data(activities, sleep_records, mood_data):
    result = {}
    
    for activity in activities:
        user_id = activity.user
        date = activity.date
        
        if user_id not in result:
            result[user_id] = {}
        
        if date not in result[user_id]:
            result[user_id][date] = {
                "user": user_id,
                "date": date,
                "mood_score": None,
                "activity": [],
                "sleep": None
            }
        
        result[user_id][date]["activity"].append({
            "activity": activity.activity,
            "steps": activity.steps,
            "distance": activity.distance,
            "duration": activity.duration,
            "calories": activity.calories
        })
    
    for sleep in sleep_records:
        user_id = sleep.user
        date = sleep.date
        
        if user_id in result and date in result[user_id]:
            result[user_id][date]["sleep"] = {
                "sleep_score": sleep.sleep_score,
                "hours_of_sleep": sleep.hours_of_sleep,
                "hours_in_bed": sleep.hours_in_bed
            }
    
    for mood in mood_data:
        user_id = str(mood["user"])
        date = mood["createdAt"].date()
        
        if user_id in result and date in result[user_id]:
            result[user_id][date]["mood_score"] = mood["value"]
    
    return [data for user_data in result.values() for data in user_data.values()]
