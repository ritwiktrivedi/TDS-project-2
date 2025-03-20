titles = [
    "VS Code Version",
    "Make HTTP requests with uv",
    "Run command with npx",
    "Use Google Sheets",
    "Use Excel",
    "Use DevTools",
    "Count Wednesdays",
    "Extract CSV from a ZIP",
    "Use JSON",
    "Multi-cursor edits to convert to JSON",
    "CSS selectors",
    "Process files with different encodings",
    "Use GitHub",
    "Replace across files",
    "List files and attributes",
    "Move and rename files",
    "Compare files",
    "SQL: Ticket Sales",
    "Write documentation in Markdown",
    "Compress an image",
    "Host your portfolio on GitHub Pages",
    "Use Google Colab",
    "Use an Image Library in Google Colab",
    "Deploy a Python API to Vercel",
    "Create a GitHub Action",
    "Push an image to Docker Hub",
    "Write a FastAPI server to serve data",
    "Run a local LLM with Llamafile",
    "LLM Sentiment Analysis",
    "LLM Token Cost",
    "Generate addresses with LLMs",
    "LLM Vision",
    "LLM Embeddings",
    "Embedding Similarity",
    "Vector Databases",
    "Function Calling",
    "Get an LLM to say Yes",
    "Import HTML to Google Sheets",
    "Scrape IMDb movies",
    "Wikipedia Outline",
    "Scrape the BBC Weather API",
    "Find the bounding box of a city",
    "Search Hacker News",
    "Find newest GitHub user",
    "Create a Scheduled GitHub Action",
    "Extract tables from PDF",
    "Convert a PDF to Markdown",
    "Clean up Excel sales data",
    "Clean up student marks",
    "Apache log requests",
    "Apache log downloads",
    "Clean up sales data",
    "Parse partial JSON",
    "Extract nested JSON keys",
    "DuckDB: Social Media Interactions",
    "Transcribe a YouTube video",
    "Reconstruct an image",
]

import pandas as pd

df = pd.read_csv("training_dataset.csv")

questions = df["QUESTION"] 

def function_case(title):
    title = title.lower()
    title = title.replace(" ", "_")
    title = title.replace(":", "")
    title = title.replace("-", "_")
    title = title.replace("(", "")
    title = title.replace(")", "") 
    title = title.replace("?", "")
    title = title.replace(",", "")
    return title

obj = {}

for i in range(len(titles)):
    for question in questions:
        obj[function_case(titles[i])] = question

# store in a json file

import json

with open("questions.json", "w") as f:
    json.dump(obj, f, indent=4)