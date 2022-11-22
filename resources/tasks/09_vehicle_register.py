from typing import List
"""
    vvvv      YOUR SOLUTION      vvvv
"""


class Person:

    def __init__(self, name: str, surname: str, age: int) -> None:

    def __eq__(self, other: 'Person') -> bool:

    def get_vehicle_count(self) -> int:

class Vehicle:

    def __init__(self, registration_plate: str, creation_date: str, owner: Person) -> None:

    def __eq__(self, other: 'Vehicle') -> bool:


class Register:

    def __init__(self) -> None:

    def insert_vehicle(self, vehicle: Vehicle) -> int:

    def update_vehicle_owner(self, registration_plate: str, new_owner: Person) -> int:

    def delete_vehicle(self, registration_plate: str) -> int:

    def list_vehicles(self) -> List[Vehicle]:

    def list_owners(self) -> List[Person]:

    def list_vehicle_by_owner(self, owner: Person) -> List[Vehicle]:


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


register = Register()

person1 = Person("John", "Doe", 20)
person2 = Person("Alice", "Doe", 22)

car1 = Vehicle("abc0", "20221122", person1)
car2 = Vehicle("abc1", "20221123", person1)
car3 = Vehicle("abc0", "20221122", person1)
car4 = Vehicle("xyz", "20221124", person2)

# car1 = Vehicle("abc", "20221122", person1)

# test insertion
assert register.insert_vehicle(car1) == 1
assert register.insert_vehicle(car2) == 1
assert register.insert_vehicle(car3) == 0
assert register.insert_vehicle(car4) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 2 and register.list_owners()[1].get_vehicle_count() == 1

# test update
assert register.update_vehicle_owner("abc1", person1) == 0
assert register.update_vehicle_owner("not in register", person1) == 0
assert register.update_vehicle_owner("abc1", person2) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person2), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 1 and register.list_owners()[1].get_vehicle_count() == 2
assert register.update_vehicle_owner("abc0", person2) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person2), Vehicle("abc1", "20221123", person2), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 3

# test delete
assert register.delete_vehicle("not in register") == 0
assert register.delete_vehicle("abc0") == 1
assert register.delete_vehicle("abc1") == 1
assert register.delete_vehicle("xyz") == 1
assert register.list_vehicles() == []
assert register.list_owners() == []

# test lists
car1 = Vehicle("abc0", "20221122", person1)
car2 = Vehicle("abc1", "20221123", person1)
car3 = Vehicle("abc0", "20221122", person1)
car4 = Vehicle("xyz", "20221124", person2)

register.insert_vehicle(car1)
register.insert_vehicle(car2)
register.insert_vehicle(car3)
register.insert_vehicle(car4)

assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)]
assert register.list_vehicle_by_owner(person1) == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1)]

