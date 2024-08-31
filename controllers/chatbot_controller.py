from flask import current_app, jsonify, request
from services.chatbot_service import get_initial_message, handle_message, calculate_bmi


def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": get_initial_message()})

    response = handle_message(user_message)
    return jsonify({"response": response})
