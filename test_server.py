from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/numbers/p', methods=['GET'])
def get_primes():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    return jsonify(random.sample(primes, 4))

@app.route('/api/numbers/f', methods=['GET'])
def get_fibonacci():
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    return jsonify(random.sample(fibonacci, 4))

@app.route('/api/numbers/e', methods=['GET'])
def get_even():
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return jsonify(random.sample(even, 4))

@app.route('/api/numbers/r', methods=['GET'])
def get_random():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    return jsonify(random.sample(random_numbers, 4))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
