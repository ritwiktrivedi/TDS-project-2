import httpx
import os

# Define the JSON schema for function extraction
function_definitions_llm = [
    {
        "name": "extract_parameters",
        "description": "Extract structured parameters from a given user query.",
        "parameters": {
            "type": "object",
            "properties": {
                "task_type": {"type": "string", "description": "Type of task (e.g., run command, make HTTP request)."},
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string", "description": "URL mentioned in the query.", "nullable": True},
                        "email": {"type": "string", "description": "Email address extracted from the query.", "nullable": True},
                        "command": {"type": "string", "description": "Shell command extracted from the query.", "nullable": True},
                        "formula": {"type": "string", "description": "Formula mentioned in the query.", "nullable": True},
                        "filename": {"type": "string", "description": "Filename mentioned in the query.", "nullable": True}
                    },
                    "additionalProperties": False
                }
            },
            "required": ["task_type", "parameters"]
        }
    }
]

# OpenAI API settings
openai_api_chat = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"  
openai_api_key = os.getenv("AIPROXY_TOKEN")  

headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json",
}

def extract_parameters(prompt: str):
    """Send a user query to OpenAI API and extract structured parameters."""
    with httpx.Client(timeout=20) as client:
        response = client.post(
            openai_api_chat,
            headers=headers,
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are an intelligent assistant that extracts structured parameters from user queries."},
                    {"role": "user", "content": prompt}
                ],
                "tools": [
                    {"type": "function", "function": function}
                    for function in function_definitions_llm
                ],
                "tool_choice": "auto"
            },
        )

    # Parse response
    response_data = response.json()
    if "choices" in response_data and "tool_calls" in response_data["choices"][0]["message"]:
        extracted_data = response_data["choices"][0]["message"]["tool_calls"][0]["function"]
        print(extracted_data)
        return extracted_data
    else:
        print("No parameters detected")
        return None

# Example usage
queries = [
    "Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2005217@ds.study.iitm.ac.in",
    "Run npx -y prettier@3.4.2 README.md | sha256sum.",
    "Type this formula in Google Sheets: =SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 15, 12), 1, 10))",
    "Save the output in output.txt"
]

for query in queries:
    result = extract_parameters(query)
    print(result)
