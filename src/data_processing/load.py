import json

def load_data(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, default=str, indent=2)
