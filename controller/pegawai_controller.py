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

@pegawai_bp.route('/', methods=['GET'])
def get_all_pegawai():
    all_pegawai = Pegawai.get_all()
    return jsonify(all_pegawai), 200

@pegawai_bp.route('/<nomor_pegawai>', methods=['GET'])
def get_pegawai_detail(nomor_pegawai):
    pegawai = Pegawai.get_by_nomor_pegawai(nomor_pegawai)
    if pegawai:
        return jsonify(pegawai), 200
    else:
        return jsonify({'error': 'Nomor pegawai not found'}), 404
