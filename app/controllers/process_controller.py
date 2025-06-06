from flask import Blueprint, request, jsonify, g
from http import HTTPStatus

from ..services import ProcessService
from ..dto import ProcessDTO

process_bp = Blueprint('process_controller', __name__, url_prefix='/process')

@process_bp.before_request
def assign_service():
    g.service = ProcessService(g.db)

@process_bp.route('/', methods=['POST'])
def create_process():
    data = request.get_json()
    try:
        process_dto = ProcessDTO(
            id=None,
            name=data['name']
        )
        created_process = g.service.create_process(process_dto)
        return jsonify(created_process.__dict__), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST

@process_bp.route('/<int:process_id>', methods=['GET'])
def get_process(process_id):
    process = g.service.get_process_by_id(process_id)
    if process:
        return jsonify(process.__dict__)
    return jsonify({'error': 'Process not found'}), HTTPStatus.NOT_FOUND

@process_bp.route('/', methods=['GET'])
def get_all_processes():
    processes = g.service.get_all_processes()
    return jsonify([process.__dict__ for process in processes])

@process_bp.route('/<int:process_id>', methods=['DELETE'])
def delete_process(process_id):
    success = g.service.delete_process(process_id)
    if success:
        return '', HTTPStatus.NO_CONTENT
    return jsonify({'error': 'Process not found'}), HTTPStatus.NOT_FOUND

@process_bp.route('/<int:process_id>', methods=['PUT'])
def update_process(process_id):
    data = request.get_json()
    try:
        process_dto = ProcessDTO(
            id=process_id,
            nome=data['nome']
        )
        updated_process = g.service.update_process(process_dto)
        if updated_process:
            return jsonify(updated_process.__dict__)
        return jsonify({'error': 'Process not found'}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
