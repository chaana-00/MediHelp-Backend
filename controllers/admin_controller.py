from flask import current_app, jsonify, request
from services.admin_service import get_admin_by_email

def get_admin_by_email_controller(email):
    mysql = current_app.config['MYSQL']
    admin = get_admin_by_email(mysql, email)
    if admin:
        return jsonify(admin)
    return jsonify({"error": "Admin not found"}), 404
