import requests


database = {
    "user": {
        1: {"name": "John", "age": 22},
        2: {"name": "Doe", "age": 25},
        3: {"name": "Smith", "age": 30},
    }
}


def get_user_by_user_id(user_id):
    return database["user"].get(user_id, None)


def get_user_by_name(name):
    for _, user in database["user"].items():
        if user["name"] == name:
            return user
    return None


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError("Failed to fetch users")
