import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# # Dummy data and models for illustration
# def predict_head_count(hour, day_of_week):
#     # Replace with actual prediction logic
#     return np.random.randint(1, 10)

# def predict_reservation_frequency(week):
#     # Replace with actual prediction logic
#     return np.random.randint(1, 50)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_head_count', methods=['GET'])
def get_head_count_prediction():
    hour = int(request.args.get('hour'))
    day_of_week = int(request.args.get('day_of_week'))
    prediction = predict_head_count(hour, day_of_week)
    return jsonify({'predicted_head_count': prediction.tolist()})

@app.route('/predict_reservation_frequency', methods=['GET'])
def get_reservation_frequency_prediction():
    week = int(request.args.get('week'))
    prediction = predict_reservation_frequency(week)
    return jsonify({'predicted_reservations': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
