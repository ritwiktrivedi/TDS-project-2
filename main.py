from flask import Flask, request, jsonify
import os
import zipfile
import pandas as pd

tmp_dir = "tmp_uploads"
os.makedirs(tmp_dir, exist_ok=True)

app = Flask(__name__)

@app.route("/")
def fun():
    return "works"

@app.route('/api/', methods=['POST'])
def process_file():
    question = request.form.get('question')
    file = request.files.get('file')

    if not question or not file:
        return jsonify({"error": "Missing question or file"}), 400

    zip_path = os.path.join(tmp_dir)
    file.save(zip_path)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(tmp_dir)

    extracted_files = zip_ref.namelist()

    return "works"

if __name__ == '__main__':
    app.run(debug=True)
