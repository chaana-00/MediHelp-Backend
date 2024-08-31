from flask import Blueprint, request, jsonify, current_app
from services.doctors_service import create_doctor, get_doctors, update_doctor, delete_doctor, get_doctor_by_id, search_doctors_by_specifications, count_doctors
from MySQLdb import IntegrityError
from werkzeug.utils import secure_filename
import os
import logging


doctor_bp = Blueprint('doctor_bp', __name__)

def get_doc_count():
    try:
        mysql = current_app.config['MYSQL']
        count = count_doctors(mysql)
        return jsonify({"doctor_count": count}), 200
    except Exception as e:
        logging.error(f"Error fetching doctor count : {e}")
        return jsonify({"error": str(e)}), 500


def get_all_doctors():
    mysql = current_app.config['MYSQL']
    doctors = get_doctors(mysql)
    return jsonify({
        "data": doctors
    })


def get_doctor(id):
    mysql = current_app.config['MYSQL']
    doctor = get_doctor_by_id(mysql, id)
    if doctor:
        return jsonify(doctor)
    return jsonify({"error": "Doctor not found"}), 404


def add_doctor():
    mysql = current_app.config['MYSQL']
    data = request.form

    try:
        create_doctor(mysql, data)
        return jsonify({"message": "Doctor created successfully"}), 201
    except IntegrityError as e:
        error_message = str(e)
        if "Duplicate entry" in error_message:
            return jsonify({"error": "Doctor already exists"}), 409
        return jsonify({"error": "Database error"}), 500


def update_doctors(id):
    mysql = current_app.config['MYSQL']
    data = request.form

    try:
        update_doctor(mysql, id, data)
        return jsonify({"message": "Doctor updated successfully"}), 200
    except IntegrityError as e:
        error_message = str(e)
        if "Duplicate entry" in error_message:
            return jsonify({"error": "Doctor already exists"}), 409
        return jsonify({"error": "Database error"}), 500


def delete_doctors(id):
    mysql = current_app.config['MYSQL']

    try:
        delete_doctor(mysql, id)
        return jsonify({"message": "Doctor deleted successfully"})
    except IntegrityError as e:
        return jsonify({"error": str(e)}), 404



def search_doctors_by_specifications(spec):
    mysql = current_app.config['MYSQL']
    doctors = get_doctors_by_specifications(mysql, spec)
    if doctors:
        return jsonify(doctors), 200
    return jsonify({"error": "Doctors not found for the specified specifications"}), 404