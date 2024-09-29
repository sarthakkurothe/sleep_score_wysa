# Perceived Energy Score - WYSA

## Overview

This project calculates a Perceived Energy score for users based on their mood, activity, and sleep data. It processes data from CSV files and a MongoDB database, combines the information, and outputs a JSON file with the calculated scores.
## Project Structure


```
perceived_energy_score/
│
├── data/
│   ├── activity_data.csv
│   └── sleep_data.csv
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── mood.py
│   │   ├── activity.py
│   │   └── sleep.py
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   └── main.py
│
├── requirements.txt
└── README.md

```


## Technology Stack

- Python 3.7+
- MongoDB Atlas (Cloud-hosted MongoDB)
- PyMongo (Python driver for MongoDB)
- CSV (for input data)
- JSON (for output data)

## Prerequisites

- Python 3.7 or higher installed
- pip (Python package installer)
- MongoDB Atlas account
- Git (for version control)

## Installation

1. Clone the repository:

```bash
  git clone https://github.com/sarthakkurothe/sleep_score_wysa.git
  cd sleep_score_wysa
```

2. Set up a virtual environment:

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
  pip install -r requirements.txt
```
4. Set up MongoDB Atlas:

- Create a MongoDB Atlas account if you don't have one
- Create a new cluster
- Create a database named "wysa_db"
- Create collections: "users" and "moods"
- Add sample data to these collections (refer to the "Data Preparation" section)

5. Configure the MongoDB connection: 
In ```src/config.py```, replace the MONGODB_URI with your MongoDB Atlas connection string. Ensure you've replaced <password> in the URI with your actual password

6. Prepare your data:

- Place your ```activity_data.csv``` and ```sleep_data.csv``` files in the data directory


## Data Preparation

- Users Collection: Insert documents like this for each user:

```bash
{
  "name": "A",
  "timezone": "America/Los_Angeles",
  "version": 70,
  "app": "Wysa",
  "country": "US",
  "createdAt": {"$date": "2022-04-01T00:00:00Z"},
  "updatedAt": {"$date": "2022-04-07T23:59:59Z"}
}
```

- Moods Collection: Insert documents like this for each mood entry:

```bash
{
  "field": "mood_score",
  "user": {"$oid": "USER_OBJECTID_HERE"},
  "value": 8,
  "createdAt": {"$date": "2022-04-01T12:00:00Z"},
  "updatedAt": {"$date": "2022-04-01T12:00:00Z"}
}
```
Replace "USER_OBJECTID_HERE" with the actual ObjectId of the user.


## Running the Project

- Ensure you're in the project root directory and your virtual environment is activated (if you're using one).

- Run the main script:

```bash
   python -m src.main
```
- The script will process the data and generate a file named ```perceived_energy_scores.json``` in the project root directory.

## Output

```bash
[
  {
    "user": "user_id_here",
    "date": "2022-04-01",
    "mood_score": 8,
    "activity": [
      {
        "activity": "Walk",
        "steps": 5768,
        "distance": 0,
        "duration": 86.2,
        "calories": 508
      }
    ],
    "sleep": {
      "sleep_score": 90,
      "hours_of_sleep": "7:22:00",
      "hours_in_bed": "8:12:00"
    }
  },
  // ... more entries
]
```

## Troubleshooting

- If you encounter MongoDB connection issues, double-check your connection string and ensure your IP address is whitelisted in MongoDB Atlas.
- If you're having problems with the CSV files, ensure they're in the correct format and located in the `data`/ directory.
- For any Python-related errors, make sure you've installed all required packages and are using a compatible Python version.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.
