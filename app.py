from flask import Flask
from controller.pegawai_controller import pegawai_bp
from model.pegawai_model import Pegawai

app = Flask(__name__)

app.register_blueprint(pegawai_bp, url_prefix='/pegawai')

if __name__ == '__main__':
    Pegawai.create_table()
    app.run(port=1234)
