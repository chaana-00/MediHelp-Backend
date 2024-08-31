from flask import Blueprint
from controllers.chatbot_controller import chat

chat_bp = Blueprint('chatbot', __name__)

chat_bp.route('/chat', methods=['POST'])(chat)

