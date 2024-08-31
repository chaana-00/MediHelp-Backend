from flask import Blueprint, request, jsonify, current_app
from services.user_service import create_user, get_users, get_user_by_id, update_user, delete_user, get_user_by_email_from_db, count_users
from MySQLdb import IntegrityError
from werkzeug.utils import secure_filename
import os
import logging

user_bp = Blueprint('user_bp', __name__)

def get_user_count():
    try:
        mysql = current_app.config['MYSQL']
        user_count = count_users(mysql)
        return jsonify({"user_count": user_count}), 200
    except Exception as e:
        logging.error(f"Error fetching user count: {e}")
        return jsonify({"error": str(e)}), 500

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} 
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_all_users():
    mysql = current_app.config['MYSQL']
    users = get_users(mysql)
    return jsonify({
        "data": users
    })


def get_user(id):
    mysql = current_app.config['MYSQL']
    user = get_user_by_id(mysql, id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


def add_user():
    mysql = current_app.config['MYSQL']
    data = request.form
    file = request.files.get('img')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        data = data.to_dict()
        data['img'] = file_path

        try:
            create_user(mysql, data)
            return jsonify({"message": "User created successfully"}), 201
        except IntegrityError as e:
            error_message = str(e)
            if "Duplicate entry" in error_message:
                if "for key 'users.email'" in error_message:
                    return jsonify({"error": "Email already exists"}), 409
                elif "for key 'users.mobile'" in error_message:
                    return jsonify({"error": "Mobile number already exists"}), 409
                elif "for key 'users.nic'" in error_message:
                    return jsonify({"error": "NIC already exists"}), 409
            return jsonify({"error": "Database error"}), 500
    else:
        return jsonify({"error": "Invalid file type"}), 400


def update_user_info(id):
    mysql = current_app.config['MYSQL']
    data = request.form
    file = request.files.get('img')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        data = data.to_dict()
        data['img'] = file_path
    else:
        data = data.to_dict()

    user = get_user_by_id(mysql, id)
    if user:
        try:
            update_user(mysql, id, data)
            return jsonify({"message": "User updated successfully"}), 200
        except IntegrityError as e:
            error_message = str(e)
            if "Duplicate entry" in error_message:
                if "for key 'users.email'" in error_message:
                    return jsonify({"error": "Email already exists"}), 409
                elif "for key 'users.mobile'" in error_message:
                    return jsonify({"error": "Mobile number already exists"}), 409
                elif "for key 'users.nic'" in error_message:
                    return jsonify({"error": "NIC already exists"}), 409
            return jsonify({"error": "Database error"}), 500
    else:
        return jsonify({"error": "User not found"}), 404


def delete_user_info(id):
    mysql = current_app.config['MYSQL']
    user = get_user_by_id(mysql, id)
    if user:
        delete_user(mysql, id)
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404


def get_user_by_email(email):
    mysql = current_app.config['MYSQL']
    user = get_user_by_email_from_db(mysql, email)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404