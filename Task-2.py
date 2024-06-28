# Event Management System Enhancement

class Event:
        def __init__(self, name, date, participant):
            self.name = name
            self.date = date
            self.participant_num = participant

        def add_participant(self): #Confused on what needs to be done
              return f"The number of participant attending the {self.name} on {self.date} is: {self.participant_num}"
        
        def get_participant_count(self):
              return self.participant_num
        
event_1 = Event("Gala", "March 8", 12)

print(event_1.add_participant())
print(event_1.get_participant_count())