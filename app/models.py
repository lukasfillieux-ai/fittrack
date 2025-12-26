class oefening:
    def __init__(self, id, naam, spier):
        self.id = id
        self.naam = naam
        self.spier = spier
        
class workoutset:
    def __init__(self, id, oefening_id, gewicht, herhalingen, datum):
        self.id = id
        self.oefening_id = oefening_id
        self.gewicht = gewicht
        self.herhalingen = herhalingen
        self.datum = datum