# City Infrastructure Management System

class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self):
              return f" The registration number of {self.owner}'s {self.type} is {self.registration_number}."

car_1 = Vehicle("123456", "Totoya", "Billy")
car_2 = Vehicle("220019", "Nissan", "Kelly")

print(car_1.update_owner())
print(car_2.update_owner())

