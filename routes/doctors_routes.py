from flask import Blueprint
from controllers.doctors_controllers import get_all_doctors, add_doctor, get_doctor, delete_doctors, update_doctors, search_doctors_by_specifications, get_doc_count

doctor_bp = Blueprint('doctor', __name__)

doctor_bp.route('/all', methods=['GET'])(get_all_doctors)
doctor_bp.route('/create', methods=['POST'])(add_doctor)
doctor_bp.route('/search/<int:id>', methods=['GET'])(get_doctor)
doctor_bp.route('/update/<int:id>', methods=['PUT'])(update_doctors)
doctor_bp.route('/delete/<int:id>', methods=['DELETE'])(delete_doctors)
doctor_bp.route('/search/specifications/<string:spec>', methods=['GET'])(search_doctors_by_specifications)
doctor_bp.route('/count', methods=['GET'])(get_doc_count)
