from flask import Blueprint, request, jsonify
from model.pegawai_model import Pegawai

pegawai_bp = Blueprint('pegawai_bp', __name__)

@pegawai_bp.route('/', methods=['POST'])
def store_pegawai():
    data = request.json
    pegawai = Pegawai(**data)
    try:
        pegawai.store_pegawai()
        return jsonify({'message': 'Data pegawai added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
