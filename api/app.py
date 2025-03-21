from flask import Flask, request, jsonify
import os

from utils.question_matching import find_similar_question
from utils.openai_api import extract_parameters
from utils.solution_functions import functions_dict
from utils.file_process import unzip_folder


tmp_dir = "tmp_uploads"
os.makedirs(tmp_dir, exist_ok=True)

app = Flask(__name__)

@app.route("/")
def fun():
    return "works"

@app.route('/api/', methods=['POST'])
def process_file():
    question = request.form.get('question')  # Get the question from the form data
    file = request.files.get('file')  # Get the uploaded file (optional)

    # Handle the file processing if file is present
    if file:
        # Your file processing logic goes here (e.g., extracting data from a CSV file)
        unzip_folder(file, tmp_dir)
        pass

    # Match the question to the appropriate function
    matched_function = find_similar_question(question) # Function to compare using cosine similarity

    # Extract the parameters required for the matched function
    parameters = extract_parameters(str(question))  # Function to call OpenAI API and extract parameters

    # the solutions functions name is same as in questions.json
    solution_function = functions_dict.get(str(matched_function), lambda parameters: "No matching function found")

    answer = solution_function(matched_function, parameters)

    # Return the answer in JSON format
    return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(debug=True)
