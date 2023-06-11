from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Define the route for the API endpoint
@app.route('/ohlc-data', methods=['GET'])
def get_ohlc_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Read the JSON file and filter data based on start and end dates
    json_data = read_and_filter_json(start_date, end_date)

    return jsonify(json_data)

def read_and_filter_json(start_date, end_date):
    # Read the JSON file into a Python object (e.g., list or dictionary)
    with open('nifty_1min_2015_2022.json', 'r') as file:
        ohlc_data = json.load(file)
        # Convert start_date and end_date to datetime objects
        # Convert start_date and end_date to datetime objects
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')

    # Filter the OHLC data based on start and end dates
    filtered_data = [item for item in ohlc_data if start_datetime <= datetime.fromtimestamp(int(item['Date'])) <= end_datetime]

    return filtered_data

if __name__ == '__main__':
    app.run()


# ** Sample Usage of API
# http://127.0.0.1:5000/ohlc-data?start_date=2021-06-01&end_date=2021-06-10
