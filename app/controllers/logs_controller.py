from flask import Blueprint, request, jsonify, g
from datetime import datetime
from http import HTTPStatus

from ..services import LogService
from ..dto import LogDTO

log_bp = Blueprint('log_controller', __name__, url_prefix='/logs')

@log_bp.before_request
def assign_service():
    g.service = LogService(g.db)

@log_bp.route('/', methods=['POST'])
def create_log():
    data = request.get_json()

    try:
        log_dto = LogDTO(
            id=None,
            id_process=data['id_process'],
            status_code=data['status_code'],
            message=data['message']
        )
        created_log = g.service.create_log(log_dto)
        return jsonify(created_log.__dict__), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST

@log_bp.route('/<int:log_id>', methods=['GET'])
def get_log(log_id):
    log = g.service.get_log_by_id(log_id)
    if log:
        return jsonify(log.__dict__)
    return jsonify({'error': 'Log not found'}), HTTPStatus.NOT_FOUND

@log_bp.route('/', methods=['GET'])
def get_all_logs():
    logs = g.service.get_all_logs()
    return jsonify([log.__dict__ for log in logs])

@log_bp.route('/<int:log_id>', methods=['DELETE'])
def delete_log(log_id):
    success = g.service.delete_log(log_id)
    if success:
        return '', HTTPStatus.NO_CONTENT
    return jsonify({'error': 'Log not found'}), HTTPStatus.NOT_FOUND

@log_bp.route('/<int:log_id>', methods=['PUT'])
def update_log(log_id):
    data = request.get_json()

    try:
        log_dto = LogDTO(
            id=log_id,
            id_process=data['id_process'],
            status_code=data['status_code'],
            timestamp=datetime.fromisoformat(data['timestamp']),
            message=data['message']
        )
        updated_log = g.service.update_log(log_dto)
        if updated_log:
            return jsonify(updated_log.__dict__)
        return jsonify({'error': 'Log not found'}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
