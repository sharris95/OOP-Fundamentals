#event_management_system_enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants_count = 0
    def add_participant(self):
        self.participants_count += 1
        print(f"Participant added. Total participants: {self.participants_count}")
    def get_participant_count(self):
        return self.participants_count
event1 = Event("Music Concert", "2024-08-15")
event1.add_participant()
event1.add_participant()
print(f"Event: {event1.name}, Date: {event1.date}, Participants: {event1.get_participant_count()}")
