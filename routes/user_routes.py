from flask import Blueprint
from controllers.user_controller import get_all_users, get_user, add_user, update_user_info, delete_user_info, get_user_by_email, get_user_count

user_bp = Blueprint('user', __name__)

user_bp.route('/all', methods=['GET'])(get_all_users)
user_bp.route('/search/<int:id>', methods=['GET'])(get_user)
user_bp.route('/email/<string:email>', methods=['GET'])(get_user_by_email)
user_bp.route('/create', methods=['POST'])(add_user)
user_bp.route('/update/<int:id>', methods=['PUT'])(update_user_info)
user_bp.route('/delete/<int:id>', methods=['DELETE'])(delete_user_info)
user_bp.route('/count', methods=['GET'])(get_user_count)
