import json
import os

def load_index(filepath) -> dict:
    # check if the index.json file exists
    if os.path.exists(filepath):
        # read in the file and return the index
        with open(filepath, "r") as index_file:
            index = json.load(index_file)
    else:
        return {}
    
    return index


def save_index(index, filename="index.json"):
    # save the index to the index.json file
    with open(filename, "w") as index_file:
        json.dump(index, index_file, indent=4)
