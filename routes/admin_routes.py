from flask import Blueprint
from controllers.admin_controller import get_admin_by_email_controller

admin_bp = Blueprint('admin', __name__)

admin_bp.route('/email/<string:email>', methods=['GET'])(get_admin_by_email_controller)
