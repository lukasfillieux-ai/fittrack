from .repository import *

def ask(msg):
    return input(msg + ": ")

def add_exercise_flow():
    print("\n--- Nieuwe oefening ---")
    naam = ask("Naam van oefening")
    spier = ask("Spiergroep")
    oefening_toevoegen(naam, spier)
    print(" Oefening toegevoegd!")
    
def show_exercises_flow():
    print("\n--- Alle oefeningen ---")
    for ex in alle_oefeningen():
        print(f"{ex.id}. {ex.naam} ({ex.spier})")
        
def add_set_flow():
    print("\n--- Nieuwe set ---")
    oefening_id = ask("Oefening ID")
    gewicht = ask("Gewicht")
    herhalingen = ask("Herhalingen")
    datum = ask("Datum")
    set_toevoegen(oefening_id, gewicht, herhalingen, datum)
    print(" Set toegevoegd!")
    
def show_sets_flow():
    print("\n--- Sets van oefening ---")
    oefening_id = ask("Exercise ID")
    sets = sets_voor_oefeningen(oefening_id)
    for s in sets:
        print(f"{s.id}: {s.gewicht}kg x {s.herhalingen} op {s.datum}")