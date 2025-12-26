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