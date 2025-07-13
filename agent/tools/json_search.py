import json
from langchain.tools import tool

@tool
def json_search(key: str) -> str:
    """
    Searches for a key in a JSON string and returns the value associated with that key.
    If the key does not exist, it returns a message indicating that the key was not found.

    key is date in format DD-MM-YYYY.
    """
    
    file_path = "db/database.json"

    # Load existing data from JSON file
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return "Database file not found."

    # Search for the key in JSON data
    if key in data:
        return str(data[key])
    else:
        return "Key not found."