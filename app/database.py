import json
import sqlite3
import os

def load_settings():
    with open("settings.json", "r") as f:
        return json.load(f)