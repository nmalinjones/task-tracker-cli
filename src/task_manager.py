import json
from datetime import datetime
from os import path, getcwd

test = {
    "id" : 1,
    "description" : "please",
    "status" : "in-progress",
    "createdAt" : 1,
    "updatedAt" : 1
}

def get_json_data(filename : str):
    try:
        with open(filename + "/src/task.json", "r") as f:
            file_data = f.read()
            data = json.loads(file_data)
        print(data)
    except:
        print("Something went wrong in loading the file data")

def create_json_data(filename : str):
    try:
        with open(filename + "/src/task.json", "w") as f:
            data = json.dumps(test)
            f.write(data)
    except:
        print("Something went wrong writing the file data")

create_json_data(getcwd())
get_json_data(getcwd())