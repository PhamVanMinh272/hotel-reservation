import os

from flask import Blueprint
from flask import render_template, send_from_directory, current_app

swagger_bp = Blueprint('swagger_bp', __name__)


@swagger_bp.route('/')
def swagger_ui():
    return render_template('swagger_ui.html')

@swagger_bp.route('/spec', methods=['GET'])
def get_spec():
    # 1. Compute the absolute path to your 'app/swagger' folder
    spec_dir = os.path.join(current_app.root_path, 'swagger')

    # 2. Serve the file by filename
    return send_from_directory(spec_dir, 'openapi.yaml', mimetype='application/x-yaml')
