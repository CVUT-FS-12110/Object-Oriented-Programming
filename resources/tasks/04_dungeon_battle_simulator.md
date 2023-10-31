# 04 - Dungeon Battle Simulator

Your task is to implement methods of several classes which are chained in inharitance.

There are following classes:

* `Entity` - default and top parent class
  * represents generally every entity in the board
  * methods:
    * `__init__` - initializes Entity with name, coordinates and hit_points
    * `take_damage` - abstract method to be overriden
    * `is_alive` - check if entity is alive according to it's hit_points
    * `get_distance` - counts Manhattan/Taxicab distance to another entity
* `Rock`
  * child class of Entity
  * methods:
    * `take_damage` - applies damage to Rock
      * overriden method
      * Rock can be damaged by 1 hit_point each time it is hit with damage_amount of at least 10
* `Furniture`
  * child class of Entity
  * methods:
    * `take_damage` - applies damage to Furniture
      * overriden method
      * Furniture is damaged by whole damage_amount it gets
* `LivingEntity`
  * child class of Entity
  * methods:
    * `__init__` - initializes LivingEntity with Entity constructor and level, damage and range
      * overriden method, calls parent method
    * `level_up` - increase level of LivingEntity by 1
    * `take_damage` - applies damage to LivingEntity
      * overriden method
      * LivingEntity is damaged by whole damage_amount it gets 
    * `hit` - abstract method to be overriden
    * `move` - moves LivingEntity on the board by provided vector
      * using 2D plane with `x` and `y` coordinates
      * move vector and coordinates can hold both positive and negative x/y values
      * the +/- defines the direction in specific axis
    * `in_range` - check if distance of other entity is less or equal to LivingEntity range
* `Warrior`
  * child class of LivingEntity
  * methods:
    * `hit` - hits another entity by calling its own take_damage method
      * overriden method
      * must check if enemy is in range
      * if enemy is out of range do nothing
    * `take_damage` - applies damage to Warrior
      * overriden method
      * Warrior is damaged by difference between his level and the damage_amount, if the damage is higher
    * `level_up` - increase level of LivingEntity and increase damage by 1 and hit_points by 2
      * overriden method, calls parent method
* `Archer`
  * child class of LivingEntity
  * methods:
    * `hit` - hits another entity by calling its own take_damage method
      * overriden method 
      * must check if enemy is in range
      * if enemy is out of range do nothing
    * `level_up` - increase level of LivingEntity and increase damage by 2 and hit_points by 1
      * overriden method, calls parent method


The basic interface is prepared in provided [template](04_dungeon_battle_simulator.py). There is also additional description to the implementation. Read it carefully.

You can implement your own methods and classes if you want or need them. Also it is allowed to use different print functions everywhere you need them. Try to make it pretty.

There is imported `Tuple` from `typing` to ensure backwards compatibility. Do not use any other imports. All you need is just pure python.
