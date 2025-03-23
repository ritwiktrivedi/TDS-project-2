import requests
import zipfile
import io
import pandas as pd

url = "http://127.0.0.1:5000/api"
question = """Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.\n    Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2005217@ds.study.iitm.ac.in\n    What is the JSON output of the command? (Paste only the JSON body, not the headers)"""

# files = {'file': open(file_path, 'rb')}
data = {'question': question}
response = requests.post(url,
    # files=files,
    data=data)
print(response.text)
