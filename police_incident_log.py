import datetime

class Incident:
    def __init__(self, officer, date, description, arrest_made):
        self.officer = officer
        self.date = date
        self.description = description
        self.arrest_made = arrest_made

class Officer:
    def __init__(self, name):
        self.name = name
        self.incidents = []

    def log_incident(self, description, arrest_made):
        incident = Incident(self, datetime.datetime.now(), description, arrest_made)
        self.incidents.append(incident)
        print(f"Incident logged for Officer {self.name}.")

    def get_arrest_rate(self):
        if len(self.incidents) == 0:
            return 0
        else:
            arrests = sum(incident.arrest_made for incident in self.incidents)
            return arrests / len(self.incidents)

# Sample usage
if __name__ == "__main__":
    officer_john = Officer("John")

    officer_john.log_incident("Suspected burglary. No arrest made.", False)
    officer_john.log_incident("Traffic violation. Driver arrested for outstanding warrant.", True)
    officer_john.log_incident("Domestic disturbance. Parties separated, no arrest made.", False)

    print(f"Officer John's arrest rate: {officer_john.get_arrest_rate() * 100}%")
