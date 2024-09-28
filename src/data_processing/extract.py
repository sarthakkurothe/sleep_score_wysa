import csv
from datetime import timedelta, datetime
from src.config import db
from src.models.activity import Activity
from src.models.sleep import Sleep

# Helper function to convert duration strings (e.g., '7:22:00') to hours as a float
def convert_duration_to_hours(duration_str):
    try:
        h, m, s = map(int, duration_str.split(':'))
        return h + m / 60 + s / 3600  # Convert the duration to hours as a float
    except ValueError:
        print(f"Invalid duration format: {duration_str}")
        return None

def extract_activity_data(file_path):
    activities = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                activity = Activity(
                    user_id=row['User'],
                    date=datetime.strptime(row['Date'], '%m/%d/%y').date(),  
                    start_time=row['StartTime'],
                    end_time=row['EndTime'],
                    activity=row['Activity'],
                    log_type=row['LogType'],
                    steps=int(row['Steps']) if row['Steps'] else 0,
                    distance=float(row['Distance']) if row['Distance'] else 0.0,
                    calories=int(row['Calories']) if row['Calories'] else 0
                )
                activities.append(activity)
            except Exception as e:
                print(f"Error processing row {row}: {e}")
    return activities

def extract_sleep_data(file_path):
    sleep_records = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                sleep = Sleep(
                    user_id=row['USER'],
                    date=datetime.strptime(row['DATE'], '%m/%d/%y').date(),
                    sleep_score=int(row['SLEEP SCORE']) if row['SLEEP SCORE'] else None,
                    hours_of_sleep=convert_duration_to_hours(row['HOURS OF SLEEP']) if row['HOURS OF SLEEP'] else None,
                    rem_sleep=float(row['REM SLEEP'].strip('%')) / 100 if row['REM SLEEP'] else None,  # Remove percentage sign and convert to decimal
                    deep_sleep=float(row['DEEP SLEEP'].strip('%')) / 100 if row['DEEP SLEEP'] else None,  # Remove percentage sign and convert to decimal
                    heart_rate_below_resting=float(row['HEART RATE BELOW RESTING'].strip('%')) / 100 if row['HEART RATE BELOW RESTING'] else None,  # Remove percentage sign and convert to decimal
                    duration_in_bed=row['DURATION IN BED']  # Handle this separately if needed (it's a time range)
                )
                sleep_records.append(sleep)
            except Exception as e:
                print(f"Error processing row {row}: {e}")
    return sleep_records

def extract_mood_data(date):
    start_date = datetime.combine(date, datetime.min.time())
    end_date = start_date + timedelta(days=1)
    try:
        return list(db.mood.find({"createdAt": {"$gte": start_date, "$lt": end_date}}))
    except Exception as e:
        print(f"Error extracting mood data: {e}")
        return []
