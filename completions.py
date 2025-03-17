import httpx
import os

function_definitions_llm = [
    {
            "name": "test",
            "description": "Run a Python script from a given URL, passing an email as the argument.",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "pattern": r"[\w\.-]+@[\w\.-]+\.\w+"}
                },
                "required": ["filename", "targetfile", "email"]
            }
        },
]

openai_api_chat  = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions" # for testing
openai_api_key = os.getenv("AIPROXY_TOKEN")

headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json",
}

def get_completions(prompt: str):
    with httpx.Client(timeout=20) as client:
        response = client.post(
            f"",
            headers=headers,
            json=
                {
                    "model": "gpt-4o-mini",
                    "messages": [
                                    {"role": "system", "content": "You are a function classifier that extracts structured parameters from queries."},
                                    {"role": "user", "content": prompt}
                                ],
                    "tools": [
                                {
                                    "type": "function",
                                    "function": function
                                } for function in function_definitions_llm
                            ],
                    "tool_choice": "auto"
                },
        )
    print(response.json()["choices"][0]["message"]["tool_calls"][0]["function"])
    return response.json()["choices"][0]["message"]["tool_calls"][0]["function"]
