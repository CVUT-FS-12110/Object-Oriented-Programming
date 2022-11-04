"""
Memento pattern example.
"""
class SavedLocation:
    
    def __init__(self, state):
        self._location = state

    def get_location(self):
        return self._location

class Maze:

    def set(self, state):
        self._location = state

    def display(self):
        print(self._location)

    def save_location(self):
        return SavedLocation(self._location)

    def load_location(self, location):
        self._location = location.get_location()


maze = Maze()
maze.set("Room1")
maze.set("Room2")
maze.display()
saved_location = maze.save_location()
maze.set("Room3")
maze.display()
maze.load_location(saved_location)
maze.display()
