from flask import request, jsonify, current_app
from services.prediction_service import create_prediction, get_all_predictions, get_predictions_under_20, count_predictions_under_20, get_predictions_by_user

def create_new_prediction():
    mysql = current_app.config['MYSQL']
    data = request.get_json()
    userId = data.get('userId')
    prediction = data.get('prediction')
    datetime = data.get('datetime')
    age = data.get('age')
    create_prediction(mysql, userId, prediction, datetime, age)
    return jsonify({'message': 'Prediction created successfully'})

def fetch_all_predictions():
    mysql = current_app.config['MYSQL']
    predictions = get_all_predictions(mysql)
    return jsonify(predictions)

def fetch_predictions_under_20():
    mysql = current_app.config['MYSQL']
    predictions = get_predictions_under_20(mysql)
    return jsonify(predictions)

def fetch_count_predictions_under_20():
    mysql = current_app.config['MYSQL']
    count = count_predictions_under_20(mysql)
    return jsonify({'count': count})

def fetch_predictions_by_user(userId):
    mysql = current_app.config['MYSQL']
    predictions = get_predictions_by_user(mysql, userId)
    return jsonify(predictions)
