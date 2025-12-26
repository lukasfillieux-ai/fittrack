import json
import sqlite3
import os

def load_settings():
    with open("settings.json", "r") as f:
        return json.load(f)

def get_connection():
    settings = load_settings()
    path = settings["database_path"]
    return sqlite3.connect(path)