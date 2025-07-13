import json
from langchain.tools import tool
import datetime

@tool
def json_insert(value: str) -> str:
        """
                Inserts a value into a JSON file with the current date as the key.
                The value is expected to be a string that can be converted to an integer.
                If the JSON file does not exist, it will be created.
                The JSON file is located at "db/database.json".
                The value is added to the existing value for the current date, or a new entry is created if it does not exist.
                Returns a message indicating the updated JSON file content.
                value is a string that can be converted to an integer.
                Example usage:
                json_insert("100")
                                
        """

        file_path = "db/database.json"

        # Load existing data from JSON file
        try:
                with open(file_path, 'r') as file:
                        data = json.load(file)
                
                # Convert value to int
                value = int(value)      

                print(f"Baza wygląda tak: {data}")

        except:
                print("nie działa, nie mogę wczytać pliku JSON")

        
        key = datetime.datetime.now().strftime("%d-%m-%Y")

        # Insert key to JSON data
        if key in data:
                data[key] = value
        else:
                data[key] = value 

        print(f"Zaktualizowana baza wygląda tak: {data}")

        data_return = json.dumps(data, indent=4)
        # Save updated data back to JSON file
        with open(file_path, 'w') as file:
                file.write(data_return)
        
        return f" Our database JSON file looks like this: {data_return}"