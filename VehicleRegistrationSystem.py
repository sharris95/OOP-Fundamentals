#VehicleRegistrationSystem

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {self.owner}")

vehicle1 = Vehicle("123ABC", "Car", "Alice")
vehicle2 = Vehicle("456DEF", "Motorbike", "Bob")

print(f"Vehicle1 - Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle2 - Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

vehicle1.update_owner("Charlie")
vehicle2.update_owner("Dave")
print(f"Vehicle1 - Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle2 - Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")