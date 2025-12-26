from .database import get_connection
from .models import oefening, workoutset

def oefening_toevoegen(naam, spier):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO oefeningen (naam, spiergroep) VALUES (?, ?)",
                (naam, spier))
    conn.commit()
    conn.close()
    
def alle_oefeningen():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM oefeningen")
    rows = cur.fetchall()
    conn.close()
    return [oefening(*row) for row in rows]

def set_toevoegen(oefening_id, gewicht, herhalingen, datum):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                INSERT INTO workout_sets (oefening_id, gewicht, herhalingen, datum)
                VALUES (?, ?, ?, ?)
                """, 
                (oefening_id, gewicht, herhalingen, datum))
    conn.commit()
    conn.close()
    
def sets_voor_oefeningen(oefening_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM workout_sets WHERE oefening_id = ?",
                (oefening_id,))
    rows = cur.fetchall()
    conn.close()
    return [workoutset(*row) for row in rows]