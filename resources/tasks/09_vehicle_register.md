# 09 - Vehicle Register

In this task we will want to implement register of vehicles which will allow us to add vehicles, update their owner in case of new registration and delete the vehicles out of the database. The register will also track all current owners of registered vehicles.

Your goal is to implement methods of several classes which are representing the register, vehicles registered in it and owners of each vehicle.


There are following classes:
* `Person` - represents owners of vehicles and tracks its number of vehicles
  * methods:
    * `__init__` - initializes Person with given `name`, `surname`, `age` and also sets its protected attribute (leading `_`) `vehicle_count` to 0
    * `__eq__` - compares two persons
      * persons are equal if they have same `name`, `surname` and `age`
    * get_vehicle_count() - returns the value of protected attribute `vehicle_count`
* `Vehicle` - represents one Vehicle
  * methods:
    * `__init__` - initializes Vehicle with given `registration_plate`, `creation_date`, `owner`
    * `__eq__` - compares two vehicles
      * vehicles are equal if they have same `registration_plate`
* `Register` - represents the whole register of vehicles and persons
  * child class of Entity
    * methods:
      * `insert_vehicle` - inserts vehicle into register
        * if vehicle already exists in register - abort insertion, return 0
        * if vehicle doesn't exist - insert it, return 1
          * if owner of new vehicle doesn't exist in register add him
      * `update_vehicle_owner` - updates owner of vehicle if conditions are met
        * if vehicle doesn't exist or old owner is the same as new owner - abort update, return 0
        * else update owner of vehicle and return 1 
      * `delete_vehicle` - deletes vehicle from register
        * if vehicle doesn't exist - abort delete, return 0
        * else delete vehicle from register and return 1
      * `list_vehicles` - returns list of currently registered vehicles
        * order of vehicles in list is the same as order of their insertion
      * `list_owners` - returns list of currently registered owners
        * order of owners in list is the same as order of their insertion
      * `list_vehicle_by_owner` - returns list of currently registered vehicles of specified person
        * order of vehicles in list is the same as order of their insertion

Important notes:
* if a person has no vehicles registered to them (its vehicle_count is zero) it cannot stay in register and must be removed (update and delete methods)
* all list methods must return the list of Vehicles or Persons respecting order of their registration (first registered will be first in the returned list)
* you can use any data structure for inner implementation of Register, just make sure that ale methods are returning defined outputs


The basic interface is prepared in provided [template](09_vehicle_register.py).

You can implement your own methods and classes if you want or need them. Also it is allowed to use different print functions everywhere you need them. Try to make it pretty.

There is imported `List` from `typing` to ensure backwards compatibility. Do not use any other imports, or you will get 0 points. All you need is just pure python.