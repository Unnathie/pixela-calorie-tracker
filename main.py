import requests
import os
from datetime import datetime

# Pixela API endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "unnathi"
TOKEN = os.getenv("TOKEN-ENV")

HEADERS = {
    "X-USER-TOKEN": TOKEN
}


def create_user():
    """Create a Pixela user account."""
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    res = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(res.text)


def create_graph():
    """Create a new graph on Pixela."""
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        "id": "graph4",
        "name": "Walking",
        "unit": "calorie",
        "type": "float",
        "color": "ajisai"
    }
    res = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(res.text)


def add_pixel(quantity: str):
    """Add a new pixel (daily entry) to the graph."""
    today = datetime.now().strftime("%Y%m%d")
    pixel_data = {
        "date": today,
        "quantity": quantity
    }
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph4"
    res = requests.post(url=pixel_endpoint, json=pixel_data, headers=HEADERS)
    print(res.text)


def update_pixel(quantity: str, date: str = None):
    """Update an existing pixel entry."""
    if not date:
        date = datetime.now().strftime("%Y%m%d")
    update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph4/{date}"
    res = requests.put(url=update_endpoint, json={"quantity": quantity}, headers=HEADERS)
    print(res.text)


def delete_pixel(date: str = None):
    """Delete a pixel entry."""
    if not date:
        date = datetime.now().strftime("%Y%m%d")
    delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph4/{date}"
    res = requests.delete(url=delete_endpoint, headers=HEADERS)
    print(res.text)


if __name__ == "__main__":
    # Example run: add today's calories
    today_str = datetime.now().strftime("%d")
    calories = input(f"How many calories did you burn? on {today_str} ")
    add_pixel(calories)
