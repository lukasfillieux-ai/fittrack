from .database import get_connection

def oefening_toevoegen(naam, spier):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO oefeningen (naam, spiergroep) VALUES (?, ?)",
                (naam, spier))
    conn.commit()
    conn.close()