import httpx
import os

function_definitions_llm = [
    {
        "name": "send_http_request",
        "description": "Send an HTTP request with specified data.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL to send the request to."
                },
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "Email parameter to pass in the request."
                        }
                    },
                    "required": ["email"]
                }
            },
            "required": ["url", "parameters"]
        }
    },
    {
        "name": "calculate_sum_in_sheet",
        "description": "Calculate the result of a formula in Google Sheets or Excel.",
        "parameters": {
            "type": "object",
            "properties": {
                "formula": {
                    "type": "string",
                    "description": "Formula used in Google Sheets or Excel."
                },
                "tool": {
                    "type": "string",
                    "description": "Spreadsheet tool (e.g., Google Sheets, Excel)."
                }
            },
            "required": ["formula", "tool"]
        }
    },
    {
        "name": "extract_css_data_value_sum",
        "description": "Extract the sum of the data-value attributes for specific HTML elements using CSS selectors.",
        "parameters": {
            "type": "object",
            "properties": {
                "html_content": {
                    "type": "string",
                    "description": "HTML content to parse."
                },
                "css_selector": {
                    "type": "string",
                    "description": "CSS selector used to match elements."
                }
            },
            "required": ["html_content", "css_selector"]
        }
    },
    {
        "name": "process_file_encodings",
        "description": "Process files with different text encodings and calculate the sum of specific values.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_details": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "file_name": {"type": "string", "description": "File name."},
                            "encoding": {"type": "string", "description": "File encoding type."}
                        },
                        "required": ["file_name", "encoding"]
                    }
                },
                "symbols": {
                    "type": "array",
                    "items": {"type": "string", "description": "Symbols to match and sum values for."}
                }
            },
            "required": ["file_details", "symbols"]
        }
    },
    {
        "name": "run_sql_query",
        "description": "Execute a SQL query to calculate total sales.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "SQL query to execute."
                },
                "database_schema": {
                    "type": "object",
                    "description": "Details of the database schema.",
                    "properties": {
                        "table_name": {"type": "string", "description": "Name of the table."},
                        "columns": {"type": "array", "items": {"type": "string", "description": "Columns in the table."}}
                    },
                    "required": ["table_name", "columns"]
                }
            },
            "required": ["query", "database_schema"]
        }
    },
    {
        "name": "write_markdown_documentation",
        "description": "Generate Markdown documentation for a project.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Main title of the Markdown document."},
                "sections": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "heading": {"type": "string", "description": "Heading of the section."},
                            "content": {"type": "string", "description": "Content of the section."}
                        },
                        "required": ["heading", "content"]
                    }
                }
            },
            "required": ["title", "sections"]
        }
    },
    {
        "name": "deploy_to_vercel",
        "description": "Deploy a Python API application to Vercel.",
        "parameters": {
            "type": "object",
            "properties": {
                "api_endpoints": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "endpoint": {"type": "string", "description": "API endpoint URL."},
                            "parameters": {"type": "object", "description": "Parameters accepted by the endpoint."}
                        },
                        "required": ["endpoint"]
                    }
                }
            },
            "required": ["api_endpoints"]
        }
    },
    {
        "name": "build_fastapi_application",
        "description": "Build a FastAPI application that processes queries and routes to appropriate functions.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_parameters": {
                    "type": "string",
                    "description": "Query string passed to the API."
                },
                "routes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "function_name": {"type": "string", "description": "Function name to route to."},
                            "arguments": {"type": "object", "description": "Arguments for the function."}
                        },
                        "required": ["function_name", "arguments"]
                    }
                }
            },
            "required": ["query_parameters", "routes"]
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
