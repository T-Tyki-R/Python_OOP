# Event Management System Enhancement

class Event:
        def __init__(self, name, date, participant):
            self.name = name
            self.date = date
            self.participant_num = participant

        def add_participant(self, people): #Confused on what needs to be done
            self.participant_num += people
        
        def get_participant_count(self):
            return self.participant_num
        
event_1 = Event("Gala", "March 8", 12)

print(event_1.add_participant(5))
print(event_1.get_participant_count())