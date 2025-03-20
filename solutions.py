import requests
import subprocess
import hashlib
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import zipfile
import pandas as pd
import os

def vs_code_version():
    return """
Version:          Code 1.98.2 (ddc367ed5c8936efe395cffeec279b04ffd7db78, 2025-03-12T13:32:45.399Z)
OS Version:       Linux x64 6.12.15-200.fc41.x86_64
CPUs:             11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz (8 x 1300)
Memory (System):  7.40GB (3.72GB free)
Load (avg):       3, 2, 2
VM:               0%
Screen Reader:    no
Process Argv:     --crash-reporter-id 80b4d7e7-0056-4767-b601-6fcdbec0b54d
GPU Status:       2d_canvas:                              enabled
                  canvas_oop_rasterization:               enabled_on
                  direct_rendering_display_compositor:    disabled_off_ok
                  gpu_compositing:                        enabled
                  multiple_raster_threads:                enabled_on
                  opengl:                                 enabled_on
                  rasterization:                          enabled
                  raw_draw:                               disabled_off_ok
                  skia_graphite:                          disabled_off
                  video_decode:                           enabled
                  video_encode:                           disabled_software
                  vulkan:                                 disabled_off
                  webgl:                                  enabled
                  webgl2:                                 enabled
                  webgpu:                                 disabled_off
                  webnn:                                  disabled_off

CPU %	Mem MB	   PID	Process
    2	   189	 18772	code main
    0	    45	 18800	   zygote
    2	   121	 19189	     gpu-process
    0	    45	 18801	   zygote
    0	     8	 18825	     zygote
    0	    61	 19199	   utility-network-service
    0	   106	 20078	ptyHost
    2	   114	 20116	extensionHost [1]
   21	   114	 20279	shared-process
    0	     0	 20778	     /usr/bin/zsh -i -l -c '/usr/share/code/code'  -p '"0c1d701e5812" + JSON.stringify(process.env) + "0c1d701e5812"'
    0	    98	 20294	fileWatcher [1]

Workspace Stats: 
|  Window (● solutions.py - tdsproj2 - python - Visual Studio Code)
|    Folder (tdsproj2): 6878 files
|      File types: py(3311) pyc(876) pyi(295) so(67) f90(60) txt(41) typed(36)
|                  csv(31) h(28) f(23)
|      Conf files:
"""

def make_http_requests_with_uv(
    url="https://httpbin.org/get", params={"email": "23f2005217@ds.study.iitm.ac.in"}
):
    response = requests.get(url, params=params)
    return response.json()

def run_command_with_npx(
    filePath="README.md", prettier_version="3.4.2", hash_algo="sha256", use_npx=True
):
    prettier_cmd = (
        ["npx", "-y", f"prettier@{prettier_version}", filePath]
        if use_npx
        else ["prettier", filePath]
    )

    try:
        prettier_process = subprocess.run(
            prettier_cmd, capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        print("Error running Prettier:", e)
        return None

    formatted_content = prettier_process.stdout.encode()

    try:
        hasher = hashlib.new(hash_algo)
        hasher.update(formatted_content)
        return hasher.hexdigest()
    except ValueError:
        print(f"Invalid hash algorithm: {hash_algo}")
        return None

def use_google_sheets(
    rows=100, cols=100, start=15, step=12, extract_rows=1, extract_cols=10
):
    matrix = np.arange(start, start + (rows * cols * step), step).reshape(rows, cols)

    extracted_values = matrix[:extract_rows, :extract_cols]

    return np.sum(extracted_values)

def use_excel(values=None, sort_keys=None, num_rows=1, num_elements=9):
    if values is None:
        values = np.array([13, 12, 0, 14, 2, 12, 9, 15, 1, 7, 3, 10, 9, 15, 2, 0])
    if sort_keys is None:
        sort_keys = np.array([10, 9, 13, 2, 11, 8, 16, 14, 7, 15, 5, 4, 6, 1, 3, 12])

    sorted_values = values[np.argsort(sort_keys)]
    return np.sum(sorted_values[:num_elements])

def use_devtools(html=None, input_name=None):
    if html is None:
        html = '<input type="hidden" name="secret" value="12345">'
    if input_name is None:
        input_name = "secret"

    soup = BeautifulSoup(html, "html.parser")
    hidden_input = soup.find("input", {"type": "hidden", "name": input_name})
    
    return hidden_input["value"] if hidden_input else None

def count_wednesdays(start_date="1990-04-08", end_date="2008-09-29", weekday=2):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    count = sum(1 for _ in range((end - start).days + 1) if (start + timedelta(_)).weekday() == weekday)
    return count

def extract_csv_from_a_zip(zip_path, extract_to="extracted_files", csv_filename="extract.csv", column_name="answer"):
    os.makedirs(extract_to, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    csv_path = os.path.join(extract_to, csv_filename)
    
    if not os.path.exists(csv_path):
        for root, _, files in os.walk(extract_to):
            for file in files:
                if file.lower().endswith(".csv"):
                    csv_path = os.path.join(root, file)
                    break
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        if column_name in df.columns:
            return ", ".join(map(str, df[column_name].dropna().tolist()))
    
    return ""

def use_json():
    return ""
    
def multi_cursor_edits_to_convert_to_json():
    return ""
    
def css_selectors():
    return ""
    
def process_files_with_different_encodings():
    return ""
    
def use_github():
    return ""
    
def replace_across_files():
    return ""
    
def list_files_and_attributes():
    return ""
    
def move_and_rename_files():
    return ""
    
def compare_files():
    return ""
    
def sql_ticket_sales():
    return ""
    
def write_documentation_in_markdown():
    return ""
    
def compress_an_image():
    return ""
    
def host_your_portfolio_on_github_pages():
    return ""
    
def use_google_colab():
    return ""
    
def use_an_image_library_in_google_colab():
    return ""
    
def deploy_a_python_api_to_vercel():
    return ""
    
def create_a_github_action():
    return ""
    
def push_an_image_to_docker_hub():
    return ""
    
def write_a_fastapi_server_to_serve_data():
    return ""
    
def run_a_local_llm_with_llamafile():
    return ""
    
def llm_sentiment_analysis():
    return ""
    
def llm_token_cost():
    return ""
    
def generate_addresses_with_llms():
    return ""
    
def llm_vision():
    return ""
    
def llm_embeddings():
    return ""
    
def embedding_similarity():
    return ""
    
def vector_databases():
    return ""
    
def function_calling():
    return ""
    
def get_an_llm_to_say_yes():
    return ""
    
def import_html_to_google_sheets():
    return ""
    
def scrape_imdb_movies():
    return ""
    
def wikipedia_outline():
    return ""
    
def scrape_the_bbc_weather_api():
    return ""
    
def find_the_bounding_box_of_a_city():
    return ""
    
def search_hacker_news():
    return ""
    
def find_newest_github_user():
    return ""
    
def create_a_scheduled_github_action():
    return ""
    
def extract_tables_from_pdf():
    return ""
    
def convert_a_pdf_to_markdown():
    return ""
    
def clean_up_excel_sales_data():
    return ""
    
def clean_up_student_marks():
    return ""
    
def apache_log_requests():
    return ""
    
def apache_log_downloads():
    return ""
    
def clean_up_sales_data():
    return ""
    
def parse_partial_json():
    return ""
    
def extract_nested_json_keys():
    return ""
    
def duckdb_social_media_interactions():
    return ""
    
def transcribe_a_youtube_video():
    return ""
    
def reconstruct_an_image():
    return ""
    