# Beschrijving
Dit is een command-line applicatie waarbij je oefeningen kunt opslaan, workoutsets toevoegen en deze dan exporteren naar een .csv bestand

## Functionaliteiten
- Oefeningen toevoegen
- Oefeningen opvragen
- Workout sets toevoegen
- Sets opvragen
- CSV bestand exporteren




## Installatie
1. Maak een virtual environment:
python -m venv venv

venv\Scripts\activate

(als dit niet direct werkt doe dan eerst dit: 
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
)
(dit werkte toch voor mij)

2. Installeer dependencies:
pip install -r requirements.txt

3. Maak een `settings.json` gebaseerd op `settings_example.json` en plaats deze in het mapje fittrack 

(het databasebestand wordt ook in deze map opgeslagen vanaf je de applicatie start)

4. Start de applicatie:
python -m app.main




## Gebruik
1. Oefening toevoegen
Eerst geef je de naam van een oefening (bv.: Benchpress). 
Daarna geef je de spiergroep in die deze oefening traint.

2. Oefeningen tonen
Hier zie je alle oefeningen die je hebt toegevoegd

3. Set toevoegen
Eerst geef je het ID in van de oefening die je hebt gedaan(zie oefening toevoegen het cijfer met het puntje). 
Daarna geef je het gewicht in (in kg) die je hebt gedaan. 
Dan geef je het aantal herhalingen die je hebt gedaan (bv.: 10). 
Als laatste kan je nog de datum ingeven wanneer je deze set hebt gedaan(DD/MM/JJJJ). 

4. Sets tonen
Eerst geef je het oefening ID(zie oefening toevoegen het cijfer met het puntje). 
Daarna zie je het aantal sets dat je al van deze oefening hebt gedaan.

5. CSV exporteren
Het CSV bestand wordt opgeslagen in het mapje fittrack

6. Afsluiten
Het programma wordt afgesloten!