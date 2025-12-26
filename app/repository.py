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