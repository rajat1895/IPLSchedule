import requests


def get_data(api):
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("successfully fetched the data")
        json_data = response.json()
        return json_data
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")


