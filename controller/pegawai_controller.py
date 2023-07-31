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

@pegawai_bp.route('/<nomor_pegawai>', methods=['PUT'])
def update_pegawai(nomor_pegawai):
    data = request.json
    existing_pegawai = Pegawai.get_by_nomor_pegawai(nomor_pegawai)
    if existing_pegawai:
        Pegawai.update(nomor_pegawai, data)
        return jsonify({'message': 'Data pegawai updated successfully'}), 200
    else:
        return jsonify({'error': 'Nomor pegawai not found'}), 404
    
@pegawai_bp.route('/<nomor_pegawai>', methods=['DELETE'])
def delete_pegawai(nomor_pegawai):
    existing_pegawai = Pegawai.get_by_nomor_pegawai(nomor_pegawai)
    if existing_pegawai:
        Pegawai.delete(nomor_pegawai)
        return jsonify({'message': 'Data pegawai deleted successfully'}), 200
    else:
        return jsonify({'error': 'Nomor pegawai not found'}), 404
    
@pegawai_bp.route('/divisi/<int:id_divisi>', methods=['GET'])
def get_pegawai_by_divisi(id_divisi):
    pegawai_list = Pegawai.get_by_divisi(id_divisi)
    if pegawai_list:
        return jsonify(pegawai_list), 200
    else:
        return jsonify({'error': 'Nomor divisi not found'}), 404
