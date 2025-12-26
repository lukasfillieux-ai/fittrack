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

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS oefeningen (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      naam TEXT NOT NULL,
                      spiergroep TEXT)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS workout_sets (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      oefening_id INTEGER,
                      gewicht REAL,
                      herhalingen INTEGER,
                      datum TEXT,
                      FOREIGN KEY(oefening_id) REFERENCES oefeningen(id))""")

    conn.commit()
    conn.close()