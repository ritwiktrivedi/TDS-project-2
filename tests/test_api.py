import requests
import zipfile
import io

url = "http://127.0.0.1:5000"
questions = [
    # {
    #     "files": None,
    #     "question": """Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.\n    Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2005217@ds.study.iitm.ac.in\n    What is the JSON output of the command? (Paste only the JSON body, not the headers)""",
    # },
    # {
    #     "files": "README.md",
    #     "question": "Let's make sure you know how to use npx and prettier.\n    Download . In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md | sha256sum.\n    What is the output of the command?",
    # },
    {
        "question": "Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below.\n    What is the output of code -s?"
    }
]

for question in questions:
    data = {"question": question.get("question")}
    print(data)
    response = requests.post(url, data=data)
    print(response.text)
    # if file_path is not None:
    #     zipped_file = io.BytesIO()
    #     with zipfile.ZipFile(zipped_file, "w") as z:
    #         for file in file_path:
    #             z.write(file)
    #     zipped_file.seek(0)
    #     files = {"file": zipped_file}
    #     response = requests.post(url, files=files, data=data)
    # else:
    #     files = {"file": open(file_path, "rb")}
    #     response = requests.post(url, files=files, data=data)

    # print(response.text)
