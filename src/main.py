from datetime import date
from src.data_processing.extract import extract_activity_data, extract_sleep_data, extract_mood_data
from src.data_processing.transform import transform_data
from src.data_processing.load import load_data

def main():
    activity_data = extract_activity_data('data/activity_data.csv')
    sleep_data = extract_sleep_data('data/sleep_data.csv')
    mood_data = extract_mood_data(date.today())  

    transformed_data = transform_data(activity_data, sleep_data, mood_data)

    load_data(transformed_data, 'perceived_energy_scores.json')

if __name__ == "__main__":
    main()