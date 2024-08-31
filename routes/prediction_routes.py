from flask import Blueprint
from controllers.prediction_controller import create_new_prediction, fetch_all_predictions, fetch_predictions_under_20, fetch_count_predictions_under_20, fetch_predictions_by_user

prediction_bp = Blueprint('prediction_bp', __name__)

prediction_bp.route('/create', methods=['POST'])(create_new_prediction)
prediction_bp.route('/all', methods=['GET'])(fetch_all_predictions)
prediction_bp.route('/under_20', methods=['GET'])(fetch_predictions_under_20)
prediction_bp.route('/count_under_20', methods=['GET'])(fetch_count_predictions_under_20)
prediction_bp.route('/user/<int:userId>', methods=['GET'])(fetch_predictions_by_user)