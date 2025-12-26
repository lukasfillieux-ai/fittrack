from .database import init_db
from .ui import *
def main():
    init_db()
    while True:
        print("\nMenu\nTyp een cijfer en druk op enter\n")
        print("1-Oefening toevoegen")
        print("2-Oefeningen tonen")
        print("3-Set toevoegen")
        print("4-Sets tonen")
        print("5-CSV exporteren")
        print("6-Afsluiten")
        
        choice = input("- ")
        
        if choice == "1":
            add_exercise_flow()
        elif choice == "2":
            show_exercises_flow()
        elif choice == "3":
            add_set_flow()
        elif choice == "4":
            show_sets_flow()
        elif choice == "5":
            sets_naar_csv()
            print("lijst.csv aangemaakt!")
        elif choice == "6":
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige keuze.")
            
if __name__ == "__main__":
    main()
