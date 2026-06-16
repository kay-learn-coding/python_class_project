import json
import os
from menu_item import food,drink


#write_DATA
def save_menu_to_json(directory,filename="menu_data.json"):
    """
    Transform object to readable dictionaries and save to json file
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, filename)
    
    serial_data={}

    for key_name, item in directory.items():
        serial_data[key_name]={
            "type": type(item).__name__,
            "name": item.name,
            "cost": item.cost,
            "quantity": item.quantity
        }
    
    with open(full_path, "w") as file:
        json.dump(serial_data,file, indent=4)

    print("Data backed up to JSON file.")


#read_DATA
def load_menu_from_json(filename="menu_data.json"):
    """
    loads JSON records and convert them
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, filename)

    try:
        with open(full_path, "r") as file:
            raw_data=json.load(file)

        loaded_directory={}
        for key,data in raw_data.items():
            item_class=drink if data["type"]=="drink" else food
            loaded_directory[key]=item_class(data["name"],data["cost"],data["quantity"])

        print("Data loaded")
        return loaded_directory
    
    except (FileNotFoundError, json.JSONDecodeError):
        print("no JSON backup found")
        return{}