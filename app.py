from flask import Flask, jsonify, request
from collections import deque
import requests

app = Flask(__name__)

WINDOW_SIZE = 10
numbers_queue = deque(maxlen=WINDOW_SIZE)
prev_numbers = []

THIRD_PARTY_API = "http://localhost:5001/api/numbers/"  

def get_number_from_third_party(number_id):
    try:
        response = requests.get(THIRD_PARTY_API + number_id, timeout=0.5)  
        response.raise_for_status()
        numbers = response.json()
        return numbers
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching numbers: {e}")
        return []

def calculate_average(queue):
    if not queue:
        return 0
    return sum(queue) / len(queue)

@app.route('/numbers/<string:number_id>', methods=['GET'])
def get_average(number_id):
    try:
        numbers = get_number_from_third_party(number_id)

        for number in numbers:
            if number not in numbers_queue:
                numbers_queue.append(number)
                prev_numbers.clear()
                prev_numbers.extend(numbers_queue)

        average = calculate_average(numbers_queue)

        response = {
            'windowPrevState': list(prev_numbers),
            'windowCurrState': list(numbers_queue),
            'numbers': numbers,
            'avg': average
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=9876)