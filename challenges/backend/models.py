"""
"""


import json


# path to list of repositories
JSON_DATA = "data.json"


# if GitHub-API rate limit exceeded
def get_data_json():
    """ read data stored in `data.json`.
    """
    with open(JSON_DATA, 'r') as file:
        return json.loads(file.read())

# Store the list of repositories in `data.json`.
def set_data_json(list_repos):
    """ Store the list of repositories in `data.json`.
    """
    with open(JSON_DATA, 'w') as file:
        file.write(json.dumps(list_repos))
