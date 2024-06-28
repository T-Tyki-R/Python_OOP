# City Infrastructure Management System

class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def get_info(self):
              return f" The registration number of {self.owner}'s {self.type} is {self.registration_number}."
        def update_owner(self, person):
              self.owner = person
              return f" The new owner is {self.owner}."

car_1 = Vehicle("123456", "Totoya", "Billy")
car_2 = Vehicle("220019", "Nissan", "Kelly")

print(car_1.get_info())
print(car_2.update_owner("Jane"))

