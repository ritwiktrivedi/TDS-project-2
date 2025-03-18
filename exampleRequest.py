import requests
import zipfile
import io
import pandas as pd

url = "https://your-app.vercel.app/api/"
question = "Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the 'answer' column of the CSV file?"
file_path = "abcd.zip"

with open(file_path, 'rb') as f:
    files = {'file': f}
    data = {'question': question}
    response = requests.post(url, files=files, data=data)

if response.status_code == 200:
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall()
    df = pd.read_csv('extract.csv')
    answer_value = df['answer'].iloc[0]
    print(answer_value)
else:
    print(f"Failed to get response: {response.status_code}")
