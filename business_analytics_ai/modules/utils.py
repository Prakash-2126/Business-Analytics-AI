import os

def create_directories():

    folders = [
        "data",
        "reports",
        "models"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)